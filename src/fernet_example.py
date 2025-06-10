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