from oving_8_oppgave_b_c import Sporsmaal

def les_inn_sporsmaalsfil(filnavn):
    with open(filnavn, encoding="UTF8") as fila:
        for linje in fila:
            komponenter = linje.split(":")
            sporsmaalstekts = komponenter[0]
            korrekt_svar = int(komponenter[1])
            svarliste_streng = komponenter[2]
            svarliste_streng = svarliste_streng.strip("[]")
            svaralternativer = svarliste_streng.split(",")
            nytt_sporsmaal = sporsmaal(sporsmaalstekts, svaralternativer)
            sporsmaalene.append(nytt_sporsmaal)
        return sporsmaalene

if __name__ == "__main__":
    sporsmaalsliste = les_inn_sporsmaalsfil("sporsmaalsfil.txt")
    for sporsmaal in  sporsmaalsliste:
        print(sporsmaal)
        svar_1 = int(input("spiller 1: Velg"))
        svar_2 = int(input("spiller 2: Velg"))
        print("korrekt svar", sporsmaal.korrekt_svar_tekst())
        if svar_1 == sporsmaal.korrekt_svar:
            print("spiller 1 gudd")
        if svar_2 == sporsmaal.korrekt_svar:
            print("spiller 2 gudd")