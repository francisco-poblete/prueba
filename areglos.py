

"""import random
def aleatorio(n):
    vector = [0]*n
    for i in range (n):
        vector[i]= random.randint(0,101)
    return vector
print("ingresar cuantos numeros aleatorios deseas obtener")
n = int(input())
a = aleatorio(n)
print(a)"""


NUMERO = 0
MAYOR = 0
MENOR = 0
LISTA = []


for i in range(0,5):
    numero = int(input("ingrese numero :\n"))
    LISTA.append(numero)
MAYOR = max(LISTA)
MENOR = min(LISTA)

print(f"los numeros ingresados son :{LISTA}")
print(f"el numero mayor : {MAYOR}")
print(f"el numero menor: {MENOR}")

total = 0
for i in LISTA:
    total = total + i
    print(total)
   
print(f"total: {total}")
resultado_final =[]
PROMEDIO = total/5
print(f"promedio :{PROMEDIO}")

print("----------------------")
print(f"el numero mayor es :{MAYOR}")
print(f"el numero menor es :{MENOR}")
print(f"la suma es {total}")
print(f"el promedio es {PROMEDIO}")
print("-----------------------")


"""personas = [{"nombre": "dante", "compras": [100,200,300]},{"nombre": "eduardo", "compras": [300,400,300]},{"nombre": "nn", "compras": [500,200,300]}]
for persona in personas: 
    total_persona = 0
    for compra in persona['compras']:
        total_persona = total_persona + compra
    resultado_final.append({"nombre": persona['nombre'], "total": total_persona})
print(resultado_final)"""import numpy as np

np.random.seed(0)

x = np.random.rand(5)
print(x)