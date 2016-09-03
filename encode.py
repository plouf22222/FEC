# -*- coding: utf-8 -*-
'''
Created on 28 oct. 2015

@author: bfayolle
'''
import codecs
import os
import tkinter.filedialog
import csv


def travaille_sur_copy(mon_fichier):
    ma_comande = "copy "+mon_fichier+" d:\data.txt"
    os.system(ma_comande)
    print("OK copy faite, on va pouvoir travailler sereinement")


def charge_fichier():
    file_opt = options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = 'D:\\'
    options['initialfile'] = 'myfile.txt'
    options['title'] = 'Give me a fucking File Bro'
    # get filename
    filename = tkinter.filedialog.askopenfilename(**file_opt)
    return(filename)


def detecte_encoding(fichier):
    encodings = ['utf-32', 'utf-16', 'utf-8', 'latin1', 'windows-1250',
                 'windows-1252']
    for e in encodings:
        try:
            f_in = codecs.open(mon_fichier, 'r', encoding=e, errors='strict')
            f_in.read(10000000)
            f_in.seek(0)
        except UnicodeDecodeError:
            print('got unicode error with %s , trying different encoding' % e)
        except UnicodeError:
            print('got unicode error with %s , trying different encoding' % e)
        else:
            print('opening the file with encoding:  %s ' % e)
            break
    return(e, f_in)


def teste_null(f_in, mon_dialect, mon_encodage):
    data = csv.reader(f_in, dialect=mon_dialect)
    try:
        for ligne in data:
            if data.line_num > 1000:
                break
    except:
        print("NULL type Error : travail sur une copy Unicode")
        travaille_sur_copy(mon_fichier.replace("/", "\\"))
        f_in.close()
        f_in = codecs.open("d:/data.txt", 'r', encoding=mon_encodage,
                           errors='ignore')
    f_in.seek(0)
    return(f_in)


def quel_dialecte(f_in):
    sample = f_in.read(1000000)
    dialect = csv.Sniffer().sniff(sample)
    isheader = csv.Sniffer.has_header(csv.Sniffer(), sample)
    sample = ""
    f_in.seek(0)
    return(dialect, isheader)

csv.field_size_limit(500 * 1024 * 1024)
mon_fichier = charge_fichier()
mon_encodage, f_in = detecte_encoding(mon_fichier)
# detection Null type
mon_dialect, isheader = quel_dialecte(f_in)
f_in = teste_null(f_in, mon_dialect, mon_encodage)
data = csv.reader(f_in, mon_dialect)
# data=csv.reader(f_in, delimiter=separateur)
if isheader:
    header = next(data)
print(header)
print("delimiter = " + mon_dialect.delimiter)

# *********************************
# traitement à faire
# *********************************
liste = dict()
# debit / credit
for ligne in data:
    if data.line_num % 1000000 == 0:
        print(data.line_num)
    a = len(ligne)
    if a in liste:
        liste[a] += 1
    else:
        liste[a] = 1
print("Nombre de ligne total : "+str(data.line_num))
'''with open(mon_fichier + "_result", "w") as csvfile:
    out = csv.writer(csvfile, delimiter=';', lineterminator='\n')
    for key in liste:
        out.writerow([str(key), str(liste[key])])
'''
for key in liste:
    print("Nombre de ligne de " + str(key) + " champs = " + str(liste[key]))