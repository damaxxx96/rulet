from ulog import SlotUlog, Ulog


class Igrac:
    def __init__(self, name: str) -> None:
        self.name = name
        self.racun = 3000
        self.ulog = Ulog()

    def ulozi(self, novi_ulog: int, igrani_broj: int) -> None:
        self.racun -= novi_ulog
        self.ulog.iznos += novi_ulog
        slot_ulog = SlotUlog(igrani_broj, novi_ulog)
        self.ulog.igrani_brojevi.append(slot_ulog)

    def obracunaj_rezultat(self, rezultat: int) -> None:
        pogodjen = False

        for slot_ulog in self.ulog.igrani_brojevi:
            if rezultat == slot_ulog.broj:
                dobitak = slot_ulog.iznos * 36
                self.racun += dobitak
                pogodjen = True
                break

        if pogodjen:
            print("Pogodjen broj!!!")
            print("Dobitak: " + str(dobitak))
        else:
            print("Promasen broj!")
            print("Gubitak: " + str(self.ulog.iznos))

        self.ulog = Ulog()
