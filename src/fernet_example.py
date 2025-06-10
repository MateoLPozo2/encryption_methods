from cryptography.fernet import Fernet

# Generate and save a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a message
message = b"Mensaje secreto con Fernet"
token = cipher.encrypt(message)

# Decrypt the message
decrypted = cipher.decrypt(token)

print("Encrypted:", token)
print("Decrypted:", decrypted.decode())

# Este código realiza los pasos clave de Fernet:
# Generación de clave: Fernet.generate_key() crea una clave secreta única.
# Inicialización del cifrador: Fernet(key) instancia un objeto Fernet con esa clave.
# Cifrado autenticado: .encrypt() produce un token Fernet seguro con marca de tiempo, IV y HMAC.
# Descifrado validado: .decrypt() asegura integridad y autenticidad antes de devolver el mensaje original.
# Este token es seguro, no puede ser manipulado ni leído sin la clave original, y es seguro para transmitirse o almacenarse temporalmente.