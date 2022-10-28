import hashlib

def ejr5_1():
    mensaje = (b"Nos atacan")
    salida = hashlib.sha256(mensaje).hexdigest()
    return salida[:8]
print(ejr5_1())