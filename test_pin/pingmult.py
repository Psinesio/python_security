import os
import time

with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:

        print("verificando o IP: ", ip)
        print("-" * 60)
        os.system(f"ping -n 2 {ip}")
        print("-" * 60)
        time.sleep(5)  # Aguardar 5 segundos antes de verificar o próximo IP
