# Jeu de mastermind en ligne de commande
from random import randrange  # Importation de la fonction randrange du module random


def choisir_couleurs(couleurs_possibles):
    "Choisir 5 couleurs à partir d'une liste de couleurs possibles"
    couleurs_choisies = []  # Liste dans laquelle on stockera toutes les couleurs choisies
    i = 0
    while i < 5:
        # Choisir une couleur au hasard
        couleur = randrange(len(couleurs_possibles))
        couleur = couleurs_possibles[couleur]
        couleurs_choisies.append(couleur)
        i += 1

    return couleurs_choisies


def comparer_couleurs(liste1, liste2):
    "Comparer les couleurs contenues dans 2 listes différentes. Cela va nous servir pour comparer les couleurs entrée par le joueur et les couleurs choisies."
    # Liste dans laquelle on stockera des booléens qui seront True si une couleur est commune aux deux listes, et False si une couleur n'est pas commune aux deux listes.
    couleurs_communes = []
    est_commune = False  # Est-ce qu'une couleur est commune aux deux listes ?

    for couleur in liste1:  # Pour chaque couleur de la première liste
        if couleur in liste2:  # Si la couleur est également présente dans la deuxième liste
            est_commune = True  # Alors la couleur est commune aux deux listes
            couleurs_communes.append(est_commune)

        else:
            est_commune = False  # La couleur n'est pas commune aux deux listes
            couleurs_communes.append(est_commune)

        est_commune = False  # Réinitialiser la variable est_commune

    return couleurs_communes


liste1 = ["bleu", "rouge", "vert", "blanc", "violet"]
liste2 = ["orange", "noir", "bleu", "vert", "marron"]

print(comparer_couleurs(liste1, liste2))
