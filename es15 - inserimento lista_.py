lista_numeri_utente = []
somma = 0
prodotto = 1
risposta_utente = input("Inserisci un numero o scrivi 'FINITO': ")
while risposta_utente != "FINITO":
    lista_numeri_utente.append(int(risposta_utente))
    risposta_utente = input("Inserisci un numero o scrivi 'FINITO': ")
for elemento in lista_numeri_utente:
    somma += elemento
    prodotto *= elemento
print(f"La somma é {somma} e il prodotto é {prodotto}")
#lista_numeri_utente è una lista vuota
#risposta_utente è l'utente che inserisce un numero alla volta fino a quando non scrive FINITO