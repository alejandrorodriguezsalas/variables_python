#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.3
Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    print('''        PRIMER número: {}
        SEGUNDO número: {}'''.format(numero_1,numero_2))


    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma = numero_1 + numero_2
    print("SUMA: {} + {} = {}".format(numero_1,numero_2,suma))

    # Resta
    resta = numero_1 + numero_2
    print("RESTA: {} - {} = {}".format(numero_1,numero_2,resta))

    # División
    div = numero_1 / numero_2
    print("DIVISION: {} / {} = {}".format(numero_1,numero_2,div))

    # Multiplicación
    mult = numero_1 * numero_2
    print("MULTIPLICACION: {} x {} = {}".format(numero_1,numero_2,mult))


def ej2():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo

    print("su nombre completo es: {} {}".format(nombre,apellido))

    # Almacenar su nombre completo en una variable
    nombre_completo = nombre + apellido

    # Imprimir la cantidad de letras que posee su nombre completo

    print("La cantidad de letras que posee su nombre es: {}".format(len(nombre_completo)) )

def ej3():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla
    print('''ACRONIMO:
            {}, {}, {} --> {}'''.format(palabra_1,palabra_2,palabra_3,palabra_1[0]+palabra_2[0]+palabra_3[0]))


def ej4():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados

    subpalabra_1 = palabra_1[:3]
    subpalabra_2 = palabra_2[len(palabra_2)-3:]

    nueva_palabra = subpalabra_1 + subpalabra_2

    print('''Recorte de la primera palabra: {}
Recorte de la segunda palabra: {}

    Combinación de ambos recortes:  {}'''.format(subpalabra_1,subpalabra_2,nueva_palabra))


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
