import re



texto = input().strip()

patron_alumno = re.compile(r"(\b[a-z])\.([a-z]{2,})\.([0-9]{4})@alumnos\.urjc\.es")
patron_profesor = re.compile(r"(\b[a-z]+)\.([a-z]{2,})@urjc\.es")

for match in patron_alumno.finditer(texto):
    inicial, apellido, anio = match.groups()
    print(f"alumno {apellido} matriculado en {anio}")

for match in patron_profesor.finditer(texto):
    nombre, apellido = match.groups()
    print(f"profesor {nombre} apellido {apellido}")