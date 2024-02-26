import time
from igrac import Igrac
import os

from rulet import Rulet


def iscrtaj_rulet() -> None:
    roulette_str = """
    ]  3  6  9  12  15  18  21  24  27  30  33  36  
     0  2  5  8  11  14  17  20  23  26  29  32  35
    ]  1  4  7  10  13  16  19  22  25  28  31  34
    """

    colored_str = ""
    for line in roulette_str.split("\n"):
        if line.strip():
            if line.startswith(" "):
                colored_str += " "
            elements = line.split()
            colored_line = ""
            for element in elements:
                if element.isdigit():
                    number = int(element)
                    if number == 0:
                        colored_line += (
                            "\033[92m" + element + "\033[0m"
                        )  # Green color for 0
                    elif number % 2 == 0:
                        colored_line += (
                            "\033[97m" + element + "\033[0m"
                        )  # White color for even numbers
                    else:
                        colored_line += (
                            "\033[91m" + element + "\033[0m"
                        )  # Red color for odd numbers
                else:
                    colored_line += element
                colored_line += " "
            colored_str += colored_line.rstrip() + "\n"
        else:
            colored_str += "\n"

    print(colored_str)


igrac = Igrac("Rade Majstor")
rulet = Rulet(igrac)

while True:
    print("-------------------")
    print("Igrac: " + igrac.name)
    print("-------------------")
    print("Vas kredit: " + str(igrac.racun))
    print("-------------------")
    print("Vas ulog: " + str(igrac.ulog.iznos))
    print("-------------------")
    print(
        "Igrani brojevi: "
        + str(list(map(lambda slot_ulog: slot_ulog.broj, igrac.ulog.igrani_brojevi)))
    )
    iscrtaj_rulet()
    print("-------------------\n")
    print("Unesite ZAVRTI da pokrenete rulet")
    print("-------------------\n")

    #### ULAGANJE
    while True:
        broj = input("Unesite broj: ")

        if broj.isdigit() and int(broj) >= 0 and int(broj) <= 36:
            broj = int(broj)
            while True:
                ulog_unos = input("Unesite ulog: ")

                if ulog_unos.isdigit():
                    ulog_unos = int(ulog_unos)
                    if ulog_unos > igrac.racun:
                        print("Nemate dovoljno kredita!")
                        continue
                    else:
                        igrac.ulozi(ulog_unos, broj)
                        break
                else:
                    print("Unos nije broj!")
                    continue
        elif broj == "ZAVRTI":
            izvuceni_slot = rulet.zavrti()
            print("--------------\n")
            print(
                "Izvucen je broj "
                + str(izvuceni_slot.broj)
                + ", boja "
                + izvuceni_slot.boja.name
            )
            igrac.obracunaj_rezultat(izvuceni_slot.broj)
            time.sleep(5)
        else:
            print("Unos nije broj!")
            continue

        os.system("cls")
        break
    #####################
