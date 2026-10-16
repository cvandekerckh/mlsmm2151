"""
Chargement des jeux de données du cours MLSMM2151.

Ce fichier est du CODE, il est donc versionné dans le dépôt.
Les DONNÉES, elles, n'y sont pas : voir data/README.md.

Utilisation dans un notebook, y compris dans Google Colab :

    !wget -q -O donnees.py https://raw.githubusercontent.com/cvandekerckh/mlsmm2151/main/utils/donnees.py
    from donnees import charger

    df = charger("airbnb_raw")

`charger` cherche le fichier dans cet ordre :

    1. le cache de la session (rapide, mais perdu à la fermeture de Colab) ;
    2. votre Google Drive, s'il est monté (survit à la fermeture) ;
    3. la release GitHub du cours (téléchargement).

Autrement dit : le premier appel prend quelques secondes, les suivants sont
instantanés, et rien n'est jamais écrit dans un dépôt git.
"""

from __future__ import annotations

import os
import shutil
import urllib.request
from pathlib import Path

import pandas as pd

__all__ = ["charger", "chemin_drive", "RELEASE"]

# Adresse des fichiers publiés. La variable d'environnement MLSMM2151_RELEASE
# permet de pointer ailleurs (une release préliminaire, un dossier local) sans
# toucher aux notebooks. Elle sert à l'enseignant, pas aux étudiants.
RELEASE = os.environ.get(
    "MLSMM2151_RELEASE",
    "https://github.com/cvandekerckh/mlsmm2151/releases/download/v1-donnees",
)

# Nom court utilisé dans les notebooks -> nom du fichier dans la release.
SOURCES = {
    # Fil rouge du cours
    "airbnb_raw": "airbnb_bruxelles_raw.csv",
    "airbnb_train": "airbnb_bruxelles_train.csv",
    "airbnb_test": "airbnb_bruxelles_test.csv",
    # Devoirs
    "devoir1": "devoir1_online_retail.csv",
    "devoir2": "devoir2_bank_marketing.csv",
    "devoir3": "devoir3_credit_default.csv",
}

DESCRIPTIONS = {
    "airbnb_raw": "Airbnb Bruxelles, données brutes (chapitres 0 à 4)",
    "airbnb_train": "Airbnb Bruxelles, table de modélisation, 80 % (chapitres 5 à 12)",
    "airbnb_test": "Airbnb Bruxelles, table de modélisation, 20 % (chapitres 5 à 12)",
    "devoir1": "Devoir 1 : Online Retail II, transactions e-commerce",
    "devoir2": "Devoir 2 : Bank Marketing, classification déséquilibrée",
    "devoir3": "Devoir 3 : Default of Credit Card Clients, segmentation",
}

CACHE_SESSION = Path("/content/donnees_mlsmm2151") if Path("/content").exists() else Path(".donnees_mlsmm2151")
DOSSIER_DRIVE = "MLSMM2151/data"


def chemin_drive() -> Path | None:
    """Renvoie le dossier de cache dans le Google Drive, s'il est monté.

    Ne monte rien tout seul : si vous voulez que vos données survivent à la
    fermeture de Colab, montez le Drive avant d'appeler `charger` :

        from google.colab import drive
        drive.mount('/content/drive')
    """
    racine = Path("/content/drive/MyDrive")
    if not racine.exists():
        return None
    dossier = racine / DOSSIER_DRIVE
    try:
        dossier.mkdir(parents=True, exist_ok=True)
    except OSError:
        return None
    return dossier


def _telecharger(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not url.startswith(("http://", "https://")):
        # RELEASE pointe vers un dossier local (voir MLSMM2151_RELEASE).
        shutil.copyfile(url, destination)
        return
    temporaire = destination.with_suffix(destination.suffix + ".partiel")
    try:
        with urllib.request.urlopen(url, timeout=120) as reponse, open(temporaire, "wb") as sortie:
            shutil.copyfileobj(reponse, sortie)
    except Exception as erreur:  # noqa: BLE001
        temporaire.unlink(missing_ok=True)
        raise RuntimeError(
            f"Impossible de telecharger {url}\n"
            f"  Cause : {erreur}\n"
            f"  Vérifiez votre connexion, ou signalez le problème si l'adresse est morte."
        ) from erreur
    # Écriture atomique : pas de fichier à moitié téléchargé dans le cache.
    os.replace(temporaire, destination)


def _localiser(nom_fichier: str, verbeux: bool) -> Path:
    """Renvoie un chemin local vers le fichier, en le téléchargeant si besoin."""
    cache_session = CACHE_SESSION / nom_fichier
    if cache_session.exists():
        return cache_session

    drive = chemin_drive()
    if drive is not None and (drive / nom_fichier).exists():
        if verbeux:
            print(f"Lu depuis votre Google Drive : {DOSSIER_DRIVE}/{nom_fichier}")
        return drive / nom_fichier

    url = f"{RELEASE}/{nom_fichier}"
    if verbeux:
        print(f"Téléchargement de {nom_fichier}...")
    _telecharger(url, cache_session)

    # Si le Drive est monté, on y dépose une copie pour la prochaine session.
    if drive is not None:
        try:
            shutil.copyfile(cache_session, drive / nom_fichier)
            if verbeux:
                print(f"Copie dans votre Drive : {DOSSIER_DRIVE}/{nom_fichier}")
        except OSError:
            pass  # Drive plein ou en lecture seule : le cache session suffit.

    return cache_session


def charger(nom: str, verbeux: bool = True, **kwargs) -> pd.DataFrame:
    """Charge un jeu de données du cours dans un DataFrame pandas.

    Paramètres
    ----------
    nom : le nom court du jeu de données. `charger.disponibles()` les liste.
    verbeux : afficher ce qui se passe (téléchargement, cache utilisé).
    **kwargs : passés tels quels à `pandas.read_csv`.
    """
    if nom not in SOURCES:
        connus = ", ".join(sorted(SOURCES))
        raise KeyError(f"Jeu de données inconnu : {nom!r}. Disponibles : {connus}")

    chemin = _localiser(SOURCES[nom], verbeux)
    df = pd.read_csv(chemin, low_memory=False, **kwargs)
    if verbeux:
        print(f"{nom} : {df.shape[0]} lignes x {df.shape[1]} colonnes")
    return df


def _disponibles() -> pd.DataFrame:
    """Liste les jeux de données du cours."""
    return pd.DataFrame(
        [{"nom": n, "fichier": SOURCES[n], "description": DESCRIPTIONS[n]} for n in SOURCES]
    )


charger.disponibles = _disponibles  # type: ignore[attr-defined]
