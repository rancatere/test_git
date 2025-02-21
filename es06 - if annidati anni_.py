print("Inserisci la tua etá:")
anni_utente = int(input())

if anni_utente >= 18:
    print("Sei maggiorenne")
    print("Vuoi la fanta, il rum o la cocacola?")
    bevanda_utente = input()
    if bevanda_utente == "fanta":
        print("Vado in cucina a prendere la fanta e torno subito")
    elif bevanda_utente == "rum":
        print("Ti verso subito il rum dato che l'ho giá qui")
    elif bevanda_utente == "cocacola":
        print("Mi spiace ma ho finito la cocacola")
    else:
        print(f"Non ho capito, non abbiamo {bevanda_utente}")
else:
    print("Sei minorenne")

print("fine programma")

