vocal=['a','e','i','o','u']
def es_vocal(a):
    if a in vocal:
        print('True')
    elif a not in vocal:
        print('False')
a = input('Di una letra: ')
es_vocal(a)