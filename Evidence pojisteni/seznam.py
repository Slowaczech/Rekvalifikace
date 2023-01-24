class Seznam:

    @staticmethod
    def zaznamy(pojistene_osoby):
        for osoba in pojistene_osoby:
            print(osoba)

    @staticmethod
    def najdi_zaznam(pojistene_osoby):
        krestni_jmeno_pojisteneho = input("Zadejte krestni jmeno pojisteneho:\n")
        prijmeni_pojisteneho = input("Zadejte prijmeni pojisteneho:\n")
        print()
        for osoba in pojistene_osoby:
            if krestni_jmeno_pojisteneho in osoba and prijmeni_pojisteneho in osoba:
                print(osoba.__str__(), "\n")
            else:
                print("Tato osoba neni v databazi.")
                print()
