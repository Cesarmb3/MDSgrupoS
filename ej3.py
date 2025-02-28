import re

patron_fecha = re.compile(r"(\b[0-9]{4})-([0-9]{2})-([0-9]{2}\b)")
texto = input().strip()
resultado = patron_fecha.sub(lambda m: f"{m.group(3)}.{m.group(2)}.{m.group(1)}", texto)
print(resultado)