class Pojisteny:

    def __init__(self, krestni_jmeno, prijmeni, telefon, vek):
        self.krestni_jmeno = krestni_jmeno
        self.prijmeni = prijmeni
        self.telefon = telefon
        self.vek = vek

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.krestni_jmeno, self.prijmeni, self.telefon, self.vek)
