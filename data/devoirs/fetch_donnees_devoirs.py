# -*- coding: utf-8 -*-
"""
Prépare les trois jeux de données des devoirs.

Ce script n'est PAS exécuté par les étudiants. Il documente la provenance des
données et régénère les fichiers publiés en asset de release GitHub. Les
fichiers produits ne sont jamais commités : voir ../README.md.

Sources, toutes issues du UCI Machine Learning Repository :

  D1  Online Retail II          https://archive.ics.uci.edu/dataset/502
  D2  Bank Marketing            https://archive.ics.uci.edu/dataset/222
  D3  Default of Credit Card    https://archive.ics.uci.edu/dataset/350

Le nettoyage appliqué ici est volontairement MINIMAL. Nettoyer les données fait
partie du travail demandé aux étudiants : livrer un fichier propre viderait les
devoirs de leur substance. On se contente de convertir les formats propriétaires
(xlsx, xls, zip imbriqués) en CSV lisibles partout.

Usage :
    python fetch_donnees_devoirs.py [--out DOSSIER]
"""

from __future__ import annotations

import argparse
import hashlib
import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

UCI = "https://archive.ics.uci.edu/static/public"

SOURCES = {
    "retail": f"{UCI}/502/online+retail+ii.zip",
    "bank": f"{UCI}/222/bank+marketing.zip",
    "credit": f"{UCI}/350/default+of+credit+card+clients.zip",
}


def _telecharger(url: str) -> bytes:
    print(f"  téléchargement de {url}")
    with urllib.request.urlopen(url, timeout=300) as reponse:
        return reponse.read()


def preparer_retail() -> pd.DataFrame:
    """Devoir 1 : transactions e-commerce britanniques, 2010-2011.

    Le fichier source contient deux feuilles annuelles. On garde la seconde,
    qui est le jeu « Online Retail » classique. Rien n'est nettoyé : les
    identifiants clients manquants, les retours en quantité négative, les
    factures d'annulation et les doublons exacts sont la matière du devoir.
    """
    archive = zipfile.ZipFile(io.BytesIO(_telecharger(SOURCES["retail"])))
    with archive.open("online_retail_II.xlsx") as fichier:
        df = pd.read_excel(fichier, sheet_name="Year 2010-2011")
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    return df


def preparer_bank() -> pd.DataFrame:
    """Devoir 2 : campagne de télémarketing bancaire, classification déséquilibrée.

    On utilise la version « bank-additional-full », la plus riche (41 188 appels,
    20 variables explicatives). La cible `y` vaut yes / no et n'est pas encodée :
    l'encoder fait partie du devoir.
    """
    archive = zipfile.ZipFile(io.BytesIO(_telecharger(SOURCES["bank"])))
    interne = zipfile.ZipFile(io.BytesIO(archive.read("bank-additional.zip")))
    with interne.open("bank-additional/bank-additional-full.csv") as fichier:
        df = pd.read_csv(fichier, sep=";")
    return df


def preparer_credit() -> pd.DataFrame:
    """Devoir 3 : comportement de paiement de 30 000 porteurs de carte, Taïwan.

    La colonne `default_next_month` est conservée mais ne doit PAS servir au
    clustering : elle sert uniquement à interpréter les segments trouvés. Le
    devoir 3 est un exercice non supervisé.
    """
    archive = zipfile.ZipFile(io.BytesIO(_telecharger(SOURCES["credit"])))
    nom = "default of credit card clients.xls"
    with archive.open(nom) as fichier:
        df = pd.read_excel(fichier, header=1)
    df = df.rename(columns={"default payment next month": "default_next_month",
                            "PAY_0": "PAY_1"})
    return df


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()[:16]


def main() -> None:
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("--out", default="_sortie",
                         help="dossier de sortie, ignoré par git")
    args = parseur.parse_args()

    dossier = Path(args.out)
    dossier.mkdir(parents=True, exist_ok=True)

    travaux = [
        ("devoir1_online_retail.csv", preparer_retail),
        ("devoir2_bank_marketing.csv", preparer_bank),
        ("devoir3_credit_default.csv", preparer_credit),
    ]

    for nom, preparer in travaux:
        print(f"\n{nom}")
        table = preparer()
        chemin = dossier / nom
        table.to_csv(chemin, index=False)
        taille = chemin.stat().st_size / 1_000_000
        print(f"  {table.shape[0]:6d} x {table.shape[1]:2d}  {taille:6.2f} Mo  "
              f"sha256:{empreinte(chemin)}")

    print(f"\nÉcrit dans {dossier.resolve()}")
    print("Publier ces fichiers en asset de release GitHub, pas dans l'arbre git.")


if __name__ == "__main__":
    main()
