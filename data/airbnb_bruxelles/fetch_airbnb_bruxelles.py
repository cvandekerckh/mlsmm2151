"""
Prépare les jeux de données Airbnb Bruxelles utilisés comme fil rouge du cours.

Ce script n'est PAS exécuté par les étudiants. Il sert à documenter la provenance
des données et à régénérer les fichiers publiés en asset de release GitHub.
Les fichiers produits ne sont jamais commités : voir data/README.md.

Source   : Inside Airbnb, https://insideairbnb.com/get-the-data/
Snapshot : Bruxelles, 21 juin 2025 (figé volontairement, voir NOTE ci-dessous)
Licence  : Creative Commons CC BY 4.0

NOTE sur le choix du snapshot
-----------------------------
Inside Airbnb republie ses données chaque trimestre et l'ancienne URL disparaît.
Le snapshot est donc figé à une date précise pour que le cours reste reproductible
d'une année sur l'autre. Le scrape du 27 juin 2026 a été écarté : plusieurs
colonnes y sont vides à 100 % (host_since, host_response_time, instant_bookable),
ce qui détruit les exemples des chapitres 3 et 4.

Trois fichiers sont produits :

  airbnb_bruxelles_raw.csv    Données brutes, volontairement sales.
                              Utilisé aux chapitres 0 à 4 (exploration, nettoyage).

  airbnb_bruxelles_train.csv  Table de modélisation propre, 80 %.
  airbnb_bruxelles_test.csv   Table de modélisation propre, 20 %.
                              Utilisées aux chapitres 5 à 12. Elles existent pour
                              que la modélisation ne dépende pas de la qualité du
                              nettoyage fait par chaque étudiant au chapitre 3.

Convention de nommage des colonnes
----------------------------------
Seules les cibles sont préfixées, pour qu'aucune ambiguïté ne soit possible :
  y_price      cible de régression      prix par nuit en euros
  y_superhost  cible de classification  l'hôte a-t-il le statut Superhost

Les variables explicatives gardent leur nom d'origine Inside Airbnb : c'est ce
que les étudiants rencontreront dans la vraie vie, et le codebook les documente.

Usage :
    python fetch_airbnb_bruxelles.py [--out DOSSIER]
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd

SOURCE_URL = (
    "https://data.insideairbnb.com/belgium/bru/brussels/2025-06-21/data/listings.csv.gz"
)

# Graine fixe : deux exécutions successives doivent produire des fichiers identiques.
SEED = 2151

# Colonnes conservées dans le fichier brut. Certaines sont volontairement
# inutilisables (license est vide à 100 %) : les repérer fait partie du chapitre 3.
COLONNES_BRUTES = [
    "id",
    "name",
    "host_id",
    "host_since",
    "host_response_time",
    "host_response_rate",
    "host_acceptance_rate",
    "host_is_superhost",
    "host_listings_count",
    "host_identity_verified",
    "neighbourhood_cleansed",
    "latitude",
    "longitude",
    "property_type",
    "room_type",
    "accommodates",
    "bathrooms",
    "bathrooms_text",
    "bedrooms",
    "beds",
    "amenities",
    "price",
    "minimum_nights",
    "maximum_nights",
    "availability_30",
    "availability_365",
    "number_of_reviews",
    "first_review",
    "last_review",
    "review_scores_rating",
    "review_scores_cleanliness",
    "review_scores_location",
    "review_scores_value",
    "instant_bookable",
    "reviews_per_month",
    "estimated_occupancy_l365d",
    "estimated_revenue_l365d",
    "license",
]


def telecharger() -> pd.DataFrame:
    print(f"Téléchargement de {SOURCE_URL}")
    df = pd.read_csv(SOURCE_URL, low_memory=False)
    print(f"  {df.shape[0]} annonces, {df.shape[1]} colonnes")
    return df


def construire_brut(df: pd.DataFrame) -> pd.DataFrame:
    """Fichier brut : on sélectionne des colonnes, on ne nettoie rien."""
    brut = df[COLONNES_BRUTES].copy()
    # Tri stable par identifiant pour que le fichier soit reproductible à l'octet près.
    brut = brut.sort_values("id").reset_index(drop=True)
    return brut


def _prix_en_nombre(serie: pd.Series) -> pd.Series:
    """'$1,234.00' -> 1234.0"""
    return pd.to_numeric(
        serie.astype(str).str.replace(r"[$,]", "", regex=True), errors="coerce"
    )


def _taux_en_nombre(serie: pd.Series) -> pd.Series:
    """'95%' -> 0.95"""
    return pd.to_numeric(
        serie.astype(str).str.rstrip("%"), errors="coerce"
    ) / 100.0


def _oui_non(serie: pd.Series) -> pd.Series:
    """'t' / 'f' -> 1 / 0"""
    return serie.map({"t": 1, "f": 0}).astype("Int64")


def _nb_equipements(serie: pd.Series) -> pd.Series:
    """La colonne amenities est une liste JSON stockée en texte."""
    return serie.fillna("[]").str.count(",").add(1).where(serie.notna(), 0)


def construire_modelisation(brut: pd.DataFrame) -> pd.DataFrame:
    """Table propre pour les chapitres 5 à 12.

    Le nettoyage appliqué ici est exactement celui que les étudiants
    reconstruisent eux-mêmes aux chapitres 3 et 4.
    """
    df = brut.copy()

    df["y_price"] = _prix_en_nombre(df["price"])
    df["y_superhost"] = _oui_non(df["host_is_superhost"])

    df["host_response_rate"] = _taux_en_nombre(df["host_response_rate"])
    df["host_acceptance_rate"] = _taux_en_nombre(df["host_acceptance_rate"])
    df["host_identity_verified"] = _oui_non(df["host_identity_verified"])
    df["instant_bookable"] = _oui_non(df["instant_bookable"])

    # Ancienneté de l'hôte et du logement, en années, à la date du snapshot.
    date_snapshot = pd.Timestamp("2025-06-21")
    for source, cible in [
        ("host_since", "anciennete_hote_annees"),
        ("first_review", "anciennete_annonce_annees"),
        ("last_review", "derniere_review_annees"),
    ]:
        dates = pd.to_datetime(df[source], errors="coerce")
        df[cible] = (date_snapshot - dates).dt.days / 365.25

    df["nb_equipements"] = _nb_equipements(df["amenities"])

    # On retire les lignes sans cible : un modèle ne s'entraîne pas sur une cible manquante.
    df = df.dropna(subset=["y_price", "y_superhost"])

    # Prix aberrants. Le seuil est discuté au chapitre 3 ; on coupe aux extrêmes
    # évidents (annonces à 8 euros ou à 15 000 euros la nuit).
    df = df[(df["y_price"] >= 20) & (df["y_price"] <= 1000)]

    # Séjours minimum absurdes (jusqu'à 500 nuits dans les données brutes).
    df = df[df["minimum_nights"] <= 365]

    colonnes_finales = [
        "id",
        "y_price",
        "y_superhost",
        "neighbourhood_cleansed",
        "property_type",
        "room_type",
        "accommodates",
        "bathrooms",
        "bedrooms",
        "beds",
        "nb_equipements",
        "minimum_nights",
        "maximum_nights",
        "availability_30",
        "availability_365",
        "number_of_reviews",
        "reviews_per_month",
        "review_scores_rating",
        "review_scores_cleanliness",
        "review_scores_location",
        "review_scores_value",
        "host_response_rate",
        "host_acceptance_rate",
        "host_listings_count",
        "host_identity_verified",
        "instant_bookable",
        "anciennete_hote_annees",
        "anciennete_annonce_annees",
        "derniere_review_annees",
        "latitude",
        "longitude",
        # Conservée volontairement : elle vaut à peu près prix × occupation et sert
        # d'exemple de fuite de données au chapitre 5.
        "estimated_revenue_l365d",
    ]
    return df[colonnes_finales].sort_values("id").reset_index(drop=True)


def decouper(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Découpage 80 / 20 stratifié sur y_superhost, déterministe."""
    rng = np.random.default_rng(SEED)
    parts = []
    for _, groupe in df.groupby("y_superhost", sort=True):
        indices = groupe.index.to_numpy()
        melange = rng.permutation(indices)
        coupe = int(round(0.8 * len(melange)))
        parts.append((melange[:coupe], melange[coupe:]))

    idx_train = np.sort(np.concatenate([p[0] for p in parts]))
    idx_test = np.sort(np.concatenate([p[1] for p in parts]))
    return df.loc[idx_train].reset_index(drop=True), df.loc[idx_test].reset_index(drop=True)


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()[:16]


def main() -> None:
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument(
        "--out",
        default="_sortie",
        help="dossier de sortie (ignoré par git, à publier en asset de release)",
    )
    args = parseur.parse_args()

    dossier = Path(args.out)
    dossier.mkdir(parents=True, exist_ok=True)

    df = telecharger()

    brut = construire_brut(df)
    modelisation = construire_modelisation(brut)
    train, test = decouper(modelisation)

    fichiers = {
        "airbnb_bruxelles_raw.csv": brut,
        "airbnb_bruxelles_train.csv": train,
        "airbnb_bruxelles_test.csv": test,
    }
    for nom, table in fichiers.items():
        chemin = dossier / nom
        table.to_csv(chemin, index=False)
        taille = chemin.stat().st_size / 1_000_000
        print(f"  {nom:32s} {table.shape[0]:5d} x {table.shape[1]:2d}  "
              f"{taille:5.2f} Mo  sha256:{empreinte(chemin)}")

    print(f"\nÉcrit dans {dossier.resolve()}")
    print("Publier ces fichiers en asset de release GitHub, pas dans l'arbre git.")


if __name__ == "__main__":
    main()
