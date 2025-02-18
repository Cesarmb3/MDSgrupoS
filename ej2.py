import re

texto = input().strip()

expresion = r'\bE[- ]?[0-9]{4}[- ]?[A-Z]{3}\b|\b[0-9]{4}[- ]?[A-Z]{3}\b'

coincidencias = re.findall(expresion, texto)

for coincidencia in coincidencias:
    print(coincidencia)
