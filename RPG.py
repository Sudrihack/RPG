# coding: utf-8

with open('actions.csv') as f:
    ligne = f.readline()
    while ligne:
        print(ligne, end='')
        if not valider_colonnes(ligne):
            print("Problème avec le nombre de colonnes.")
        ligne = f.readline()
        
def valider_colonnes(ligne):
    colonnes = ligne.split(',')
    return colonnes == 3 # magick number
