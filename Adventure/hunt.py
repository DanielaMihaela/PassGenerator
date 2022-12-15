import random
cave = ["death", "death", "death"]

hunterName ="Bob"
hunterHP = 100
caveTimeToCheckAWae = 50

randomNumber = random.randint(0, 2)
cave[randomNumber] = "relic"

attempts = 0
days = 1

hunterHP = hunterHP - caveTimeToCheckAWae

caleaAleasa = input("Pestera are 3 cai. Pe ce cale vrei sa o iei?")
aiGasitRelicva = ""

if cave[int(caleaAleasa)] == "relic":
    print("ai gasit calea, ai gasit relicva")
    aiGasitRelicva = True
else:
    print("nu ai gasit relicva")
    aiGasitRelicva = False
    
attempts = attempts + 1
hunterHP = hunterHP - caveTimeToCheckAWae

caleaNoua = ""  
if aiGasitRelicva == False :
    caleaNoua = input("Mai incearca alta cale ca sa gasesti relicva , mai ai 2 incercari !")
    cave.pop(0)
    
if cave[int(caleaNoua)] == "relic":
    print("ai gasit calea, ai gasit relicva")
    aiGasitRelicva = True
    hunterHP -= caveTimeToCheckAWae
else:
    print("nu ai gasit relicva, revino maine si i-ao pe partea cealalta")
    aiGasitRelicva = False
    hunterHP -= (2 * caveTimeToCheckAWae)
    

