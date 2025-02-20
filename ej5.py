import re

texto = input().strip()

patron_direccion = re.compile(r"\b(?:C/|Calle) ([A-Z][a-z]+),? *(?:[nN][º]? *([0-9]+)|([0-9]+)),? *([0-9]{5})\b")

for match in patron_direccion.finditer(texto):
    calle = match.group(1)
    numero = match.group(2) if match.group(2) else match.group(3)
    cp = match.group(4)
    print(f"{cp}-{calle}-{numero}")

