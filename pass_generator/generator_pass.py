import random
import string

tamanho = int(input("Digite o tamanho da senha: "))

chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"

rnd = random.SystemRandom()  # Use SystemRandom for better randomness

print("".join(rnd.choice(chars) for _ in range(tamanho)))
