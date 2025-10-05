#Angel Alvarez Santana
#validador de correo electronico simple
import re
import matplotlib.pyplot as plt
#expresion regular para validar correo
er = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

patron = re.compile(er, re.UNICODE)
archivo = open("correos.txt", "r")
texto = archivo.read()
coincidencias = re.findall(patron, texto)
invalidos = re.findall(r'\S+@\S+', texto)
invalidos = [correo for correo in invalidos if correo not in coincidencias]

if coincidencias:
    print("Correos validos encontrados:" ,(len(coincidencias)))
if invalidos:
    print("Correos invalidos encontrados:",(len(invalidos)))

#graficar
plt.xlabel('Tipo de correo')
plt.ylabel('Cantidad de correos')
plt.title('Correos validos e invalidos')
tipos = ['Validos', 'Invalidos']
cantidades = [len(coincidencias), len(invalidos)]
plt.bar(tipos, cantidades, color=['green', 'red'])
plt.show()
