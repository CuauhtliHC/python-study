from random import choice

def randomWord():
    wordList = ["hola", "mundo", "juego", "zoologico"]
    return list(choice(wordList))

def letterUser():
    print(randomWord())
    valid = True
    while valid:
        letter = input("Ingresa una letra: ")
        if letter.isalpha():
            valid = False

def checkLetters(letter, letterList):
    return any(letter in word for word in letterList)
