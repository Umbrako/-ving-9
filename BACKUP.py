
# -----------------------------------------------------------
#                     Oppgave d
# -----------------------------------------------------------

import json 
from datetime import datetime

class Avtale5:
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

class Avtale1:
  def __init__(self, tittel, sted):
    self.tittel = tittel
    self.sted = sted

    def __str__(self):
        return f"tittel={self.tittel}, sted ={self.sted}"

avtale = Avtale1("Kvernevik", "Hafrsfjord")

print(avtale.tittel)   
print(avtale.sted) 


# -----------------------------------------------------------
#                     Oppgave f
# -----------------------------------------------------------
class Avtale2:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet

a2 = Avtale2(input("Tittel:"), input("Sted:"), datetime.fromisoformat(input("Start (ÅÅÅÅ-MM-DD HH:MM:SS):")), input("Varighet:"))
print()
print("Avtale 2")
print(a2.tittel) 
print(a2.sted)
print(a2.start)
print(a2.varighet,"timer")

print()

        
# -----------------------------------------------------------
#                     Oppgave g
# -----------------------------------------------------------
class Banken:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet
    
    def __str__(self):
        return f"tittel={self.tittel}, sted ={self.sted}, start={self.start}, varighet ={self.varighet}"
 
deal = Banken("Bankkort","DNB Arena",datetime.fromisoformat("2022-01-11 12:00:00"), "2 timer")
print("Banken")
print(deal.tittel)
print(deal.sted)
print(deal.start)
print(deal.varighet)


# -----------------------------------------------------------
#                     Oppgave h
# -----------------------------------------------------------

avtaler = []
avtaler.append(avtale)
avtaler.append(a2)
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
class Avtale:
  def __init__(self, tittel, sted, start, varighet): 
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet
  

  def get_tittel(self):
    return self.tittel



avtale1 = Avtale("Avtale 1", "", "", "")
avtale2 = Avtale("Avtale 2", "", "", "")
avtale3 = Avtale("absssss", "", "", "")


liste = [avtale1, avtale2, avtale3]


def funksjon(liste, streng):
    returnList = []
    for avtale in liste:
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
# 
# 
# 
# -----------------------------------------------------------
#                     Oppgave m
# -----------------------------------------------------------
# 
# 
# 
# -----------------------------------------------------------
#                     Oppgave n
# -----------------------------------------------------------
