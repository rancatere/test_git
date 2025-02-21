figura = input("Che figura vuoi disegnare? (Quadrato, Rettangolo, Triangolo): ").upper()
carattere = input("Di che carattere vuoi che sia formata la figura? (inserire un solo carattere): ")
if len(carattere)!=1:
    print("Errore, avevo detto di mettere un solo carattere :c")
    exit()

match figura:
    case "QUADRATO" | "Q":
        lato = int(input("Inserisci il lato del quadrato: "))
        for i in range(lato):
            print(carattere*lato)
    case "RETTANGOLO" | "R":
        base = int(input("Inserisci la base del rettangolo: "))
        altezza = int(input("Inserisci l'altezza del rettangolo: "))
        for i in range(altezza):
            print(carattere*base)
    case "TRIANGOLO" | "T":
        altezza = int(input("Inserire altezza triangolo : "))
        for i in range(altezza):
            numero_di_spazi = altezza-i-1
            numero_di_caratteri = i*2+1
            #print(f"i: {i} spazi:{numero_di_spazi} caratteri: {numero_di_caratteri}")
            for j in range(numero_di_spazi):
                print(" ", end="")
            for j in range(numero_di_caratteri):
                print(carattere, end="")
            print("")
    case _:
        print("Risposta non valida")

#anche qui abbiamo usato oppure: |  ovvero se l'utente mi scrive:
#QUADRATO oppure Q (può scrivere solo q e identifica quadrato)
#.upper() mi rende MAIUSCOLO quello che mi inserisce l'utente, così posso
#effettuare il controllo solo sulle maiuscole
#in pratica se mi scrive con iniziale grande poi tutto piccolo, oppure tutto piccolo, oppure un mix
#non mi interessa perchè io trasformo tutto in grande e guardo solo se mi scrive
#le possibilità che gli ho dato: quadrato, rettangolo e triangolo.
