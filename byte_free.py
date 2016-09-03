# -*- coding: utf-8 -*-
'''
Created on 3 sept. 2016

@author: Plouf
'''

import tkinter.filedialog
import os


def charge_fichier():
    file_opt = options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
    options['initialdir'] = os.getcwd()
    options['initialfile'] = 'myfile.txt'
    options['title'] = 'Give me a fucking File Bro'
    # get filename
    filename = tkinter.filedialog.askopenfilename(**file_opt)
    return(filename)

liste_ascii = list()
for i in range (32,255):
    liste_ascii.append(i)

# non printable car
liste_ascii.remove(173)
liste_ascii.remove(160)
liste_ascii.remove(157)
liste_ascii.remove(144)
liste_ascii.remove(143)
liste_ascii.remove(141)
liste_ascii.remove(129)
'''
print(liste_ascii)
f_out = open("test.txt", 'wb')
f_out.write(b'CACA\x00\x10\x13\n\x08\x90CACA\xE9\xF8')
f_out.close()
'''
mon_fichier = charge_fichier()
f_in = open(mon_fichier, 'rb')
f_out = open(mon_fichier+".byte", 'w', encoding="latin-1")
for ligne in f_in:
    for c in ligne:
        if c in liste_ascii:
            # f_out.write((c).to_bytes(1, byteorder='big'))
            f_out.write(chr(c))
    f_out.write('\n')
f_in.close()
f_out.close()
