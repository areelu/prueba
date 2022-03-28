import random


simulaciones = 10000

cont = 0

for simulacion in range(simulaciones):
    x = random.uniform(0, 1)
    y = random.uniform(0, 2)
    if x < y:
        cont += 1

print(cont)
