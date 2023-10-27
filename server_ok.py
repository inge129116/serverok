import sys

if len(sys.argv) >= 2:
    optie = sys.argv[1]
else:
    optie = input("geef het getal van jou keuze: \n0. stoppen\n1. toevoegen1 \n2. verwijderen \n3. lijst tonen \n")
print(f"je hebt gekozen voor optie {optie}")
match optie:
    case "1":
        print("toevoegen")
    case "2":
        print("verwijderen")
    case "3":
        print("lijst tonen")
    case "0":
        sys.exit(0)