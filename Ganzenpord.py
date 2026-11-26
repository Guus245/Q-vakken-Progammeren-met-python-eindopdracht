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

#dobbelsteen functie, kijkt naar de variabele en geeft afhankelijk van 1 of 2 dobbelstenen een random getal terug tussen de 1 en de 6. speel je met 2 dobbelstenen en gooi je dubbel geeft hij 0 terug en wordt je gediskwalificeerd. anders geeft hij de som van de 2 dobbelstenen terug.
def dobbelsteen():
    if dobbelstenen == 1:
        dobbel = random.randint(1, 6)
        print("Je hebt een", dobbel, "gegooid.")
        return dobbel
    else:
        dobbel1 = random.randint(1, 6)
        dobbel2 = random.randint(1, 6)
        print("Je hebt een", dobbel1, "en een", dobbel2, "gegooid.")
        if dobbel1 == dobbel2:
            print("Je hebt dubbele ogen gegooid! Je bent gediskwalificeerd en mag niet meer meespelen.")
            return 0
        else:
            return dobbel1 + dobbel2


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
while put == gg1 or put == gg2 or put == vakjes:
    put = random.randint(2, vakjes)
doornstruik = random.randint(3, vakjes)
while doornstruik == put or doornstruik == gg1 or doornstruik == gg2 or doornstruik == vakjes:
    doornstruik = random.randint(3, vakjes)

print("De put is vakje", put, ", val je daar in moet je wachten totdat een andere speler op dat vakje beland om je uit de put te helpen.")
print("De doornstruik is vakje", doornstruik, ", val je daar in ga je 2 vakjes terug.")

dobbelsteenincorrect = False
while dobbelsteenincorrect == False:
    dobbelstenen = getalinput(" Wil je met een of 2 dobbelstenen spelen? (voer 1 of 2 in): ")
    if dobbelstenen == 1:
        print("Je speelt met 1 dobbelsteen.")
        dobbelsteenincorrect = True
    else:
        if dobbelstenen == 2:
            print("Je speelt met 2 dobbelstenen. gooi je dubbele dan ben je af en wint de andere speler.")
            dobbelsteenincorrect = True
        else:   
            print("Ongeldige invoer. Je kunt alleen 1 of 2 dobbelstenen kiezen. probeer het nog eens.")

print("Het spel begint! ")
print("Het spel is afgelopen als een speler precies op het laatste vakje landt. Land je er overheen dan ga je terug hoeveel vakjes je extra hebt gegooid.")
spelbezig = True
vakjespeler1 = 1
vakjespeler2 = 1
speler1put = False
speler2put = False

