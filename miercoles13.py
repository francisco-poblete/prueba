#ejercicio 01
from ctypes.wintypes import PINT
from re import X


"""mensaje = "bienvenido al mundo de la programacion"
print(f"{mensaje}")
print("bienvenido al mundo de la programacion")"""
#ejercicio 02

"""nom=input("ingresa tu nombre:  ")
print(f"bienvenido {nom}")"""

#ejercicio 03

""" X = int(input("ingrese valor para resolver la ecuacion (x^2 + 3x + 1)/4: "))
resultado = (X**2 + 3*X +1)/4
print(f"el resultado de la ecuacion con el numero {X} es igual a {resultado}") """

# ejercicio 04

"""nombre = input ("ingrese su nombre")
rut = int(input("ingrese su rut sin codigo de verificador"))
dv = input("ingrese codigo verificador")
correo = input ("ingrese su correo")
celular = int(input("ingrese su numero telefonico"))

print("NOMBRE: {nombre} \nRUT: {rut} \nCORREO: {correo} \ncelular: {celular}")"""

#como manejar otro tipo de dato 
"""decimal = (input("ingrese numero decimal"))
print (f"{decimal}")
print(type (decimal))"""

#sintaxis if, elif y elso
#acividad 2 ejercicio 01
"""edad = int(input("ingrese su edad"))
if edad >=18 and edad < 110 :
    print("usted es mayor de edad")
elif edad <18 and edad > 0 :
    print("usted es menor de edad ")
else:
    print("no existe edad , ingrese nuevamente ")"""
    
# ejercicio 2
"""user1="pedro"
pass1="1234"
user2= "angel"
pass2="a4s1"

user0 = input ("ingrese su nombre  de usuario")
pass0 = input ("ingrese su clave de usuario")
if user0 == user1 and pass0 == pass1:
    print("binvenido pedro")
elif user0 ==user2 and  pass0 == pass2:
    print ("binvenido angel")
else:
print("credenciales incorrectas")"""

"""nota1 = float (input("ingresw su primera nota :"))
nota2 = float (input("ingresw su primera nota :"))
nota3 = float (input("ingresw su primera nota :"))

promedio (nota1+nota2+nota3)/3
if promedio >=4.0:
print(f"felicitaciones , esta aprobado con nota de {promedio}")
else:
    print(f"lo sineto , esta reprobado con una nota de {promedio}")"""