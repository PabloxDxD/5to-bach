import procedimientos as pro

while True:
    print("\n------------------------------------")
    print("------ Bienvenido a RENAP ----------")
    print("------------------------------------")

    print('''Que documento deseas realizar
        1. Certificado de naciemiento
        2. Solicitud de DPI
        3. Certificado de defuncion
        4. Salir''')
    opcion = input()

    if opcion == '1':
        pro.certificado()
    elif opcion == '2':
        pro.dpi()
    elif opcion == '3':
        pro.defuncion()
    elif opcion == '4':
        print("Vuelva pronto :)")
        break
