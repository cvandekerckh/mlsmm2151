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

DEVOIR = 2


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


def _variante(graine: int) -> dict:
    """Sous-échantillon et coût relatif des erreurs.

    `cout_faux_negatif` est le coût d'un client qui aurait souscrit et qu'on
    n'a pas appelé, rapporté au coût d'un appel inutile (fixé à 1). Il sert à
    choisir le seuil de décision, à la partie 5.
    """
    couts = [3, 4, 5, 6, 8, 10]
    return {
        "devoir": 2,
        "fraction_echantillon": round(0.70 + (graine % 21) / 100, 2),
        "graine_echantillon": graine % 10_000,
        "cout_faux_negatif": couts[graine % len(couts)],
        "cout_faux_positif": 1,
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
