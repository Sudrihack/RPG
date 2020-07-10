# coding: utf-8

def valider_colonnes(ligne):
    return len(ligne) == 3 # magick number

def recuperer_lignes(fichier):
    lignes = []
    with open(fichier) as f:
        ligne = f.readline()
        while ligne:
            ligne = ligne[:-1].split(',') # faire quelque chose (dernier char = \n); magick char
            print(ligne)
            if valider_colonnes(ligne):
                lignes.append(ligne)
            else:
                print("  Probleme avec le nombre de colonnes.")
            ligne = f.readline()

if __name__ == '__main__':
    actions = recuperer_lignes('actions.csv') # magick str
    faits = recuperer_lignes('table_faits.csv')
        
