# -*- coding: utf-8 -*-
from datetime import datetime
import tkinter.filedialog
import os

fichier = tkinter.filedialog.askopenfilename(title="Selectionner le fichier CSV")
separateur='|'  # '\t' '|' ';'
nb = 0
f_in=open(fichier)
header = f_in.readline().strip('\n')
f_out = open(fichier + ".new", 'w')
f_out.write(header+'\n')
for line in f_in:
    nb += 1
    if nb % 100000 == 0:
        print(nb)
    ligne = line.strip('\n').split(separateur)
    if ligne[11] == "+0,00":
        ligne[11] = "0,00"
    else:
        ligne[11] = ligne[11][1:]
    f_out.write('|'.join(ligne) + '\n')