def MCD(num_1,num_2):
    if num_1>num_2:
        num1=num_1
        num2=num_2
    else:
        num1=num_2
        num2=num_1
    while num1%num2 != 0:
        num2, num1 =num1%num2,num2
    print(f'El máximo común divisor es: {num2}')
num_1= int(input('Dime el primer número: '))
num_2= int(input('Dime el segundo número: '))
MCD(num_1,num_2)
