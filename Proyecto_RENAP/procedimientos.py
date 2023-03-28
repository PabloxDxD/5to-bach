def certificado():
    print('''Los requisitos para poder registrar a su bebe son
    1. Nombre de los padres
    2. DPI de ambos padres
    3. Informe de naciemto extendido por el hospital
    4. Comprobante de pago completo
    5. Datos del bebe''')

    nombre_padre = input("Ingrese el nombre del Padre: ")
    nombre_madre = input("Ingrese el nombre de la Madre: ")
    dpi_padre = int(input("Ingrese el DPI del Padre: "))
    dpi_madre = int(input("Ingrese el DPI de la Madre: "))
    cumpleP = input("Ingrese la fecha de naciemiento del padre: ")
    cumpleM = input("Ingrese la fecha de naciemiento del madre: ")
    info_hospital = input("Ingrese el informe del hospital: ")
    comprobante = input("Ingrese el comprobante del pago: ")
    nombre = input("Ingrese el nombre completo del bebe: ")
    fecha = input("Ingrese la fecha que nacio el bebe: ")
    hora = int(input("Ingrese la hora de nacimiento: "))

    print('Los datos del padre son: ')
    print("El nombre del padre es: ",nombre_padre)
    print("El DPI del padre es: ",dpi_padre)
    print("El nacimiento del padre es: ",cumpleP)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Los datos de la madre son:")
    print(nombre_madre)
    print(dpi_madre)
    print(cumpleM)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Los datos del bebe son: ")
    print(nombre)
    print(fecha)
    print(hora)
    print(info_hospital)

def dpi():
    nombre = input("Nombre Completo: ")
    nac = input("Lugar de naciemiento: ")
    fecha = input("Ingresa la fecha de nacimiento: ")
    print("\nSe le entregara el DPI dentro de un mes, esperamos volver a verlo :) ")

def defuncion():
    nombre = input("Ingrese el nombre del difunto: ")
    causa_muerte= input("Ingrese la causa de muerte: ")
    sexo = input("Ingrese el genero del difunto: ")
    lugar= input("Ingrese el lugar de muerte: ")
    hora_muerte = int(input("Ingrese la hora de muerte: "))

    print("Su certificado de defuncion es: ")
    print("El nombre de su difunto es: ",nombre)
    print("Fallecio por causa de ",causa_muerte)
    print("Su genero era: ",sexo)
    print("Fallecio en: ",lugar)
    print("Fallecio a las: ",hora_muerte)
