

"""igualACero = 0
mayoACero = 0
menorACero = 0
for i in range(0,5):
    number = int(input("Ingresa numero :"))
    if number == 0:
        igualACero = igualACero + 1
    elif number > 0: 
        mayoACero = mayoACero + 1
    elif number< 0:
        menorACero =menorACero + 1
    
print('Resultado')
print(f'Cantidad de numeros igual a cero : {igualACero}')
print(f'Cantidad de numeros Mayor a Cero : {mayoACero}')
print(f'Numeros menores a cero : {menorACero}')"""
vocales = 0
consonante = 0
for i in range(0,10):
    letra = input("Escribe una letra: ")
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        vocales = vocales + 1
    else:
        consonante = consonante +1
print(f'Consonantes {consonante}, Vocales {vocales} ')
