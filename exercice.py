#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import recettes

# TODO: Définissez vos fonction ici

#Exercice 1
def compare(fichier1, fichier2):
    with open(fichier1, "r", encoding="utf-8") as f1, open(fichier2, "r", encoding="utf-8") as f2:
        for ligne1 in f1:
            ligne2 = f2.readline()
            if ligne1 != ligne2:
                print("Dans le fichier : ", fichier1)
                print(ligne1,"est différent de")
                print(ligne2, "dans la fichier : ", fichier2)

                return

        print("Les fichiers", (fichier1, fichier2), "sont identiques")


#Exercice 2
def copie(fichier, fichier_vide):
    with open(fichier, "r", encoding="utf-8") as f1, open(fichier_vide, "w", encoding="utf-8") as f2:
        for ligne in f1:
            for i in ligne:
                if i == ' ':
                    f2.write('   ')
                else:
                    f2.write(i)


#Exercice 3
def mentions(fichier, fichier_mentions):
    with open(fichier, "r", encoding="utf-8") as f1, open(fichier_mentions, "w", encoding="utf-8") as f2:
        for ligne in f1:
            verifier = False
            for i in PERCENTAGE_TO_LETTER:
                intervalle = PERCENTAGE_TO_LETTER.get(i)
                if int(ligne) >= intervalle[0] and int(ligne) <= intervalle[1] and verifier == False:
                    verifier = True
                    f2.write(i)
                    f2.write("\n")


#Exercice 4
def supprimer_recette(dictionnaire):
    nom_recette = input("Entrez le nom exact de la recette à supprimer")
    for clef in dictionnaire:
        if nom_recette == clef:
            del dictionnaire[nom_recette]
            break

def base_de_donnee(livre):
    livre_de_recette = {}
    while True:
        choix = int(input("Veuillez choisir parmis les options suivantes \n "
                          "1 : ajouter une recette \n "
                          "2 : supprimer une recette \n "
                          "3 : modifier une recette \n "
                          "4 : Afficher une recette \n "
                          "5 : Vous avez terminé \n "
                          "Votre choix : "))
        if choix == 1:
            recettes.add_recipes(livre_de_recette)
        elif choix == 2:
            supprimer_recette(livre_de_recette)
        elif choix == 3:
            recettes.add_recipes(livre_de_recette)
        elif choix == 4:
            recettes.print_recipe(livre_de_recette)
        elif choix == 5:
            break
        else:
            print("Choix incorrect")

    with open(livre, 'w', encoding="utf-8") as f:
        for i in livre_de_recette:
            f.write(str(i))
            f.write(':')
            f.write(str(livre_de_recette.get(i)))
            f.write('\n')


#Exercice 5
def liste_croissante(fichier):
    liste = []
    with open(fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            liste_ligne = ligne.split()
            for element in liste_ligne:
                if element.isdigit():
                    liste.append(int(element))

    return sorted(liste)


#Exercice 6
def recopie_une_ligne_sur_deux(fichier1, fichier2):
    Compteur = 0
    with open(fichier1, "r", encoding="utf-8") as f1, open(fichier2, "w", encoding="utf-8") as f2:
        for ligne in f1:
            if Compteur % 2 == 0:
                f2.write(ligne)
                f2.write("\n")
            Compteur += 1


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # Exercice 1
    print(compare('exemple.txt', 'notes.txt'))
    print(compare('exemple.txt', 'exemple.txt'))

    # Exercice 2
    print(copie('exemple.txt', 'fichier_vide'))

    # Exercice 3
    print(mentions('notes.txt', 'fichier_mentions'))

    # Exercice 4
    print(base_de_donnee('livre'))

    # Exercice 5
    print(liste_croissante('exemple.txt'))

    # Exercice 6
    print(recopie_une_ligne_sur_deux('notes.txt', 'fichier2'))