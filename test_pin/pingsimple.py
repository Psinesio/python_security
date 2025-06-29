import os  # Importar a biblioteca os para executar comandos do sistema operacional

print("#" * 60)  # Imprimir uma linha de hash para formatação

ip_host = input(
    "Digite o IP ou Host a ser verificado: "
)  # Solicitar ao usuário que insira um IP ou Host para verificação

print("-" * 60)

os.system(
    f"ping -n 6 {ip_host}"
)  # Executar o comando ping com pacotes para o IP ou Host fornecido

print("-" * 60)  # Imprimir outra linha de hash para formatação
