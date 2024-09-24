from backend import *
import os
from colorama import Fore, Style, init

# Initialize colorama for color usage in terminal
init(autoreset=True)

# Function to clear the screen for a cleaner UI
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print a visually appealing menu
def printMeny():
    clear_screen()

    # Menu Header
    print(Fore.CYAN + Style.BRIGHT + "╔═══════════════════════════════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + Fore.YELLOW + "                  🌟 Kalkulator 🌟                   " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚═══════════════════════════════════════════════════╝")

    # Menu Options
    print(Fore.CYAN + "╔═══════════════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.GREEN + "  1. ➕  Legg sammen (pluss)                       " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "  2. ➖  Trekk fra   (minus)                       " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "  3. ✖️  Gange                                   " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + "  4. ➗  Dele                                    " + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.RED   + "  5. ❌  Avslutt                                 " + Fore.CYAN + "║")
    print(Fore.CYAN + "╚═══════════════════════════════════════════════════╝")

    # Input Prompt
    menyvalg = input(Fore.YELLOW + "✨ Velg operasjon fra menyen (1-5): " + Fore.RESET)
    utfoerMenyvalg(menyvalg)

# Function to execute menu option based on user input
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
        bekreftelse = input(Fore.RED + "❓ Er du sikker på at du vil avslutte? J/N: " + Fore.RESET)
        if bekreftelse.lower() == "j":
            print(Fore.MAGENTA + "👋 Takk for at du brukte kalkulatoren. Ha en flott dag!" + Fore.RESET)
            exit()
        else:
            printMeny()
    else:
        nyttForsoek = input(Fore.RED + "*** Ugyldig valg. Velg et tall mellom 1-5. Trykk for å fortsette *** " + Fore.RESET)
        printMeny()

# Function to pause and return to menu
def pause_og_fortsett():
    input(Fore.CYAN + "🔄 Trykk en tast for å fortsette..." + Fore.RESET)
    printMeny()

# Start by displaying the menu
printMeny()
