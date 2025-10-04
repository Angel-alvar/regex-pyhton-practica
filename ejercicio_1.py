#Angel Alvarez Santana
#validador de correo electronico simple
import re

#expresion regular para validar correo
er = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

#entrada
correo = input("Ingrese un correo electrónico: ")
if re.match(er, correo):
    print("Correo electrónico válido.")
else:
    print("Correo electrónico inválido.")