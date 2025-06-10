import base58

data = b"mensaje codificado"
encoded = base58.b58encode(data)
decoded = base58.b58decode(encoded)

print("Encoded Base58:", encoded.decode())
print("Decoded:", decoded.decode())