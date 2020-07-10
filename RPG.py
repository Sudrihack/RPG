# coding: utf-8

with open('actions.csv') as f:
    ligne = f.readline()
    while ligne:
        print(ligne, end='')
        ligne = f.readline()
        
