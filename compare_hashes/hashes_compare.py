import hashlib
import os

arquivo1 = "a.txt"
arquivo2 = "b.txt"

# Check if files exist
if not os.path.exists(arquivo1):
    print(f"Erro: O arquivo '{arquivo1}' não foi encontrado.")
    exit(1)

if not os.path.exists(arquivo2):
    print(f"Erro: O arquivo '{arquivo2}' não foi encontrado.")
    exit(1)

hash1 = hashlib.new("ripemd160")

hash1.update(open(arquivo1, "rb").read())

hash2 = hashlib.new("ripemd160")
hash2.update(open(arquivo2, "rb").read())

if hash1.digest() != hash2.digest():
    print(f"Os arquivos {arquivo1} e {arquivo2} são diferentes.")
    print(f"Hash do arquivo {arquivo1}: {hash1.hexdigest()}")
    print(f"Hash do arquivo {arquivo2}: {hash2.hexdigest()}")
else:
    print(f"Os arquivos {arquivo1} e {arquivo2} são iguais.")
    print(f"Hash do arquivo {arquivo1}: {hash1.hexdigest()}")
    print(f"Hash do arquivo {arquivo2}: {hash2.hexdigest()}")
