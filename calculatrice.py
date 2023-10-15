# calculatrice:
#je vais récupérer ce que me donne l'utilisateur

# problème sur la division à zéro

import math

fin = 0

while fin ==0:

    print("Bonjour calculons ensemble 😊")

    # numberOne = input("le premier nombre : ")
    # numberTwo = input("le deuxième nombre : ")
    # operation = input("que faut il en faire :")

    while True:
            try:
                numberOne = float(input("Le premier nombre : "))
                break 
            except ValueError:
                print("Ce n'est pas un nombre entier valide. Réessayez.")

    while True:
            try:
                numberTwo = float(input("Le deuxième nombre : "))
                break
            except ValueError:
                print("Ce n'est pas un nombre entier valide. Réessayez.")

    operation = input("que faut il en faire (/ : + : - : * ):")



    if numberTwo == 0:
        print("problème")

    if numberTwo == 0:
        print("problème")

    if operation == "+":
        print(round((float(numberOne) + float(numberTwo)),2))
    elif operation == "-":
        print(round((float(numberOne) - float(numberTwo)),2))
    elif operation == "/" and int(numberTwo)!= 0:
        print(round((float(numberOne) / float(numberTwo)),2))
    elif operation == "*":
        print(round((float(numberOne) * float(numberTwo)),2))
    else:
        print("on ne peut pas diviser par zéro 😒")

    encore = input("souhaitez-vous continuer ? y/n -- ")

    if encore == "y":
        fin =0
    else:
        fin = 1




