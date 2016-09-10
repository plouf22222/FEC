import os

header = dict()

L = [os.path.join(os.getcwd(),f) for f in os.listdir('.') if os.path.isfile(os.path.join(os.getcwd(),f))]
for fichier in L:
    if fichier[-3:] != 'txt':
        f_in=open(fichier, 'r')
        data = f_in.readline()
        if data in header:
            header[data][0] += 1
            header[data].append(fichier)
        else:
            header[data] = [1]
            header[data].append(fichier)
        f_in.close()
f_out = open("headers.csv",'w')
for key in header:
    f_out.write(header[key])
    f_out.write(key)

