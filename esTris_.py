def stampa_griglia(griglia):
    for riga in griglia:
        print(" | ".join(riga))
        print("-" * 9)

def aggiorna_griglia(griglia, riga, colonna, simbolo):
    if griglia[riga][colonna] == " ":
        griglia[riga][colonna] = simbolo
    else:
        print("Questa posizione è già occupata!")

def chiedi_mossa():
    while True:
        try:
            riga = int(input("Inserisci la riga (0-2): "))
            colonna = int(input("Inserisci la colonna (0-2): "))
            if 0 <= riga <= 2 and 0 <= colonna <= 2:
                return riga, colonna
            else:
                print("Devi inserire numeri tra 0 e 2!")
        except ValueError:
            print("Per favore, inserisci numeri validi!")

# Inizio partita
griglia = [[" " for _ in range(3)] for _ in range(3)]
giocatore = "X"

for turno in range(9):  # Massimo 9 turni (griglia piena)
    stampa_griglia(griglia)
    print(f"Tocca al giocatore {giocatore}")
    
    riga, colonna = chiedi_mossa()
    aggiorna_griglia(griglia, riga, colonna, giocatore)
    
    # Cambia turno
    giocatore = "O" if giocatore == "X" else "X"

stampa_griglia(griglia)
print("Partita terminata!")