#Angel Alvarez Santana
#Analizador de fechas y formateador
import re
from datetime import datetime

# Diccionario para meses en texto
meses = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12,
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

# Patrones de fechas
patrones = [
    (r"\b(\d{2})/(\d{2})/(\d{4})\b", "%d/%m/%Y"),        # DD/MM/YYYY
    (r"\b(\d{4})-(\d{2})-(\d{2})\b", "%Y-%m-%d"),        # YYYY-MM-DD
    (r"\b(\d{2})-([A-Za-z]{3})-(\d{4})\b", None),        # DD-MMM-YYYY
    (r"\b([A-Za-z]+) (\d{2}), (\d{4})\b", None),         # Mes DD, YYYY
]

def convertir_fecha(texto):
    resultados = []

    for patron, formato in patrones:
        for match in re.finditer(patron, texto):
            original = match.group(0)
            estandar = None

            try:
                if formato:  
                    estandar = datetime.strptime(original, formato).strftime("%Y-%m-%d")
                else:
                    if len(match.groups()) == 3:
                        # Caso DD-MMM-YYYY
                        if match.group(2).isalpha() and len(match.group(2)) == 3:
                            dia, mes_abrev, anio = match.groups()
                            mes = meses.get(mes_abrev.capitalize(), 0)
                            estandar = f"{anio}-{mes:02d}-{int(dia):02d}"

                        # Caso Mes DD, YYYY
                        else:
                            mes_texto, dia, anio = match.groups()
                            mes = meses.get(mes_texto.capitalize(), 0)
                            estandar = f"{anio}-{mes:02d}-{int(dia):02d}"

            except Exception:
                estandar = "No válido"

            if estandar:
                resultados.append((original, estandar))

    return resultados

# entrada de usuario
texto_usuario = input("Escribe un texto con fechas: ")

fechas = convertir_fecha(texto_usuario)

if fechas:
    print("\nFechas encontradas y convertidas:")
    for original, estandar in fechas:
        print(f"- Formato original: {original} => Estándar: {estandar}")
else:
    print("\nNo se encontraron fechas en el texto.")
