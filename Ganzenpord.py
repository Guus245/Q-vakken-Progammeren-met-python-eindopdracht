import random
# onderstaande functie zorgt ervoor dat een invoer een getal is. als dit niet is vraagt hij opnieuw voor een getal. 
def getalinput(a):
    invoerCorrect = False
    while invoerCorrect == False:
        getal = input(a)
        if getal.isdigit():
            invoerCorrect = True
            return int(getal)
        else:
        print("Ongeldige invoer. Voer een geldig getal in.")
Print("Welkom bij ganzenbord!")
vakjes = getalinput("Hoeveel vakjes wil je op het bord hebben? (minimaal 10)")
while vakjes < 10:
    print("Het aantal vakjes moet minimaal 10 zijn. probeer het nog eens.")
    vakjes = getalinput("Hoeveel vakjes wil je op het bord hebben? (minimaal 10)")
Print("Het bord heeft nu", vakjes, "vakjes.")