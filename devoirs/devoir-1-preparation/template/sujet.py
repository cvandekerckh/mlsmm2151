# -*- coding: utf-8 -*-
"""
Tire la variante individuelle de ce devoir à partir de votre matricule.

Chaque étudiant reçoit un sous-échantillon et des paramètres qui lui sont
propres. Vos chiffres ne seront donc pas ceux de votre voisin, et c'est voulu.

Utilisation, au tout début de votre notebook :

    from sujet import mon_sujet
    sujet = mon_sujet("12345678")     # votre matricule UCLouvain
    print(sujet)

Ne modifiez pas ce fichier. Le correcteur utilise le même pour vérifier que
vous avez bien travaillé sur votre propre variante.
"""

from __future__ import annotations

import hashlib

DEVOIR = 1


def _graine(matricule: str) -> int:
    """Transforme un matricule en graine reproductible.

    On passe par sha256 plutôt que par `hash()`, qui varie d'une exécution à
    l'autre en Python et ne serait donc pas reproductible.
    """
    matricule = str(matricule).strip()
    if not matricule or not matricule.isdigit():
        raise ValueError(
            f"Matricule invalide : {matricule!r}. "
            "Attendu : votre numéro UCLouvain, uniquement des chiffres."
        )
    empreinte = hashlib.sha256(f"mlsmm2151-d{DEVOIR}-{matricule}".encode()).hexdigest()
    return int(empreinte[:12], 16)


# Fenêtres d'analyse possibles : six trimestres glissants de l'année 2011.
FENETRES = [
    ("2011-01-01", "2011-04-30"),
    ("2011-02-01", "2011-05-31"),
    ("2011-03-01", "2011-06-30"),
    ("2011-04-01", "2011-07-31"),
    ("2011-05-01", "2011-08-31"),
    ("2011-06-01", "2011-09-30"),
]

# Marchés de référence, tous suffisamment fournis pour être analysables.
PAYS = ["United Kingdom", "Germany", "France", "EIRE", "Netherlands", "Belgium"]


def _variante(graine: int) -> dict:
    debut, fin = FENETRES[graine % len(FENETRES)]
    return {
        "devoir": 1,
        "periode_debut": debut,
        "periode_fin": fin,
        "pays_reference": PAYS[(graine // 7) % len(PAYS)],
    }


def mon_sujet(matricule: str) -> dict:
    """Renvoie les paramètres de VOTRE variante de ce devoir."""
    graine = _graine(matricule)
    sujet = _variante(graine)
    sujet["matricule"] = str(matricule).strip()
    sujet["graine"] = graine % 10_000
    return sujet


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage : python sujet.py VOTRE_MATRICULE")
        raise SystemExit(1)
    for cle, valeur in mon_sujet(sys.argv[1]).items():
        print(f"{cle:24} {valeur}")
