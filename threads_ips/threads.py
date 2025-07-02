import time  # Importing the time module
from threading import Thread


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        print(f"{piloto} percorreu {trajeto} km")
        time.sleep(0.5)  # Pause for 0.5 seconds


# Creating threads for two cars
t_carro1 = Thread(target=carro, args=(1, "Piloto 1"))
t_carro2 = Thread(target=carro, args=(1.5, "Piloto 2"))

# Starting the threads
t_carro1.start()
t_carro2.start()

# Ensuring both threads complete execution
t_carro1.join()
t_carro2.join()
