from igrac import Igrac
from slot import Slot
import random
import time


class Rulet:
    def __init__(self, igrac: Igrac) -> None:
        self.igrac = igrac
        self.slotovi: list[Slot] = []

        for i in range(0, 37):
            slot = Slot(i)
            self.slotovi.append(slot)

    def zavrti(self) -> Slot:
        print("Loptica se vrti...")
        time.sleep(5)
        izvuceni_slot = random.choice(self.slotovi)

        return izvuceni_slot
