import hashlib
salida= hashlib.sha256(b'El Libro De python').hexdigest()
print(salida)