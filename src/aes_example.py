from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16) # 16-byte key (128 bits)
cipher = AES.new(key, AES.MODE_CBC)
plaintext = b"Mensaje secreto AES"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Decrypt
decipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted.decode())