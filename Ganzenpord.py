# Uitbreidingen:
# - Marathon
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
print("Welkom bij ganzenbord! Dit spel is gemaakt voor 2 spelers.")
#onderstaande vraagt hoeveel vakjes de spelers op het bord willen hebben. checkt of de invoer een getal is en of het hoger dan 10 is.
#daarna laat hij zien hoeveel vakjes er op het bord zijn en welke vakjes de put en de doornstruik zijn
vakjes = getalinput("Hoeveel vakjes wil je op het bord hebben? (minimaal 10): ")
while vakjes < 10:
    print("Het aantal vakjes moet minimaal 10 zijn. probeer het nog eens.")
    vakjes = getalinput("Hoeveel vakjes wil je op het bord hebben? (minimaal 10)")
# vraagt aan de spelers om hun naam en geluksgetal. check of de invoer een getal is en of het tussen 1 en het aantal vakjes ligt. daarna print hij welk vakje de speler heeft gekozen
print("Het bord heeft nu", vakjes, "vakjes.")
naamspeler1 = input("Speler 1, wat is je naam? : ")
gg1 = getalinput("Hoi "+ naamspeler1+ "Wat is jouw geluksgetal? je kunt kiezen tussen 1 t/m "+ str(vakjes)+ ". : ")
while gg1 < 1 or gg1 > vakjes:
    print("Ongeldige invoer. Voer een geldig getal in tussen 1 en", vakjes, ".")
    gg1 =getalinput ("Hoi "+ naamspeler1+ "Wat is jouw geluksgetal? je kunt kiezen tussen 1 t/m "+ str(vakjes)+". : ")
print("jouw geluksvakje is ", str(gg1), ".")

naamspeler2 = input("Speler 2, wat is je naam? : ")
gg2 = getalinput ("Hoi "+naamspeler2+ "Wat is jouw geluksgetal? je kunt kiezen tussen 1 t/m "+str(vakjes)+". : ")
while gg2 < 1 or gg2 > vakjes:
    print("Ongeldige invoer. Voer een geldig getal in tussen 1 en", vakjes, ".")
    gg2 =getalinput("Hoi "+ naamspeler2+ "Wat is jouw geluksgetal? je kunt kiezen tussen 1 t/m "+ str(vakjes)+ ". : ")
print("jouw geluksvakje is "+str(gg2)+ ".") 