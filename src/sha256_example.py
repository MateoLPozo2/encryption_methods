import hashlib

data = "mensaje de prueba"
hashed = hashlib.sha256(data.encode()).hexdigest()

print("SHA-256 Hash:", hashed)