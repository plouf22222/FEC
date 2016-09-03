# -*- coding: utf-8 -*-
'''
Created on 7 nov. 2014

@author: bfayolle
'''
from datetime import datetime

import tkinter.filedialog
import os


#changement de repertoire de travail
#os.chdir("")
#r?cup?re le chemin d'acc?s au fichier via l'ihm TK
fichier = tkinter.filedialog.askopenfilename(title="Selectionner le fichier CSV")
#fichier = "D:/FEC/775691140FEC20131231.txt"
separateur='|'  # '\t' '|' ';'
'''if os.path.isdir(fichier):
    print "OK!"
    exit()
else:
    print "catastrophe"
    exit()
   ''' 
	

    
def veriffichier():
    
    f_in=open(fichier)
    champ_par_ligne = dict()
    derniere_par_champ = dict()
    nbligne=0
    for ligne in f_in:
        nbligne+=1
        if nbligne % 100000 == 0:
            print(nbligne)
        nbsep = ligne.count(separateur)
        if nbsep in champ_par_ligne:
            champ_par_ligne[nbsep]+=1
        else:
            champ_par_ligne[nbsep] = 1
        if nbsep in derniere_par_champ:
            derniere_par_champ[nbsep]=nbligne
        else:
            derniere_par_champ[nbsep]=nbligne
        
    print("nombre de ligne du fichier : " + str(nbligne))
    nblignediff=0
    for key in champ_par_ligne:
        nblignediff+=1
        print("Nombre de ligne de " + str(key) + " champs = " + str(champ_par_ligne[key]) + " derniere ligne " + str(derniere_par_champ[key]))
    f_in.close()
    if not (nblignediff == 1):
        print("==> Fichier impropre : des champs en trop/manquant sur des lignes")
        return False
    return True

def ma_cle(un_fichier):
    return str(hash(str(os.path.getctime(un_fichier))+str(os.path.getmtime(un_fichier))+str(os.path.getsize(un_fichier))))

def fin_traitement():
    print("==> Fin du Traitement")
    time2 = datetime.now()
    tim_diff = time2 - time1
    print("Temps ecoule: " + str(tim_diff.seconds))
    exit()

def test_valid():
    if (os.path.isfile(fichier)):
        if os.path.isfile(fichier+".valid"):
            f_verif_cle=open(fichier+".valid","rb")
            test = f_verif_cle.read()
            f_verif_cle.close()
            if test==ma_cle(fichier):
                return True
        return False
    else:
        print("==> Erreur de fichier en entré : " + fichier)
        print("==> Traitement ABORT")
        fin_traitement()
        
def debut_traitement():
    print("==> Début traitement")
    if not(test_valid()):
        if not(veriffichier()):
            print("==> Traitement ABORT")
            fin_traitement()



if __name__ == '__main__':
    time1 = datetime.now()
    #choppeligne(8942498)
    debut_traitement()
    #traitement()
    fin_traitement()
    #main()
