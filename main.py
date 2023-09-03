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


couleurs_possibles = ["bleu", "blanc", "vert", "rouge",
                      "orange", "noir"]  # Liste des couleurs possibles
print(choisir_couleurs(couleurs_possibles))
