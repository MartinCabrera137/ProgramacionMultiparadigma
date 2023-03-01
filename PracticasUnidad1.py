##1 Funciones con n parámetros

def funcion(a,b):
    total = (a+b)
    return total
print("Total= ", funcion(10,10))


#2 Manejo y manipulación de elementos de una lista

#lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#print(lista)

def funcion():

    abc= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    abc_final = []
    for i in range(len(abc)):
        if i%3!=0:
            abc_final += abc[i]

    print(abc_final)

funcion()

#3 Entrada de datos y manipulación. 

nombre = input("¿Cómo te llamas? ")

nombre_invertido = ''.join(reversed(nombre))

for indice in range(len(nombre)):
    caracter = nombre_invertido[indice]
    print(caracter)

#4 Entrada de datos y estructuración.
Ciclo = int(input("Cuantas materias ingresaras: "))


#print("Tipo de dato: ",type(Credito3))

curso = {}
total_creditos = 0


for i in range(Ciclo):
    Materia = input("Escribe la materia: ")
    Credito3 = int(input("Escribe el credito6: "))
    curso[Materia] = Credito3

for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total_creditos += creditos
print('Número total de créditos del curso: ', total_creditos)

#5 Manejo de información

def funcion(**valores):
    print(valores)
funcion(Nombre="Luis", Apellido="Zapata", 
        Telefono=6500, ID=17)



#6 Razonamiento y prueba de código

def dfuncion(valor):
    Diccionario = {'1': "Uno", '2': "Dos", '3': "Tres", '4': "Cuatro", '5': "Cinco",
    '6': "Seis", '7': "Siete", '8': "Ocho", '9': "Nueve", '10': "Diez", '11':
    "Once", '12': "Doce", '13': "Trece", '14': "Catorce", '15': "Quince", '16':
    "Dieciseis", '17': "Diecisiete", '18': "Dieciocho", '19': "Diecinueve",
    '20': "Veinte", '0': "Cero"}
    print(Diccionario.get(str(valor)))
dfuncion(input("Teclee un numero del 0 al 20: "))

#7 Formateo y conversiones
import os
from datetime import date
from datetime import datetime

while True:
    print(f"SELECCIONE FORMATO DE LA FECHA A IMPRIMIR\n\
Presiona 1 para YYYY/MM/DD.\n\
Presiona 2 para MM/DD/YYYY.\n\
Presiona 3 para salir.")
    opcion=input()
    if opcion=='1':
        now = datetime.now()
        format = now.strftime('%Y/%m/%d')
        print(format)
    elif opcion=='2':
        now = datetime.now()
        format = now.strftime('%m/%d/%Y')
        print(format)
    elif opcion=='3':
        break
    input()
    os.system("cls")