import sys
import json
from ping3 import ping
import datetime
from bs4 import BeautifulSoup


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

def check_ping():
    #deze check werkt enkel als de server ping toe staat!
    #bestand wordt in map waar jij staat geplaatst niet map van programma!
    for server in servers:
        
        answer = ping(server)
        if answer == None:
            up = "down"
        else:
            up = "up"
        checks.append(f"time: {datetime.datetime.now()} {server}:{up}")
    print(checks)
    web_page(checks)
    try:
        with open("checks.json","w") as f:
            json.dump(checks,f)
            print("bestand aangevuld")
    except:
        print("checks.json niet gevonden" )

def web_page(content_to_add):
    with open("template.html", "r") as html_file:
    # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_file, "html.parser")
    target_div = soup.find("div", id="checks")
    print("start web page")
    for item in content_to_add:
        new_element = BeautifulSoup("\n <p>"+item , "html.parser")
        target_div.extend(new_element)
    with open("index.html", "w") as html_file:
        html_file.write(str(soup))
    #with open("index.html", "a") as html_file:
    # schrijf de inhoud van de lijst naar de html file
    #    for line in checks:
    #        html_file.write("<p>"+line +"<\p> \n")
    #        print("Content added to index.html")

    

def run_cli(args):
    match args[0]:
        case "1": #json overschrijven
            add_server(args[1])
        case "2": #json overschrijven
            delete_server(args[1])
        case "3":
            showlist()
        case "4":
            check_ping()

def run_int():
    
    while(True):
        optie = input("geef het getal van jou keuze: \n0. stoppen\n1. toevoegen \n2. verwijderen \n3. lijst tonen \n4. ping check \n")
        print(f"je hebt gekozen voor optie {optie}")
        match optie:
            case "1": 
                
                add_server(input("geef de url van de server: "))
                
            case "2": 
                
                delete_server(input("geef de nummer van de server die je wil verwijderen"))
                
            case "3":
                showlist() #enumerate

            case "4":
                check_ping()
            case "0":
                sys.exit(0)

def run_checks():
    while(True):
        check_optie = input("geef het getal van jou keuze: \n0. stoppen\n1. ping check \n")
        print(f"je hebt gekozen voor optie {check_optie}")
        match check_optie:
            case "1": 
                check_ping()    
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
    modus = input("wil u dit in managment of check modus uitvoeren (standaart check) ")
    if modus == "managment":
        run_int()
    else:
        run_checks()
        
