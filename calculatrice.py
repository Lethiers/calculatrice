# calculatrice:
#je vais récupérer ce que me donne l'utilisateur

# problème sur la division à zéro

fin = 0

while fin ==0:

    print("Bonjour calculons ensemble 😊")

    numberOne = input("le premier nombre : ")
    numberTwo = input("le deuxième nombre : ")
    operation = input("que faut il en faire :")

    if numberTwo == 0:
        print("problème")

    if numberTwo == 0:
        print("problème")

    if operation == "+":
        print(int(numberOne) + int(numberTwo))
    elif operation == "-":
        print(int(numberOne) - int(numberTwo))
    elif operation == "/" and int(numberTwo)!= 0:
        print(int(numberOne) / int(numberTwo))
    elif operation == "*":
        print(int(numberOne) * int(numberTwo))
    else:
        print("on ne peut pas diviser par zéro 😒")

    encore = input("souhaitez-vous continuer ? y/n -- ")

    if encore == "y":
        fin =0
    else:
        fin = 1




