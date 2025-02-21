print("Vuoi la fanta, il rum o la cocacola?")
bevanda_utente = input()

match bevanda_utente:
    case "fanta" | "aranciata":
        print("Vado in cucina a prendere la fanta e torno subito")
    case "rum":
        print("Ti verso subito il rum dato che l'ho giá qui")
    case "cocacola":
        print("Mi spiace ma ho finito la cocacola")
    case _:
        print(f"Non ho capito, non abbiamo {bevanda_utente}")

#SHIFT + TAB <-
#TAB         ->


#swicth è un caso particolare perchè sottintende un if,
#prendere la risposta dell'utente e confrontarla con le possibilità che gli diamo
#prendo la risposta dell'utente e controllo se mi ha scritto: fanta, coca o rum
#se non mi ha scritto nulla delle possibilità posso mettere case_: