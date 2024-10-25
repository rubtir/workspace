#programa que decideix si un nombre és prim o no i que calcule un nombre de primers consecutius
t=int(input('Indica el número de casos que cal processar'))
for i in range(0,t):
    k = int(input('Introdueix un nombre entre 0 i 100:'))
    n = int(input('Introdueix un nombre sencer entre 1 i 10000 i et diré si es primer o no'))
    if k ==0:
        if (n % 2 != 0):
            print ('Si')
        else:
            print('No')