import random

health = 50

difficulity = 1

potion_heatlh = int(random.randint(25,50) / difficulity) 

health = health + potion_heatlh

print(health)

