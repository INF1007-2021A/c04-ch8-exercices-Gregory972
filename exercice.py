#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def compare(fichier1, fichier2):
    f1 = open(fichier1, "r", encoding="utf-8")
    f2 = open(fichier2, "r", encoding="utf-8")
    for lettre1, lettre2 in f1, f2:
        if lettre1 != lettre2:

            return 'Les fichiers sont différents à partir de :', (lettre1, lettre2)
    return 'Les fichiers sont identiques'



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