while spelbezig == True:
    print("Het is de beurt van", naamspeler1, ".")
    print("put = ", put,)
    print("doornstruik = ", doornstruik,)
    print("geluksvakje = ", gg1,)
    #geeft aan de speler weer welk vakje ze staan, en welke vakjes er naast liggen. mocht het vakje niet bestaan dan laat hij niks zien
    if vakjespeler1 -1 < 1:
        pass
    else:
        if vakjespeler1 -1 == put:
            print(vakjespeler1 -1 , " put")
        else:
            if vakjespeler1 -1 == doornstruik:
                print(vakjespeler1 -1 ,  "doornstruik")
            else:
                print(vakjespeler1 -1)
    print(vakjespeler1 , naamspeler1)
    if vakjespeler1 +1 > vakjes:
        pass
    else:
        if vakjespeler1 +1 == put:
            print(vakjespeler1 +1 , "put")
        else:
            if vakjespeler1 +1 == doornstruik:
                print(vakjespeler1 +1 , "doornstruik")
            else:
                print(vakjespeler1 +1)
    if not speler1put:
        invoer = input("druk op een knop om te rollen, op o om op te geven : ")
        if not invoer == "o":
            dobbel = dobbelsteen()
            if dobbel == 0:
                spelbezig = False
                print(naamspeler1, "is gediskwalificeerd en mag niet meer meespelen.")
                print(naamspeler2, "heeft gewonnen!")
                break
            else:
                vakjespeler1 = vakjespeler1 + dobbel
                if vakjespeler1 > vakjes:
                    vakjespeler1 = vakjes - (vakjespeler1 - vakjes)
                    print("Je bent over het laatste vakje gegaan! Je gaat terug naar vakje", vakjespeler1)
                if vakjespeler1 == gg1:
                    print("Je bent op je geluksgetal geland! Je mag nogmaals", dobbel, "stappen zetten.")
                    vakjespeler1 = vakjespeler1 + dobbel
                if vakjespeler1 > vakjes:
                    vakjespeler1 = vakjes - (vakjespeler1 - vakjes)
                    print("Je bent over het laatste vakje gegaan! Je gaat terug naar vakje", vakjespeler1)
                    #geluksgetal bonus wordt maar 1 keer per ronde gegeven omdat je anders in een soft brick state komt
                if vakjespeler1 == doornstruik:
                    print("Je bent in de doornstruik gevallen! Je gaat 5 vakjes terug.")
                    vakjespeler1 = vakjespeler1 - 5
                if vakjespeler1 == put:
                    if speler2put == True:
                        print("Je bent in de put gevallen! Maar", naamspeler2, "staat ook in de put. Jullie helpen elkaar om uit de put te komen!")
                        speler2put = False
                        vakjespeler1 = vakjespeler1 + 1
                    else:
                        speler1put = True
                        print("Je bent in de put gevallen! Je moet wachten totdat een andere speler op dat vakje beland om je uit de put te helpen.")

                if vakjespeler1 == vakjes:
                    print(naamspeler1, "heeft gewonnen!")
                    spelbezig = False
                    break
                else :
                    print("Je staat nu op vakje", vakjespeler1)
        else : 
            print(naamspeler1, "heeft opgegeven. ", naamspeler2, "heeft gewonnen!")
            spelbezig = False
            break
    if speler1put:
        print("Je staat in de put. Je moet wachten totdat een andere speler op dat vakje beland om je uit de put te helpen.")
    

        # Speler 2
    print("Het is de beurt van", naamspeler2, ".")
    print("put = ", put,)
    print("doornstruik = ", doornstruik,)
    print("geluksvakje = ", gg2,)
    #geeft aan de speler weer welk vakje ze staan, en welke vakjes er naast liggen. mocht het vakje niet bestaan dan laat hij niks zien
    if vakjespeler2 -1 < 1:
        pass
    else:
        if vakjespeler2 -1 == put:
            print(vakjespeler2 -1 , " put")
        else:
            if vakjespeler2 -1 == doornstruik:
                print(vakjespeler2 -1 ,  "doornstruik")
            else:
                print(vakjespeler2 -1)
    print(vakjespeler2 , naamspeler2)
    if vakjespeler2 +1 > vakjes:
        pass
    else:
        if vakjespeler2 +1 == put:
            print(vakjespeler2 +1 , "put")
        else:
            if vakjespeler2 +1 == doornstruik:
                print(vakjespeler2 +1 , "doornstruik")
            else:
                print(vakjespeler2 +1)
    if not speler2put:
        invoer = input("druk op een knop om te rollen, op o om op te geven : ")
        if not invoer == "o":
            dobbel = dobbelsteen()
            if dobbel == 0:
                spelbezig = False
                print(naamspeler2, "is gediskwalificeerd en mag niet meer meespelen.")
                print(naamspeler1, "heeft gewonnen!")
                break
            else:
                vakjespeler2 = vakjespeler2 + dobbel
                if vakjespeler2 > vakjes:
                    vakjespeler2 = vakjes - (vakjespeler2 - vakjes)
                    print("Je bent over het laatste vakje gegaan! Je gaat terug naar vakje", vakjespeler2)
                if vakjespeler2 == gg2:
                    print("Je bent op je geluksgetal geland! Je mag nogmaals", dobbel, "stappen zetten.")
                    vakjespeler2 = vakjespeler2 + dobbel
                if vakjespeler2 > vakjes:
                    vakjespeler2 = vakjes - (vakjespeler2 - vakjes)
                    print("Je bent over het laatste vakje gegaan! Je gaat terug naar vakje", vakjespeler2)
                    #geluksgetal bonus wordt maar 1 keer per ronde gegeven omdat je anders in een soft brick state komt
                if vakjespeler2 == doornstruik:
                    print("Je bent in de doornstruik gevallen! Je gaat 5 vakjes terug.")
                    vakjespeler2 = vakjespeler2 - 5
                if vakjespeler2 == put:
                    if speler1put == True:
                        print("Je bent in de put gevallen! Maar", naamspeler1, "staat ook in de put. Jullie helpen elkaar om uit de put te komen!")
                        speler1put = False
                        vakjespeler2 = vakjespeler2 + 1
                    else:
                        speler2put = True
                        print("Je bent in de put gevallen! Je moet wachten totdat een andere speler op dat vakje beland om je uit de put te helpen.")

                if vakjespeler2 == vakjes:
                    print(naamspeler2, "heeft gewonnen!")
                    spelbezig = False
                    break
                else :
                    print("Je staat nu op vakje", vakjespeler2)
        else : 
            print(naamspeler2, "heeft opgegeven. ", naamspeler1, "heeft gewonnen!")
            spelbezig = False
            break
    if speler2put:
        print("Je staat in de put. Je moet wachten totdat een andere speler op dat vakje beland om je uit de put te helpen.")
  

  # (prive na cijfer) github repository: https://github.com/Guus245/Q-vakken-Progammeren-met-python-eindopdracht