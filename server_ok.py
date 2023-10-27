import sys

def showlist():
    for server in enumerate(servers):
            print(server)
    

def run_cli(args):
    match args[0]:
        case "1": #json overschrijven
            print("toevoegen")
        case "2": #json overschrijven
            print("verwijderen")
        case "3":
            print("lijst tonen")

def run_int():
    
    while(True):
        optie = input("geef het getal van jou keuze: \n0. stoppen\n1. toevoegen \n2. verwijderen \n3. lijst tonen \n")
        print(f"je hebt gekozen voor optie {optie}")
        match optie:
            case "1": #json overschrijven
                print("toevoegen")
                server = input("geef de url van de server: ")
                servers.append(server)
            case "2": #json overschrijven
                nummer_server = input("geef de nummer van de server die je wil verwijderen")
                servers.pop(nummer_server)
            case "3":
                showlist() #enumerate bekijken
            case "0":
                sys.exit(0)

servers = [] #moet uit json file met try expect en json niet in git servers.json in git ignore
if len(sys.argv) >= 2:
    run_cli(sys.argv[1:])
else:
    run_int()
