# calculatrice:
fin = 0

while fin ==0:

    print("Bonjour calculons ensemble 😊")
    while True:
            try:
                nombreUn = float(input("Le premier nombre : "))
                break 
            except ValueError:
                print("Ce n'est pas un nombre entier valide. Réessayez.")

    while True:
            try:
                nombreDeux = float(input("Le deuxième nombre : "))
                break
            except ValueError:
                print("Ce n'est pas un nombre entier valide. Réessayez.")

    operation = input("que faut il en faire (/ : + : - : * ):")

    if operation == "+":
        print(round((float(nombreUn) + float(nombreDeux)),2))
    elif operation == "-":
        print(round((float(nombreUn) - float(nombreDeux)),2))
    elif operation == "/" and int(nombreDeux)!= 0:
        print(round((float(nombreUn) / float(nombreDeux)),2))
    elif operation == "*":
        print(round((float(nombreUn) * float(nombreDeux)),2))
    else:
        print("on ne peut pas diviser par zéro 😒")

    encore = input("souhaitez-vous continuer ? y/n -- ")

    if encore == "y":
        fin =0
    else:
        fin = 1




