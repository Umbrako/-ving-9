# -----------------------------------------------------------
#                     Oppgave d
# -----------------------------------------------------------
from datetime import datetime

class Avtale1:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet
    
now = datetime.now()
dag = now.strftime("%H:%M:%S:")
print((datetime.fromisoformat("2000-09-20 12:00:00")))







 
# -----------------------------------------------------------
#                     Oppgave e
# -----------------------------------------------------------

class Avtale:
  def __init__(self, tittel, sted):
    self.tittel = tittel
    self.sted = sted

    def __str__(self):
        return f"tittel={self.tittel}, sted ={self.sted}"

avtale = Avtale("Kvernevik", "Hafrsfjord")

print(avtale.tittel)    




# -----------------------------------------------------------
#                     Oppgave f
# -----------------------------------------------------------
class Avtale2:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet

a2 = Avtale2(input("Tittel:"), input("Sted:"), datetime.fromisoformat(input("Start:")), input("Varighet:"))
print(a2.tittel) 
print(a2.sted)
print(a2.start)
print(a2.varighet,"timer")
  
        



 
# -----------------------------------------------------------
#                     Oppgave g
# -----------------------------------------------------------
# 
# 
# 
# -----------------------------------------------------------
#                     Oppgave h
# -----------------------------------------------------------
# 
# 
# 
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
