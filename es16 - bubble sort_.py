lista_numeri_utente = []
risposta_utente = input("Inserisci un numero o scrivi 'FINITO': ")
while risposta_utente != "FINITO":
    lista_numeri_utente.append(int(risposta_utente))
    risposta_utente = input("Inserisci un numero o scrivi 'FINITO': ")

for j in range(0, len(lista_numeri_utente)-1, 1):
    for i in range(0, len(lista_numeri_utente)-1-j, 1):
        #CONTROLLO SE É MAGGIORE DEL SEGUENTE
        if lista_numeri_utente[i] > lista_numeri_utente[i+1]:
            #SE É MAGGIORE LI SCAMBIO
            temp = lista_numeri_utente[i]
            lista_numeri_utente[i] = lista_numeri_utente[i+1]
            lista_numeri_utente[i+1] = temp

print(lista_numeri_utente)
#creo una lista
#quello che mette l'utente lo chiamo: risposta_utente
#finchè la risposta dell'utente è diversa da: FINITO resta nel ciclo del while, inoltre ogni
#numero che inserisce viene salvato nella lista_numeri_utente
#siccome ho bisogno che mi SALVI ogni numero inserito dall'utente devo creare
#.APPEND nella lista_numeri_utente perchè voglio che mi salvi TUTTI i numeri 
#che inserisce fino alla parola FINITO
#il fatto di ripetere 2 volte l'input della risposta_utente mi permette di far ripetere l'inserimento
#dei numeri ogni volta dall'utente