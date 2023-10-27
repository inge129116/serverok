import sys

def run_cli(args):
    match args[0]:
        case "1":
            print("toevoegen")
        case "2":
            print("verwijderen")
        case "3":
            print("lijst tonen")

def run_int():
    
    while(True):
        optie = input("geef het getal van jou keuze: \n0. stoppen\n1. toevoegen \n2. verwijderen \n3. lijst tonen \n")
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

if len(sys.argv) >= 2:
    run_cli(sys.argv[1:])
else:
    run_int()
