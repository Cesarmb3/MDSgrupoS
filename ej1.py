import re

texto = input()

expresion = r'\b[0-9]{4}\b'

coincidencias = re.findall(expresion, texto)

for coincidencia in coincidencias:
    print(coincidencia)
