# -----------------------------------------------------------
#                     Oppgave d
# -----------------------------------------------------------

import json
from datetime import datetime
from typing import List, Optional

prioritet_verdier = {"VANLIG": 1, "VIKTIG": 2, "SVÆRT VIKTIG": 3}


# -----------------------------------------------------------
#                     Oppgave 10c)
# -----------------------------------------------------------

class Kategori:
    def __init__(self, id_: str, navn: str, prioritet: str):
        self.id_ = id_
        self.navn = navn
        self.prioritet = prioritet

    def __str__(self):
        return f"id_={self.id_}, navn={self.navn}, prioritet={prioritet_verdier[self.prioritet]}"


# -----------------------------------------------------------
#                     Oppgave 10g)
# -----------------------------------------------------------

class Sted:
    def __init__(self,
                 id_: str,
                 navn: str,
                 adresse=None,
                 post_nummer=None,
                 post_sted=None):
        self.id_ = id_
        self.navn = navn
        self.adresse = adresse
        self.post_nummer = post_nummer
        self.post_sted = post_sted

    def __str__(self):
        # Pga. vi vil bare ta med instance variables som ikke er none
        # kan vi loope gjennom dictionary-en til selve klassen som
        # inneholder egenskapene til objektet
        verdier = []
        for egenskap in self.__dict__:
            verdi = self.__dict__[egenskap]
            if verdi:
                verdier.append(f"{egenskap}={verdi}")
        return ', '.join(verdier)


class Avtale:
    def __init__(self,
                 tittel: str,
                 sted: Sted,
                 start: datetime,
                 varighet: int,
                 kategorier: List[Kategori]):
        self.tittel = tittel
        self.sted = sted
        self.start = start
        self.varighet = varighet
        self.kategorier = kategorier

    def legg_til_kategori(self, ny_kategori: Kategori):
        """Legg til en ny kategori"""

        print(f"Kategorien '{ny_kategori.navn}' ble lagt inn i avtalen")
        self.kategorier.append(ny_kategori)

    # Oppgave 10s)
    def prioritet(self):
        v = 1
        for kategori in self.kategorier:
            v = max(v, prioritet_verdier[kategori.prioritet])
            # Kan stoppe loop dersom prioritet er høyest (3)
            if v == 3:
                break
        return v

    # Oppgave e
    # Hentet fra https://stackoverflow.com/a/5618910
    def __str__(self):
        return f"tittel={self.tittel}, " \
               f"sted={self.sted.navn}, " \
               f"start={self.start}, " \
               f"varighet={self.varighet}, " \
               f"kategorier={', '.join([kategori.navn for kategori in self.kategorier])}, " \
               f"prioritet={self.prioritet()}"


# -----------------------------------------------------------
#                     Oppgave f
# -----------------------------------------------------------

def velg_eller_lag_ny_sted(lagrede_steder: List[Sted]) -> Optional[Sted]:
    """
    Velg et eksisterende Sted-objekt
    eller lag en nytt enkelt Sted-objekt
    """

    # La brukeren få velge mellom registrerte steder
    # Dersom sted ikke eksisterer lar vi brukeren lage en ny
    # og legger den inn i lagrede_steder (systemet)
    skriv_ut_liste(lagrede_steder, overskrift="Velg et sted...")

    sted_indeks = input("Velg en indeks fra listen over. Dersom indeks-en ikke eksisterer "
                        "vil du automatisk lage en ny Sted-objekt # ")

    try:
        sted_indeks_int = int(sted_indeks)
    except ValueError:
        print("Du oppga ikke en int!")
        return None

    try:
        sted = lagrede_steder[sted_indeks_int]
    except IndexError:
        steds_navn = input("\nSkriv inn et navn for det nye Sted-objektet # ")
        sted = Sted(sted_indeks, steds_navn)

    lagrede_steder.append(sted)
    return sted


def lag_ny_avtale(lagrede_steder: List[Sted]) -> Optional[Avtale]:
    """Registrer en ny avtale"""

    tittel = input("Skriv inn avtale tittel # ")

    sted = velg_eller_lag_ny_sted(lagrede_steder)

    # velg_eller_lag_ny_sted kan av og til returnere None!
    if not isinstance(sted, Sted):
        return None

    start = input("Skriv inn avtale start 'ÅÅÅÅ-MM-DD HH:MM:SS' # ")
    varighet = input("Skriv inn avtale varighet (minutter) # ")

    # Sjekk om vi kan konvertere start til et datetime objekt
    try:
        start_tid = datetime.fromisoformat(start)
    except ValueError:
        print("Dato-formatet du oppgav ble ikke gjenkjent, bruk 'ÅÅÅÅ-MM-DD HH:MM:SS'")
        return None

    # Sjekk om varighet er et tall
    try:
        varighet_int = int(varighet)
    except ValueError:
        print("Du må skrive inn et gyldig tall for varighet!")
        return None

    return Avtale(tittel, sted, start_tid, varighet_int, [])


