import os
import random
from turtle import done

def hangman():
    #Secret word that player is trying to guess
    secret_word = read()
    guessed = []
    hangmanpic = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']
    hangmanpic1 = hangmanpic[::-1]
    

    # Number of turns that player have
    failure_count = 6
    done = False
    #Loop for guess the word
    while not done:

        os.system("clear")
        print('''¡Adivina la palabra!''' )
        print(hangmanpic1[failure_count])
        for letter in secret_word:
            if letter in guessed:
                print(letter.upper(), end=" ")
            else:
                print("_", end=" ")

        print("\n")
        
        guess = input("Número de intentos restantes: " + str(failure_count) + ", Escribe una letra: ")
        assert guess.isalpha(), "Solo puedes ingresar letras"
        guessed.append(guess.lower())

        if guess.lower() not in secret_word.lower():
            failure_count -= 1
            if failure_count == 0:
                break

        done = True
        for letter in secret_word:
            if letter not in guessed:
                done = False
        
        
    if done:
        os.system("clear")
        print('''
   _ _      ___                   __
  (_) | /| / (_)__  ___  ___ ____/ /
 / /| |/ |/ / / _ \/ _ \/ -_) __/_/ 
/_/ |__/|__/_/_//_/_//_/\__/_/ (_)
    +---+
        |
        |
   \O/  |
    |   |
   / \  |     
    ========='''+ "\n")
        print("Ganaste, la palabra es: " + secret_word.upper())
    else:
        os.system("clear")
        print('''¡Adivina la palabra!''' )
        print(hangmanpic1[failure_count]+"\n")
        print("Perdiste, la palabra secreta era: "+secret_word.upper())
        
        
def read():
    words = []
    words1 ={}
    with open("./archivos/data.txt", "r", encoding="utf-8" ) as f:
        words =[line.rstrip() for line in f]
        words1 ={count: number for count, number in enumerate(words)}           
    secret_word = words1.get(random.randint(0, len(words1)))
    return secret_word


def run():
    done = True
    while done:
        hangman()
        var=input("¿Quieres volver a intentarlo? y/n: ")
        if var.lower() == "y":
            done= True
        else:
            print("Gracias por jugar")
            break


if __name__=="__main__":
    run()