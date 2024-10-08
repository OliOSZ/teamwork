from backend import *
import os
from colorama import Fore, Style, init

# starter colorama
init(autoreset=True)

# gjør skjermen klar og clean
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# legger til colorama for at de skal se bra ut
def printMeny():
    clear_screen()

    # Menu top
    print(Fore.CYAN + Style.BRIGHT + "╔═══════════════════════════════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + "                  🌟 Kalkulator 🌟                 " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚═══════════════════════════════════════════════════╝")

    # Meny
    print(Fore.CYAN + "╔═══════════════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.GREEN + "  1. ➕  Legg sammen (pluss)                       " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "  2. ➖  Trekk fra   (minus)                       " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "  3. ✖️   Gange                                     " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "  4. ➗  Dele                                      " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.RED   + "  5. ❌  Avslutt                                   " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚═══════════════════════════════════════════════════╝")

    # Input 
    menyvalg = input(Fore.YELLOW + "✨ Velg hva du vil regne med som du ikke kan bruke det lille hjernen din til jævla firkantfjes (1-5): " + Fore.RESET)
    utfoerMenyvalg(menyvalg)

# følger brukerens input
def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        leggSammen()
        pause_og_fortsett()
    elif valgtTall == "2":
        trekkFra()
        pause_og_fortsett()
    elif valgtTall == "3":
        gange()
        pause_og_fortsett()
    elif valgtTall == "4":
        dele()
        pause_og_fortsett()
    elif valgtTall == "5":
        bekreftelse = input(Fore.RED + "❓Vil du avslutte brur? J/N: " + Fore.RESET)
        if bekreftelse.lower() == "j":
            print(Fore.MAGENTA + "OK, fuck off da, det er ikke noa galt i å være en liten bitch" + Fore.RESET)
            exit()
        else:
            printMeny()
    else:
        nyttForsoek = input(Fore.RED + "*** Ugyldig valg din dumme faen. Velg et tall mellom 1-5 og faenmeg gjør det, dette er ikke rakettforskning. Trykk for å fortsette *** " + Fore.RESET)
        printMeny()

# pauser og returnerer til menyen
def pause_og_fortsett():
    input(Fore.CYAN + "🔄 Trykk en tast for å fortsette. eller ikke. ditt valg, ikke mitt..." + Fore.RESET)
    printMeny()

# viser menyen
printMeny()
