Para ejecutar las pruebas:

```bash
# Crear entorno virtual (si es necesario)
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias necesarias
pip install cryptography pycryptodome base58

# Ejecutar scripts
python src/fernet_example.py
python src/sha256_example.py
python src/aes_example.py
python src/rsa_example.py
python src/base58_example.py

# Desactivar y eliminar el entorno
deactivate
rm -r venv