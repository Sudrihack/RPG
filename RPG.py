# coding: utf-8

def valider_colonnes(ligne):
    colonnes = ligne.split(',')
    return len(colonnes) == 3 # magick number

with open('actions.csv') as f:
    ligne = f.readline()
    while ligne:
        print(ligne[:-1]) # faire quelque chose (dernier char = \n)
        if not valider_colonnes(ligne):
            print("Probleme avec le nombre de colonnes.")
        ligne = f.readline()
        
