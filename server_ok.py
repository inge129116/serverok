import sys
import json

def add_server(nieuwe_server):
    print(f"{nieuwe_server} toevoegen")
    servers.append(nieuwe_server)
    try:
        with open("servers.json","w") as f:
            json.dump(servers,f)
    except:
        print("servers.json niet gevonden" )
        
def delete_server(oude_server):
    print(f"{servers.pop(int(oude_server))} verwijderen")
    
    try:
        with open("servers.json","w") as f:
            json.dump(servers,f)
    except:
        print("servers.json niet gevonden" )

def showlist():
    for server in enumerate(servers):
            print(server)
    

def run_cli(args):
    match args[0]:
        case "1": #json overschrijven
            add_server(args[1])
        case "2": #json overschrijven
            delete_server(args[1])
        case "3":
            showlist()

def run_int():
    
    while(True):
        optie = input("geef het getal van jou keuze: \n0. stoppen\n1. toevoegen \n2. verwijderen \n3. lijst tonen \n")
        print(f"je hebt gekozen voor optie {optie}")
        match optie:
            case "1": 
                
                add_server(input("geef de url van de server: "))
                
            case "2": 
                
                delete_server(input("geef de nummer van de server die je wil verwijderen"))
                
            case "3":
                showlist() #enumerate
            case "0":
                sys.exit(0)

 #servers list moet uit json file met try expect en json niet in git servers.json in git ignore
try:
    with open("servers.json","r") as f:
        servers = json.load(f)
except:
        servers = []
        print("servers.json niet gevonden" )
try:
    with open("checks.json","r") as f:
        checks = json.load(f)
except:
        checks = []
        print("checks.json niet gevonden" )

if len(sys.argv) >= 2:
    run_cli(sys.argv[1:])
else:
    run_int()
