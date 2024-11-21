def max_de_tres(a,b,c):
    if a>b and a>c:
        print('a')
    elif b>c and b>a:
        print(b)
    else:
        print(c)
a = int(input('Di el primer número: '))
b = int(input('Di el segundo número: '))
c = int(input('Di el tercer número: '))
max_de_tres(a,b,c)