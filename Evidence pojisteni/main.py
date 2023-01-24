from pojisteny import Pojisteny
from seznam import Seznam

pojistene_osoby = []
seznam = Seznam()
menu = True

while menu:
    print("********************\nEvidence pojistenych\n********************\n")
    vyber = input("Vyberte moznost:\n"
                  "1 - Pridat novy zaznam.\n"
                  "2 - Vypis vsech pojistenych osob.\n"
                  "3 - Vyhledat pojistenou osobu.\n"
                  "4 - Konec.\n")
    print()
    if vyber == "1":
        krestni_jmeno = input("Zadejte krestni jmeno pojisteneho:\n")
        prijmeni = input("Zadejte prijmeni pojisteneho:\n")
        telefon = input("Zadejte telefon pojisteneho:\n")
        vek = input("Zadejte vek pojisteneho:\n")
        novy_zaznam = Pojisteny(krestni_jmeno, prijmeni, telefon, vek)
        pojistene_osoby.append(novy_zaznam.__str__())
        print()
        input("Zaznam byl ulozen. Pokracujte stisknutim libovolne klavesy.\n")
    elif vyber == "2":
        seznam.zaznamy(pojistene_osoby)
        print()
        input("Pokracujte stisknutim libovolne klavesy.\n")
    elif vyber == "3":
        seznam.najdi_zaznam(pojistene_osoby)
        input("Pokracujte stisknutim libovolne klavesy.\n")
    elif vyber == "4":
        menu = False
        print()
        print("Dekujeme za pouziti nasi aplikace. Mejte pekny den!\n")
    else:
        input("Zadana hodnota je nespravna. Pokracujte stisknutim libovolne klavesy.\n")