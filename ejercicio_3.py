#Angel Alvarez Santana
#Validador de contraseñas seguras
import re
er = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
contraseña = input("Ingrese una contraseña: ")
errores = []

if re.match(er, contraseña):
    print(contraseña ,"Contraseña segura.")
else:
    if len(contraseña) < 8:
        errores.append("Debe tener al menos 8 caracteres.")
    if not re.search(r'[A-Z]', contraseña):
        errores.append("Al menos debe tener una mayuscula.")
    if not re.search(r'[a-z]', contraseña):
        errores.append("Al menos debe tener una minúscula.")
    if not re.search(r'\d', contraseña):
        errores.append("Debe contener al menos un digito.")
    if not re.search(r'[@$!%*?&]', contraseña):
        errores.append("Debe contener al menos un caracter especial (@, $, !, %, *, ?, &).")

    print(contraseña ,"Contraseña invalida. Errores:")
    for error in errores:
        print("-", error)