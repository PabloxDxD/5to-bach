import numpy as np 

print("-----------------------------------")
print("---- OPERACIONES ARITMETICAS ------")
print("-----------------------------------")

r = input('''
            "MENU"
        1. DATO STRING, FLOAT E INT
        2. SUMA
        3. RESTA
        4. MULTIPLICACION 
        5. DIVISION 
        6. POTENCIA
        7. RAIZ CUADRADA

    Seleccione una opcion:  ''')

if r == '1':
    print("Ingrese un dato de tipo string")
    s = str(input("Dato de tipo string: "))

    print("Ingrese un dato de tipo float")
    f = float(input("Dato de tipo string: "))

    print("Ingrese un dato de tipo int")
    i = int(input("Dato de tipo string: "))

    print("Su dato de tipo string es: ", s)
    print("Su dato de tipo float es: ", f)
    print("Su dato de tipo int es: ", i)

if r == '2':
    print("Ingrese el primer termino para sumar")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("El resultado de su suma es: ", num1 + num2)

if r == '3':
    print("Ingrese el primer termino para restar")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("El resultado de su resta es: ", num1 - num2)

if r == '4':
    print("Ingrese el primer termino para multiplicar")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("El resultado de su multiplicacion es: ", num1 * num2)

if r == '5':
    print("Ingrese el primer termino para dividir")
    num1 = int(input("Primer numero: "))
    num2 = int(input("Segundo numero: "))
    print("El resultado de su division es: ", num1 / num2)

if r == '6':
    print("Ingrese el primer termino para la base de su potencia")
    num1 = int(input("Numero base: "))
    print("Ingrese el exponente que desea elevar")
    num2 = int(input("Exponente: "))
    square = num1 ** num2
    print("El resultado de su potencia es: ", square)

if r == '7':
    print("Ingrese el primer termino para sacarle su raiz")
    num1 = float(input("Primer numero: "))
    raiz = np.sqrt(num1)
    print("El resultado de su raiz cuadrada es: ", raiz) 
else:
    print("Seleccione una opcion valida")