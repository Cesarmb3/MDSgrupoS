import re


patron_fecha = re.compile(r"(\b\d{4})-(\d{2})-(\d{2}\b)")
texto = input().strip()
resultado = patron_fecha.sub(lambda m: f"{m.group(3)}.{m.group(2)}.{m.group(1)}", texto)
print(resultado)