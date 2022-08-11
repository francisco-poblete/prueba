"""x = range(5)
for n in x:
    print(n)"""

"""x = range(1,10,2)
for n in x:
    print(n)"""

"""frase = "hola mundo"
for caracter in frase:
    print(caracter)"""


"""for n in range(1,11):
    print(f'Tabla del: {n}')
    for i in range(1,11):
        print(f"{n} x {i} = {i*n}")"""



"""def num_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
      for i in range(2,numero):
        if numero  % i == 0 :   
         return False      
    return True  
for i in range (2, 100):
  print(i, num_primo(i))"""

"""numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
 
if contador > 0 :
  print("El número no es primo" )
else:
  print("El nÚmero es primo")"""

"""numero = int(input("ingrese un numero :"))
suma = 0
for n in suma:
    if numero % n == 0:
        suma += 1
    print("divisor:",n)"""
    

"""def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False
 
num = int(input("ingrese un numero:"))
 
if NumeroPerfecto(num):
  print("%s es un numero perfecto" % num)
else:
  print("%s NO es un numero perfecto" % num)"""
