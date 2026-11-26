# Uitbreidingen:
# - Marathon
# - In de put op vakje RANDOM
# - De doornstruik op vakje RANDOM gaat bij landen -2 vakjes terug
# - Double trouble
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
gg1 = getalinput("Hoi "+ naamspeler1+ ", Wat is jouw geluksgetal? je kunt kiezen tussen 1 t/m "+ str(vakjes)+ ". : ")
while gg1 < 1 or gg1 > vakjes:
    print("Ongeldige invoer. Voer een geldig getal in tussen 1 en", vakjes, ".")
    gg1 =getalinput ("Hoi "+ naamspeler1+ ", Wat is jouw geluksgetal? je kunt kiezen tussen 1 t/m "+ str(vakjes)+". : ")
print("jouw geluksvakje is ", str(gg1), ".")

naamspeler2 = input("Speler 2, wat is je naam? : ")
gg2 = getalinput ("Hoi "+naamspeler2+ ", Wat is jouw geluksgetal? je kunt kiezen tussen 1 t/m "+str(vakjes)+". : ")
while gg2 < 1 or gg2 > vakjes:
    print("Ongeldige invoer. Voer een geldig getal in tussen 1 en", vakjes, ".")
    gg2 =getalinput("Hoi "+ naamspeler2+ ", Wat is jouw geluksgetal? je kunt kiezen tussen 1 t/m "+ str(vakjes)+ ". : ")
print("jouw geluksvakje is "+str(gg2)+ ".") 

#gemereert de put en doornstruikvakjes op een random vakje, controleert of dit niet op een ander actie vak ligt of op het laatste vakje (omdat het anders onmogelijk is om te winnen). print daarna de locatie van de put en de doornstruik
put = random.randint(2, vakjes)
while put == gg1 or put == gg2:
    put = random.randint(2, vakjes)
while put == vakjes:
    put = random.randint(2, vakjes)
doornstruik = random.randint(3, vakjes)
while doornstruik == put:
    doornstruik = random.randint(2, vakjes)
while doornstruik == gg1 or doornstruik == gg2:
    doornstruik = random.randint(2, vakjes)
while doornstruik == vakjes:
    doornstruik = random.randint(2, vakjes)

print("De put is vakje", put, ", val je daar in moet je wachten totdat een andere speler op dat vakje beland om je uit de put te helpen.")
print("De doornstruik is vakje", doornstruik, ", val je daar in ga je 2 vakjes terug.")


print("Het spel begint! We spelen met 2 dobbelstenen. gooi je dubbele ogen dan wordt je gediskwalificeerd en mag je niet meer meespelen.")
print("Het spel is afgelopen als een speler precies op het laatste vakje landt. Land je er overheen dan ga je terug hoeveel vakjes je extra hebt gegooid.")
spelbezig = True
vakjespeler1 = 1
vakjespeler2 = 1
while spelbezig == True:
    print("Het is de beurt van", naamspeler1, ".")
    print("put = ", put,)
    print("doornstruik = ", doornstruik,)
    if vakjespeler1 -1 < 0:
        print(vakjespeler1 + naamspeler1)
        print (vakjespeler1 +1)
    else:
        if vakjespeler1 +1 > vakjes:
            print(vakjespeler1 -1)
            print(vakjespeler1 + naamspeler1)
        else:
            if vakjespeler1 -1 == put:
                print(vakjespeler1 -1)
                print(vakjespeler1 + naamspeler1)
                print (vakjespeler1 +1)

            print(vakjespeler1 -1)
            print(vakjespeler1 + naamspeler1)
            print (vakjespeler1 +1)
    if vakjespeler1 == put:
        print("Je bent in de put gevallen! Je moet wachten totdat een andere speler op dat vakje beland om je uit de put te helpen.")
