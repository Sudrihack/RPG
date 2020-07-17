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
    return lignes
            
def recuperer_points(actions):
    points = {}
    for action, categorie, points_action in actions:
        points[action] = int(points_action)
    return points

def creer_fichier_scores(scores_tries):
    with open('scores.csv', 'w') as f:
        for nom, score in scores_tries:
            f.write(f'{nom},{score}\n')

def dictionnaire(lignes):
    res = {}
    for action, categorie, points in lignes:
        res[action] = [categorie, points] # la premiere colonne fait office de clef primaire
    return res
        
def recuperer_profil(nom, actions, faits):
    profil = {}
    actions = dictionnaire(actions)

    for date, nom_etudiant, action in faits:
        if action in actions:
            categorie, points_action = actions[action]
        else:
            print(f'L\'action "{action}" n\'existe pas.')
        if nom_etudiant == nom:
            if not categorie in profil:
                profil[categorie] = int(points_action)
            else:
                profil[categorie] += int(points_action)
    return profil
        
if __name__ == '__main__':
    actions = recuperer_lignes('actions.csv') # magick str
    faits = recuperer_lignes('table_faits.csv')

    points = recuperer_points(actions)
    print(points)
    
    scores = {}

    for date, nom, action in faits:
        if action in points:
            pts = points[action]
            print(f'Ajout de {pts} points pour {nom}.')
            if nom in scores:
                scores[nom] += pts
            else:
                scores[nom] = pts
        else:
            print(f'L\'action "{action}" n\'existe pas.')

    # trier le dictionnaire par valeurs
    scores_tries = sorted(scores.items(), key=lambda x:x[1], reverse=True)

    print(*scores_tries, sep='\n')

    creer_fichier_scores(scores_tries)

    # tests pour la fonction recuperer_profil
    print(recuperer_profil('demol', actions, faits))
    print(recuperer_profil('reiffers', actions, faits))
