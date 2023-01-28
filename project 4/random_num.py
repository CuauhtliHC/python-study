from random import randint

numRandom = randint(1, 100)

name = input('¿Cual es tu nombre?: ')

print(f"Bueno, {name}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

attempts = 8

while attempts >= 0:
    if attempts > 0:
        choiceNum = input()
        attempts -= 1
        if int(choiceNum) < 1 or int(choiceNum) > 100:
            print("Ha elegido un número que no está permitido")
        elif int(choiceNum) < numRandom:
            print(f"Ha elegido un número menor al número secreto, le quedan {attempts} intentos")   
        elif int(choiceNum) > numRandom:
            print(f"Ha elegido un número mayor al número secreto, le quedan {attempts} intentos")
        else:
            print(f"Ha eligido el numero secreto, le tomo {8 - attempts}")
            break
    elif attempts == 0:
        print("Te haz quedado sin intentos")
        break