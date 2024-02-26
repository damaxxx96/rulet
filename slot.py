from enum import Enum


class Boja(Enum):
    ZELENA = (1,)
    CRNA = (2,)
    CRVENA = (3,)


class Slot:
    def __init__(self, broj: int) -> None:
        self.broj = broj

        if broj == 0:
            self.boja = Boja.ZELENA
        elif broj % 2 != 0:
            self.boja = Boja.CRVENA
        elif broj % 2 == 0:
            self.boja = Boja.CRNA
        else:
            print("Nepostoji taj broj na ruletu!!!")
