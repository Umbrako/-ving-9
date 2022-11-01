# -----------------------------------------------------------
#                     Oppgave d FERDIG
# -----------------------------------------------------------
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
#                     Oppgave e FERDIG
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
#                     Oppgave f FERDIG
# -----------------------------------------------------------
class Avtale2:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet

a2 = Avtale2(input("Tittel:"), input("Sted:"), datetime.fromisoformat(input("Start:")), input("Varighet:"))
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
class Avtale3:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet
    
    def __str__(self):
        return f"tittel={self.tittel}, sted ={self.sted}, start={self.start}, varighet ={self.varighet}"
 
deal = Avtale3("Bankkort","DNB Arena",datetime.fromisoformat("2022-01-11 12:00:00"), "2 timer")
print("Avtale 3")
print(deal.tittel)
print(deal.sted)
print(deal.start)
print(deal.varighet)


# -----------------------------------------------------------
#                     Oppgave h
# -----------------------------------------------------------
with open('readme.txt', 'w') as Avtaler:
    Avtaler.write('Create a new text file!')
# -----------------------------------------------------------
#                     Oppgave i
# -----------------------------------------------------------
# 
# 
# 
# -----------------------------------------------------------
#                     Oppgave j
# -----------------------------------------------------------
# 
# 
# 
# -----------------------------------------------------------
#                     Oppgave k
# -----------------------------------------------------------
# 
# 
# 
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
