import procedimientos as pro

print("------------------------------------")
print("------ Bienvenido a RENAP ----------")
print("------------------------------------")

print('''Que documento deseas realizar
    1. Certificado de naciemiento
    2. Solicitud de DPI
    3. Certificado de defuncion''')
opcion = input()

if opcion == '1':
    pro.certificado()

