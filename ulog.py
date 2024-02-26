class SlotUlog:
    def __init__(self, broj, iznos):
        self.broj: int = broj
        self.iznos: int = iznos


class Ulog:
    def __init__(self):
        self.iznos = 0
        self.igrani_brojevi: list[SlotUlog] = []
