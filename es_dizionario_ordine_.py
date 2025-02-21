print("Inserisci lista utenti")
lista=[]
while True:
    utente1 = {
    'nome':0,
    'cognome':0,
    'anno':0,
    'frutto':0
}
    for chiave in utente1.keys():
         print(f"Inserisci {chiave}")
         utente1[chiave]=input()
    lista.append(utente1)
    scelta = input("Vuoi continuare?")
    if scelta == "si":
          continue
    else:
          break
print(lista)

lista_temporanea=[]
for el in lista:
     lista_temporanea.append(el['nome'])
     lista_temporanea.append(el['cognome'])
print(f"{lista_temporanea}")
lista_temporanea.sort()
print(f"{lista_temporanea}")




#non funziona perchè bisogna creare un unica scatola di variabili temporanee e quindi un unica lista di temporanee comprendente sia i nomi che i cognomi
#possiamo fare in due modi: lista nella lista (nome,nome,nome[cognome,cognome]) oppure concatenare nome&cognome, nome&cognome,

#lista_temporanea_2=[]
#for el in lista:
#     lista_temporanea_2.append(el['cognome'])
#print(f"{lista_temporanea_2}")
#lista_temporanea_2.sort()
#print(f"{lista_temporanea_2}")
#if el['cognome'] == el['cognome']:
#     print(el['nome'])
#else:
#     print(el['cognome'])
     






     





#print(lista[0].get('nome'))



