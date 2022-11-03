# -----------------------------------------------------------
#                     Oppgave d
# -----------------------------------------------------------

import json 
from datetime import datetime

class Avtale:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet
    
  
    
now = datetime.now()
dag = now.strftime("%H:%M:%S:")
print(datetime.fromisoformat("2000-09-20 12:00:00"))

# -----------------------------------------------------------
#                     Oppgave e
# -----------------------------------------------------------



def __str__(self, tittel, sted, start, varighet):
      return f"tittel={self.tittel}, sted ={self.sted}, start={self.start}, varighet={varighet}"

avtale = Avtale("Kvernevik", "Hafrsfjord", "start", "varighet")



print(avtale.tittel)   
print(avtale.sted) 



# -----------------------------------------------------------
#                     Oppgave f
# -----------------------------------------------------------
def nyAvtale(self, tittel, sted, start, varighet):
    self.tittel = input("Tittel:")
    self.sted = input("Sted:")
    self.start = datetime.fromisoformat(input("Start (ÅÅÅÅ-MM-DD HH:MM:SS):"))
    self.varighet =input("Varighet: ")
    return f"tittel={self.tittel}, sted ={self.sted}, start={self.start}, varighet={varighet}"
 
    
    

print()
print("Avtale 2")
print(nyAvtale.tittel) 
print(nyAvtale.sted)
print(nyAvtale.start)
print(nyAvtale.varighet,"timer")
print()

        
# -----------------------------------------------------------
#                     Oppgave g
# -----------------------------------------------------------

    
def Banken(self, tittel, sted, start, varighet):
        
        return f"tittel={self.tittel}, sted ={self.sted}, start={self.start}, varighet ={self.varighet}"
 
deal = Avtale("Bankkort","DNB Arena",datetime.fromisoformat("2022-01-11 12:00:00"), "2 timer")
print()
print("Banken")
print(deal.tittel)
print(deal.sted)
print(deal.start)
print(deal.varighet)


# -----------------------------------------------------------
#                     Oppgave h
# -----------------------------------------------------------

avtaler = []
avtaler.append(Avtale)
avtaler.append(deal)
    
json_object = json.dumps({'avtaler': avtaler}, indent=4)

with open("test.json", "w") as outfile:
    outfile.open(json_object)
    
    
        
# -----------------------------------------------------------
#                     Oppgave i
# -----------------------------------------------------------
with open("test.json", "r") as outfile:
    print(outfile.read())
    
# -----------------------------------------------------------
#                     Oppgave j
# -----------------------------------------------------------
def alle_avtaler_paa_dato(avtaler, dato):
    avtaler_paa_dato = []
    for avtale in avtaler:
        avtale_dato = datetime.fromisoformat(avtale.start)
        if avtale_dato >= dato:
            avtaler.append(avtale)
        return avtaler_paa_dato

# -----------------------------------------------------------
#                     Oppgave k
# -----------------------------------------------------------

def get_tittel(self):
    return self.tittel



avtale1 = Avtale("Avtale 1", "", "", "")
avtale2 = Avtale("Avtale 2", "", "", "")
avtale3 = Avtale("absssss", "", "", "")


liste = [avtale1, avtale2, avtale3]


def funksjon(liste, streng):
    returnList = []
    for Avtale in liste:
        tittelValue = avtale.get_tittel()
        if (tittelValue.find(streng) != -1):
            returnList.append(avtale)
    
    return returnList



print(funksjon(liste, "Avtale"))


avtaler = funksjon(liste, "Avtale")
for avtale in avtaler:
    print(avtale.get_tittel())
 
 
# -----------------------------------------------------------
#                     Oppgave l
# -----------------------------------------------------------

mylist = []
def meny():

    while True:
        operation = input('''
        Select operation:
        [1] Lese inn avtaler fra fil
        [2] Skrive avtalene til fil
        [3] Skrive inn ny avtale
        [4] Skrive ut alle avtalene
        [5] Avslutt

        ''')
        if operation == 1
            print("")

        elif operation == 2
            print()

        elif operation == 3

        elif operation == 4

        elif operation == 5
            break
# -----------------------------------------------------------
#                     Oppgave m
# -----------------------------------------------------------
# 
# 
# 
# -----------------------------------------------------------
#                     Oppgave n
# -----------------------------------------------------------