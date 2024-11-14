with open('Ficheros/temperaturas.dat') as f:
    for linea in f:
        min_temp, max_temp = linea.strip().split()
        print(min_temp, max_temp)