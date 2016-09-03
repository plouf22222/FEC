import os

header = dict()

# L = [os.path.join(os.getcwd(),f) for f in os.listdir('.') if os.path.isfile(os.path.join(os.getcwd(),f))]
L = [ "test.txt.byte"]
for fichier in L:
    if fichier[-3:] != '.py':
        f_in=open(fichier, 'r')
        data = f_in.readline()
        if data in header:
            header[data] += 1
        else:
            header[data] = 1
        f_in.close()

for key in header:
    print(header[key], " Header => ", key)

