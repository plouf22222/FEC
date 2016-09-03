# -*- coding: utf-8 -*-
from datetime import datetime
import tkinter.filedialog
import os

fichier = tkinter.filedialog.askopenfilename(title="Selectionner le fichier CSV")
separateur='|'  # '\t' '|' ';'
liste_cpt = dict()
nb = 0
f_in=open(fichier)
header = f_in.readline().strip('\n')
for line in f_in:
    nb += 1
    if nb % 100000 == 0:
        print(nb)
    ligne = line.strip('\n').split(separateur)
    if ligne[4] in liste_cpt:
        liste_cpt[ligne[4]] += 1
    else:
        liste_cpt[ligne[4]] = 1
        
f_out = open("liste_cpt.csv", 'w')
f_out.write("num CPT;nb\n")
for key in sorted(liste_cpt):
    f_out.write(str(key)+";"+str(liste_cpt[key])+"\n")
    
            