#Angel Alvarez Santana
#Extractor de numeros de telefono
import re

patron = r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}'

texto = input("Ingrese un texto: ")
coincidencias = re.findall(patron, texto)
if coincidencias:
    print("Números de teléfono encontrados:", coincidencias)
else:
    print("No se encontraron números de teléfono en el texto.")
    