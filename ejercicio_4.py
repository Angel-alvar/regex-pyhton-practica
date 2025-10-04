#Angel Alvarez Santana
#Extractor de Urls y dominios
import re

#expresiones regulares
er = r'(https?://)?(www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(/[a-zA-Z0-9._%+-]*)*'
protocolo = r'https?|'
ruta = r'/[a-zA-Z0-9._%+-]*'


texto = input("Ingrese un texto: ")
coincidencias = re.findall(er, texto)
if coincidencias:
    for coincidencia in coincidencias:
        url_completa = ''.join(coincidencia)
        dominio = coincidencia[2]
        print(f"URL completa: {url_completa}, Dominio: {dominio} Protocolos: {re.findall(protocolo, url_completa)} rutas: {re.findall(ruta, url_completa)}")
else:
    print("No se encontraron URLs o dominios en el texto.")
    