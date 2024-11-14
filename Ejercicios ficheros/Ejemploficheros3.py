f = open('Ficheros/aeropuertos.dat', 'a')
canary_iata = ('VLC', 'CDT', 'ORL')
for code in canary_iata:
    f.write(code + '\n')
f.close()