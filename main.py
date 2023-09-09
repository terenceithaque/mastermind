# Jeu de mastermind en ligne de commande
from random import randrange  # Importation de la fonction randrange du module random


def choisir_couleurs(couleurs_possibles):
    "Choisir 5 couleurs à partir d'une liste de couleurs possibles"
    couleurs_choisies = []  # Liste dans laquelle on stockera toutes les couleurs choisies
    n_couleurs_choisies = 0  # Nombre de couleurs choisies
    while n_couleurs_choisies < 5:
        # Choisir une couleur au hasard
        couleur = randrange(len(couleurs_possibles))
        couleur = couleurs_possibles[couleur]
        couleurs_choisies.append(couleur)
        n_couleurs_choisies += 1

    return couleurs_choisies


def couleurs_communes(liste1, liste2):
    "Trouver les couleurs communes de deux listes différentes"
    couleurs_com = []  # Liste dans laquelle on contiendra toute couleur commune aux deux listes
    for couleur in liste1:  # Pour chaque couleur de la première liste
        if couleur in liste2:
            couleurs_com.append(couleur)

    return couleurs_com


def comparer_positions(liste1, liste2):
    "Comparer les positions des couleurs dans deux listes différentes"
    # Trouver toutes les couleurs communes aux deux listes
    couleurs_com = couleurs_communes(liste1, liste2)
   # print("couleurs_com :", couleurs_com)
    # Booléen pour vérifier si la position d'une couleur est la même d'une liste à l'autre
    pos_identique = True
    pos = []  # Liste pour contenir les valeurs de pos_identique pour chaque couleur
    for couleur in couleurs_com:
        if couleur in liste1 and couleur in liste2:
            # print("Position liste 1 :", liste1.index(couleur),
            # "Position liste 2 :", liste2.index(couleur))

            if liste1.index(couleur) != liste2.index(couleur):
                # print("La position des couleurs est différente !")
                pos_identique = False
                pos.append(pos_identique)

            else:
                pos_identique = True
                pos.append(pos_identique)

    return pos


def jeu():
    "Jeu"
    # Liste des couleurs que le jeu peut tirer au hasard
    couleurs_possibles = ["blanc", "bleu", "vert", "noir", "blanc", "rouge"]
    couleurs_choisies = choisir_couleurs(couleurs_possibles)
    print(couleurs_choisies)
    essais = 12

    while essais > 0:
        # Demander au joueur de saisir 5 couleurs
        print()  # Sauter à la ligne
        couleurs = input("Saisissez 5 couleurs:")
        couleurs = couleurs.split()  # Représenter la saisie du joueur sous forme de liste
        # Comparer les positions des couleurs de couleurs et couleurs_choisies
        comp = comparer_positions(couleurs, couleurs_choisies)
        # Pour chaque couleur entrée par le joueur
        for i, couleur in enumerate(couleurs):
            if comp[i]:  # Si la couleur est bien placée
                print(couleur, ": O, ", end=" ")
            else:
                print(couleur, ": X, ", end=" ")

            if couleur not in couleurs_choisies:
                print(couleur)

        if couleurs != couleurs_choisies:  # Si le joueur n'a pas deviné les bonnes couleurs et/ou leur position
            essais -= 1
            print("Essais restants :", essais)

        if couleurs == couleurs_choisies:  # Si le joueur a deviné toutes les couleurs ainsi que leur position
            # Afficher un message de fin de partie
            print("Bravo ! Vous avez gagné !")
            break  # Terminer la partie

        if essais > 0:
            continue

        else:
            print()  # Sauter à la ligne
            print("GAME OVER")


jeu()
