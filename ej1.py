import re


texto = input()

expresion = '[0-9]{4}'

coincidencias = re.findall(expresion, texto)

if coincidencias:
    for coincidencia in coincidencias:
        print(coincidencia)
