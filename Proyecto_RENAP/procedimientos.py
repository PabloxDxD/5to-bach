def certificado():
    print('''Los requisitos para poder registrar a su bebe son
    1. Nombre de los padres
    2. DPI de ambos padres
    3. Informe de naciemto extendido por el hospital
    4. Comprobante de pago completo
    5. Nombre Completo del bebe''')

    nombre_padre = input("Ingrese el nombre del Padre: ")
    nombre_madre = input("Ingrese el nombre de la Madre: ")
    dpi_padre = int(input("Ingrese el DPI del Padre: "))
    dpi_madre = int(input("Ingrese el DPI de la Madre: "))
    info_hospital = input("Ingrese el informe del hospital: ")
    comprobante = input("Ingrese el comprobante del pago: ")
    nombre = input("Ingrese el nombre completo del bebe: ")

    print('Sus datos son: ')
    print(nombre_padre)
    print(nombre_madre)
    print(dpi_padre)
    print(dpi_madre)
    print(info_hospital)
    print(comprobante)
    print(nombre)