# -----------------------------------------------------------
#                     Oppgave g
# -----------------------------------------------------------
def skriv_ut_liste(objekter: List[object], overskrift=None) -> None:
    """Skriv ut en liste med objekter til skjermen"""

    if not objekter:
        print("Listen du ville ta en titt på er tom...")
        return

    # Pga. overskrift er frivillig må vi først se om overskrift ble oppgitt
    if overskrift:
        print(overskrift)

    # Loop gjennom listen og skriv ut indeks + tittel til objekt
    # {type(objekt).__name__} er hentet fra https://stackoverflow.com/a/511059
    for i in range(len(objekter)):
        objekt = objekter[i]
        print(f"#{i} {type(objekt).__name__} {objekt}")


# -----------------------------------------------------------
#                     Oppgave h
# -----------------------------------------------------------

# Hentet fra https://stackoverflow.com/a/60035604
# og https://stackoverflow.com/a/35780962
# Vi trenger denne for å konvertere datetime object til string
def datetime_option(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return obj.__dict__


def skriv_avtaler_til_fil(lagrede_kategorier: List[Kategori],
                          lagrede_steder: List[Sted],
                          lagrede_avtaler: List[Avtale]) -> None:
    """
    Skriv liste med kategorier,
    steder og kategorier til json fil
    """

    skriv_kategorier_til_fil(lagrede_kategorier)
    skriv_steder_til_fil(lagrede_steder)

    json_object = json.dumps(lagrede_avtaler, default=datetime_option,
                             indent=4, separators=(',', ': '),
                             ensure_ascii=False)

    with open("avtale_liste.json", "w", encoding='utf8') as json_fil:
        json_fil.write(json_object)


# -----------------------------------------------------------
#                     Oppgave i
# -----------------------------------------------------------

def kategori_fra_id(lagrede_kategorier: List[Kategori], id_: str) -> Optional[Kategori]:
    """Finn kategori ut ifra class variablen id_"""
    for kategori in lagrede_kategorier:
        if kategori.id_.lower() == id_.lower():
            return kategori
    return None


def sted_fra_id(lagrede_steder: List[Sted], id_: str) -> Optional[Sted]:
    """Finn sted ut ifra class variablen id_"""
    for sted in lagrede_steder:
        if sted.id_.lower() == id_.lower():
            return sted
    return None


def les_avtaler_fra_fil(lagrede_kategorier: List[Kategori],
                        lagrede_steder: List[Sted]) -> List[Avtale]:
    """Les inn alle avtaler fra fil og returner i liste"""

    avtaler = []
    with open("avtale_liste.json", "r", encoding='utf8') as json_fil:
        try:
            json_data = json.load(json_fil)

            # Det er trygt å anta at typene til
            # variablene er korrekt pga. vi skriver
            # bare gyldig "avtaler" til filen
            for avtale_json in json_data:
                tittel = avtale_json["tittel"]

                # Vi har allerede lastet inn steder-objektene og kan derfor
                # hente Sted-objektet fra metoden sted_fra_id
                # Det samme gjelder kategori!
                sted = sted_fra_id(lagrede_steder, avtale_json["sted"]["id_"])

                start = datetime.fromisoformat(avtale_json["start"])
                varighet = int(avtale_json["varighet"])

                kategorier = []
                for kategori_json in avtale_json["kategorier"]:
                    kategori = kategori_fra_id(lagrede_kategorier, kategori_json["id_"])
                    kategorier.append(kategori)

                ny_avtale = Avtale(tittel, sted, start, varighet, kategorier)
                avtaler.append(ny_avtale)
        except ValueError:
            print("Feil ved innhenting av json data, er avtale_liste.json tom?")

        return avtaler


# -----------------------------------------------------------
#                     Oppgave j
# -----------------------------------------------------------
def alle_avtaler_paa_dato(avtaler: List[Avtale], dato: datetime):
    """Returner alle avtale på bestemt dato"""
    avtaler_paa_dato = []
    for avtale in avtaler:
        if avtale.start == dato:
            avtaler_paa_dato.append(avtale)
    return avtaler_paa_dato


# -----------------------------------------------------------
#                     Oppgave k
# -----------------------------------------------------------

def sok_etter_avtale(avtaler: List[Avtale], soke_ord_liste: List[str]):
    """Søk etter en avtale i en liste"""

    sok_resultat = []
    for avtale in avtaler:

        # Gjør søket ufølsomt mot små/store bokstaver
        avtale_tittel = avtale.tittel.lower()

        # Lag en kopi av soke ordene
        soke_ord_liste_kopi = soke_ord_liste.copy()
        for soke_ord in soke_ord_liste:
            if soke_ord in avtale_tittel:
                soke_ord_liste_kopi.remove(soke_ord)

            # Dersom soke_ord_liste_kopi er tom er søket fullført
            if not soke_ord_liste_kopi:
                sok_resultat.append(avtale)
                continue

    return sok_resultat


# -----------------------------------------------------------
#                     Oppgave l, m, n, o
# -----------------------------------------------------------


def rediger_avtale(avtale: Avtale, lagrede_steder: List[Sted]):
    """Rediger en avtale"""

    valg = input("""[1] Endre tittel
[2] Endre sted
[3] Endre start
[4] Endre varighet
Velg en operasjon # """)

    if valg == "1":
        ny_tittel = input(f"Skriv inn en ny tittel for avtalen '{avtale.tittel}' # ")
        avtale.tittel = ny_tittel

    elif valg == "2":
        # velg_eller_lag_ny_sted kan av og til returnere None!
        ny_sted = velg_eller_lag_ny_sted(lagrede_steder)
        if isinstance(ny_sted, Sted):
            avtale.sted = ny_sted

    elif valg == "3":
        start = input(f"Skriv inn en ny start-tid for avtalen '{avtale.tittel}' 'ÅÅÅÅ-MM-DD HH:MM:SS' # ")

        # Gjør om str til datetime
        try:
            ny_start = datetime.fromisoformat(start)
            avtale.start = ny_start
        except ValueError:
            print("Dato-formatet du oppgav ble ikke gjenkjent, bruk 'ÅÅÅÅ-MM-DD HH:MM:SS'")

    elif valg == "4":
        vargihet = input(f"Skriv inn en ny varighet avtalen '{avtale.tittel}' # ")

        try:
            ny_varighet = int(vargihet)
            avtale.varighet = ny_varighet
        except ValueError:
            print("Du oppga ikke en int!")


# -----------------------------------------------------------
#                     Oppgave 10..
# -----------------------------------------------------------

# -----------------------------------------------------------
#                     Oppgave d)
# -----------------------------------------------------------

def lag_ny_kategori() -> Optional[Kategori]:
    """Registrer en ny kategori"""

    id_ = input("Skriv inn kategori id # ")
    navn = input("Skriv inn kategori navn # ")
    prioritet = input("Skriv inn kategori prioritet (1, 2 eller 3) # ")

    # Her må vi sjekke om prioritet == 3 eller prioritet == 2
    # slik at vi kan endre det til svært viktig, viktig, eller vanlig
    # som er default value
    if prioritet == "3":
        prioritet = "SVÆRT VIKTIG"
    elif prioritet == "2":
        prioritet = "VIKTIG"
    else:
        prioritet = "VANLIG"

    return Kategori(id_, navn, prioritet)


# -----------------------------------------------------------
#                     Oppgave e)
# -----------------------------------------------------------

# Vi ønsker å lagre kategorier i egen fil pga. hva skjer dersom
# vi lager en kategori, men ikke legger den i en Avtale? Lagres den da?


def skriv_kategorier_til_fil(kategorier: List[Kategori]) -> None:
    """Skriv liste med kategorier til json fil"""

    json_object = json.dumps(kategorier, indent=4,
                             default=datetime_option, separators=(',', ': '),
                             ensure_ascii=False)

    with open("kategori_liste.json", "w", encoding='utf8') as json_fil:
        json_fil.write(json_object)


def les_kategorier_fra_fil() -> List[Kategori]:
    """Les inn alle kategorier fra fil og returnerer ei liste"""

    kategorier = []
    with open("kategori_liste.json", "r", encoding='utf8') as json_fil:
        try:
            json_data = json.load(json_fil)

            # Det er trygt å anta at typene til
            # variablene er korrekt pga. vi skriver
            # bare gyldig "avtaler" til filen
            for kategori_json in json_data:
                id_ = kategori_json["id_"]
                navn = kategori_json["navn"]
                prioritet = kategori_json["prioritet"]

                kategorier.append(Kategori(id_, navn, prioritet))

        except ValueError:
            print("Feil ved innhenting av json data, er kategori_liste.json tom?")

        return kategorier


# -----------------------------------------------------------
#                     Oppgave h)
# -----------------------------------------------------------

def lag_ny_sted() -> Optional[Sted]:
    """Lag sted-objekt"""

    id_ = input("Skriv inn sted id # ")
    navn = input("Skriv inn sted navn # ")
    adresse = input("Skriv inn sted adresse # ")
    post_nummer = input("Skriv inn sted post-nummer # ")
    post_sted = input("Skriv inn sted post-sted # ")

    # Her er det realistisk at post_nummer er tall (int)
    # Derfor kan vi like så godt sjekke dette
    try:
        post_nummer_int = int(post_nummer)
    except ValueError:
        print("Du må skrive inn et gyldig tall for post-nummer, for eksempel 0010 !")
        return None

    return Sted(id_, navn, adresse=adresse, post_nummer=post_nummer_int, post_sted=post_sted)


# -----------------------------------------------------------
#                     Oppgave i)
# -----------------------------------------------------------

# Vi ønsker å lagra steder i egen fil pga. hva skjer dersom
# vi lager et sted, men ikke legger den i en Avtale? Lagres den da?


def skriv_steder_til_fil(steder: List[Sted]) -> None:
    """Skriv liste med avtaler til json fil"""

    json_object = json.dumps(steder, indent=4,
                             default=datetime_option, separators=(',', ': '),
                             ensure_ascii=False)

    with open("sted_liste.json", "w", encoding='utf8') as json_fil:
        json_fil.write(json_object)


def les_steder_fra_fil() -> List[Sted]:
    """Les inn alle steder fra fil og returnerer ei liste"""

    steder = []
    with open("sted_liste.json", "r", encoding='utf8') as json_fil:
        try:
            json_data = json.load(json_fil)

            # Det er trygt å anta at typene til
            # variablene er korrekt pga. vi skriver
            # bare gyldig "avtaler" til filen
            for sted_json in json_data:
                sted = Sted(sted_json["id_"],
                            sted_json["navn"],
                            adresse=sted_json["adresse"],
                            post_nummer=sted_json["post_nummer"],
                            post_sted=sted_json["post_sted"])

                steder.append(sted)
        except ValueError:
            print("Feil ved innhenting av json data, er sted_liste.json tom?")

        return steder


# -----------------------------------------------------------
#                     Oppgave l)
# -----------------------------------------------------------

# Objektene lagres allerede som objekter i json...

# -----------------------------------------------------------
#                     Oppgave o)
# -----------------------------------------------------------

def legg_til_kategorier_for_avtale(lagrede_avtaler: List[Avtale],
                                   lagrede_kategorier: List[Kategori]) -> None:
    """Legg til en eller flere kategorier for en avtale"""

    # Dersom det ikke finnes noen avtaler/kategorier skriver vi
    # dette til bruker og går ut av funksjonen
    if not lagrede_avtaler:
        print("Det finnes ingen avtaler")
        return

    if not lagrede_kategorier:
        print("Det finnes ingen registrerte kategorier, lag en ny og prøv igjen!")
        return

    # Skriv ut lagrede avtaler
    skriv_ut_liste(lagrede_avtaler, overskrift="Registrerte avtaler:")

    avtale_indeks = input("Velg indeksen til avtalen du vil legge kategorier i # ")
    try:
        avtale_indeks_int = int(avtale_indeks)

        valgt_avtale = lagrede_avtaler[avtale_indeks_int]
    except IndexError:
        print(f"1 Det fantes ingen avtaler med indeksen du oppga!")
        return
    except ValueError:
        print("Du oppga ikke en int!")
        return

    # Skriv ut lagrede kategorier
    skriv_ut_liste(lagrede_kategorier, overskrift="Registrerte kategorier:")

    # Vi forventer at kategori_indekser ser slikt ut "1,2,3" som betyr
    # at brukeren vil velge kategoriene med indeksene 1, 2, og 3.
    # For å få dette som en liste bruker vi .split(",")
    # Dermed kan vi bruke en loop og legge til kategoriene i avtalen dersom de eksisterer
    kategori_indekser = input("Skriv inn hvilke kategorier du vil legge til avtalen slik '1,2,3' # ").split(",")

    # Først må vi loope igjennom alle indeksene i kategori_indekser
    # Så må vi hente kategorien i listen med gitt indeks
    for indeks in kategori_indekser:
        try:
            ny_kategori = lagrede_kategorier[int(indeks)]
            valgt_avtale.legg_til_kategori(ny_kategori)
        except ValueError:
            print(f"{indeks} er ikke en int!")
        except IndexError:
            print(f"Det finnes ingen registrerte kategori med indeks {indeks}")


# -----------------------------------------------------------
#                     Oppgave p)
# -----------------------------------------------------------

def finn_avtaler_paa_sted(lagrede_avtaler: List[Avtale],
                          lagrede_steder: List[Sted]) -> None:
    """
    Finn alle avtaler som er på et bestemt
    sted og skriv dem ut til bruker
    """

    # Skriv ut lagrede steder
    skriv_ut_liste(lagrede_steder, overskrift="Registrerte steder:")
    sted_navn = input("Oppgi et sted-navn # ").lower()

    avtaler = []
    for avtale in lagrede_avtaler:
        if avtale.sted.navn.lower() == sted_navn:
            avtaler.append(avtale)

    skriv_ut_liste(avtaler, f"Alle avtaler på {sted_navn}")


# -----------------------------------------------------------
#                     Meny system
# -----------------------------------------------------------

def kjor_meny_system():
    lagrede_avtaler = []
    lagrede_steder = []
    lagrede_kategorier = []
    ulagret = False

    while True:
        valg = input("""[1] Lese inn avtaler fra fil
[2] Skrive avtalene til fil
[3] Lag ny avtale
[4] Skrive ut alle avtalene
[5] Rediger en avtale
[6] Slett en avtale
[7] Lag ny kategori
[8] Lag ny sted
[9] Legg til kategorier i en avtale
[10] Finn avtaler på bestemt sted
[11] Avslutt
Velg en operasjon # """)

        if valg == "1":
            # Spør om bekfreftelse før vi leser inn dersom lagrede_avtaler ikke er tom
            if lagrede_avtaler:
                bekreftelse = input("Vil du overskrive avtaler (Ja/Nei) # ").lower()
                if bekreftelse == "ja":
                    lagrede_kategorier = les_kategorier_fra_fil()
                    lagrede_steder = les_steder_fra_fil()
                    lagrede_avtaler = les_avtaler_fra_fil(lagrede_kategorier,
                                                          lagrede_steder)
            else:
                lagrede_kategorier = les_kategorier_fra_fil()
                lagrede_steder = les_steder_fra_fil()
                lagrede_avtaler = les_avtaler_fra_fil(lagrede_kategorier,
                                                      lagrede_steder)

        elif valg == "2":
            skriv_avtaler_til_fil(lagrede_kategorier,
                                  lagrede_steder,
                                  lagrede_avtaler)
            ulagret = False

        elif valg == "3":
            ny_avtale = lag_ny_avtale(lagrede_steder)
            if isinstance(ny_avtale, Avtale):
                lagrede_avtaler.append(ny_avtale)
                ulagret = True

        elif valg == "4":
            skriv_ut_liste(lagrede_avtaler, overskrift=input("Skriv inn overskrift # "))

        elif valg == "5":
            skriv_ut_liste(lagrede_avtaler, overskrift="Alle avtaler:")

            valgt_indeks = input("Velg indeksen til avtalen du vil redigere # ")
            try:
                valgt_indeks_int = int(valgt_indeks)

                valgt_avtale = lagrede_avtaler[valgt_indeks_int]
                rediger_avtale(valgt_avtale, lagrede_steder)
                ulagret = True

            except ValueError:
                print("Du oppga ikke en int!")

        elif valg == "6":
            skriv_ut_liste(lagrede_avtaler, overskrift="Alle avtaler:")

            valgt_indeks = input("Velg indeksen til avtalen du vil slette # ")
            try:
                valgt_indeks_int = int(valgt_indeks)

                del lagrede_avtaler[valgt_indeks_int]
                ulagret = True
            except IndexError:
                print(f"3 Det fantes ingen avtaler med indeksen du oppga!")
            except ValueError:
                print("Du oppga ikke en int!")

        elif valg == "7":
            ny_kategori = lag_ny_kategori()
            if isinstance(ny_kategori, Kategori):
                lagrede_kategorier.append(ny_kategori)
                ulagret = True

        elif valg == "8":
            ny_sted = lag_ny_sted()
            if isinstance(ny_sted, Sted):
                lagrede_steder.append(ny_sted)
                ulagret = True

        elif valg == "9":
            legg_til_kategorier_for_avtale(lagrede_avtaler, lagrede_kategorier)

        elif valg == "10":
            finn_avtaler_paa_sted(lagrede_avtaler, lagrede_steder)

        elif valg == "11":
            if ulagret:
                lagre_valg = input("Vil du lagre ? (Ja/Nei) ").lower()
                if lagre_valg == "ja":
                    skriv_avtaler_til_fil(lagrede_kategorier,
                                          lagrede_steder,
                                          lagrede_avtaler)
            break


if __name__ == '__main__':
    kjor_meny_system()
