from datetime import datetime
from colorama import init, Fore, Style

# Inicializace barev
init(autoreset=True)

def zapis_do_historie(text):
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    with open("historie.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {text}\n")

def vypis_nadpis():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "               VYLEPŠENÝ PŘEVODNÍK JEDNOTEK")
    print(Fore.CYAN + "=" * 60 + "\n")

def nacti_cislo(dotaz):
    while True:
        try:
            return float(input(dotaz))
        except ValueError:
            print(Fore.RED + "Chyba: Zadej platné číslo.")

# Hlavní program
vypis_nadpis()

while True:
    print(Fore.YELLOW + "Zvol kategorii převodu:")
    print("1 - Teplota (°C ↔ °F)")
    print("2 - Délka (metry ↔ stopy)")
    print("3 - Hmotnost (kg ↔ lb)")
    print("4 - Rychlost (km/h ↔ mph)")
    print("5 - Čas (minuty ↔ sekundy)")
    print("6 - Objem (litry ↔ galony)")
    print("7 - Zobrazit historii")
    print("8 - Zobrazit poslední převod")
    print("0 - Ukončit")
    print("-" * 60)

    volba = input("Zadej volbu (0–8): ")

    if volba == "1":
        smer = input("a - °C → °F\nb - °F → °C\nZadej směr (a/b): ").lower()
        if smer == "a":
            c = nacti_cislo("Zadej teplotu ve °C: ")
            f = (c * 9 / 5) + 32
            vysledek = f"{c} °C = {round(f, 2)} °F"
        elif smer == "b":
            f = nacti_cislo("Zadej teplotu ve °F: ")
            c = (f - 32) * 5 / 9
            vysledek = f"{f} °F = {round(c, 2)} °C"
        else:
            continue
        print(Fore.GREEN + "Výsledek:", vysledek)
        zapis_do_historie("[Teplota] " + vysledek)

    elif volba == "2":
        smer = input("a - metry → stopy\nb - stopy → metry\nZadej směr (a/b): ").lower()
        if smer == "a":
            m = nacti_cislo("Zadej délku v metrech: ")
            ft = m * 3.28084
            vysledek = f"{m} m = {round(ft, 2)} ft"
        elif smer == "b":
            ft = nacti_cislo("Zadej délku ve stopách: ")
            m = ft / 3.28084
            vysledek = f"{ft} ft = {round(m, 2)} m"
        else:
            continue
        print(Fore.GREEN + "Výsledek:", vysledek)
        zapis_do_historie("[Délka] " + vysledek)

    elif volba == "3":
        smer = input("a - kg → lb\nb - lb → kg\nZadej směr (a/b): ").lower()
        if smer == "a":
            kg = nacti_cislo("Zadej hmotnost v kilogramech: ")
            lb = kg * 2.20462
            vysledek = f"{kg} kg = {round(lb, 2)} lb"
        elif smer == "b":
            lb = nacti_cislo("Zadej hmotnost v librách: ")
            kg = lb / 2.20462
            vysledek = f"{lb} lb = {round(kg, 2)} kg"
        else:
            continue
        print(Fore.GREEN + "Výsledek:", vysledek)
        zapis_do_historie("[Hmotnost] " + vysledek)

    elif volba == "4":
        smer = input("a - km/h → mph\nb - mph → km/h\nZadej směr (a/b): ").lower()
        if smer == "a":
            kmh = nacti_cislo("Zadej rychlost v km/h: ")
            mph = kmh * 0.621371
            vysledek = f"{kmh} km/h = {round(mph, 2)} mph"
        elif smer == "b":
            mph = nacti_cislo("Zadej rychlost v mph: ")
            kmh = mph / 0.621371
            vysledek = f"{mph} mph = {round(kmh, 2)} km/h"
        else:
            continue
        print(Fore.GREEN + "Výsledek:", vysledek)
        zapis_do_historie("[Rychlost] " + vysledek)

    elif volba == "5":
        smer = input("a - minuty → sekundy\nb - sekundy → minuty\nZadej směr (a/b): ").lower()
        if smer == "a":
            minuty = nacti_cislo("Zadej čas v minutách: ")
            sekundy = minuty * 60
            vysledek = f"{minuty} min = {int(sekundy)} s"
        elif smer == "b":
            sekundy = nacti_cislo("Zadej čas v sekundách: ")
            minuty = sekundy / 60
            vysledek = f"{sekundy} s = {round(minuty, 2)} min"
        else:
            continue
        print(Fore.GREEN + "Výsledek:", vysledek)
        zapis_do_historie("[Čas] " + vysledek)

    elif volba == "6":
        smer = input("a - litry → galony\nb - galony → litry\nZadej směr (a/b): ").lower()
        if smer == "a":
            l = nacti_cislo("Zadej objem v litrech: ")
            gal = l * 0.264172
            vysledek = f"{l} l = {round(gal, 2)} gal"
        elif smer == "b":
            gal = nacti_cislo("Zadej objem v galonech: ")
            l = gal / 0.264172
            vysledek = f"{gal} gal = {round(l, 2)} l"
        else:
            continue
        print(Fore.GREEN + "Výsledek:", vysledek)
        zapis_do_historie("[Objem] " + vysledek)

    elif volba == "7":
        try:
            print(Fore.CYAN + "\n=== HISTORIE PŘEVODŮ ===")
            with open("historie.txt", "r", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("Žádná historie zatím neexistuje.")
        print("-" * 60)

    elif volba == "8":
        try:
            with open("historie.txt", "r", encoding="utf-8") as f:
                radky = f.readlines()
                if radky:
                    print(Fore.CYAN + "Poslední převod:")
                    print(radky[-1])
                else:
                    print("Historie je prázdná.")
        except FileNotFoundError:
            print("Historie ještě nebyla vytvořena.")

    elif volba == "0":
        print(Fore.YELLOW + "\nDíky za použití programu. Měj se hezky!")
        break

    else:
        print(Fore.RED + "Chybná volba. Zkus to znovu.")
