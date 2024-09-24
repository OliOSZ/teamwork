def leggSammen():
    try:
        tall1 = input("Skriv inn første tallet: ")
        tall2 = input("Skriv inn andre tallet: ")
        sum = int(tall1) + int(tall2)
        print(f'{tall1} + {tall2} = {sum}')
    except ValueError:
        print("Feil: Du må skrive inn gyldige heltall.")
        
def trekkFra():
    try:
        tall1 = input("Skriv inn første tallet: ")
        tall2 = input("Skriv inn andre tallet: ")
        diff = int(tall1) - int(tall2)
        print(f'{tall1} - {tall2} = {diff}')
    except ValueError:
        print("Feil: Du må skrive inn gyldige heltall.")

def gange():
    try:
        tall1 = input("Skriv inn første tallet: ")
        tall2 = input("Skriv inn andre tallet: ")
        prod = int(tall1) * int(tall2)
        print(f'{tall1} * {tall2} = {prod}')
    except ValueError:
        print("Feil: Du må skrive inn gyldige heltall.")

def dele():
    try:
        tall1 = input("Skriv inn første tallet: ")
        tall2 = input("Skriv inn andre tallet: ")
        divy = int(tall1) / int(tall2)
        print(f'{tall1} / {tall2} = {divy}')
    except ValueError:
        print("Feil: Du må skrive inn tall. Tulling.")
    except ZeroDivisionError:
        print("Feil: Du kan ikke dele på null. Fjomp.")
