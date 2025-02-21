#es1_data una lista di numeri filtrare e stampare a video quelli maggiori di 0 (usando anche la funzione lambda)

















#es2_data una lista variegata di numeri e stringhe tenere solamente i numeri e stamparli in ordine decrescente
















#es3_data una lista di numeri a 4 cifre stamparli in ordine, se ho 0001, 1234, 9876 devo considerarli ribaldando l'ordine dei numeri in ogni numero, stamparli dal più piccolo al più grande.
#ciao oaic 1234 4321 usando funzioni lambda

lista= [1253, 6178, 9298]
def numero_stringa(numero):
    return numero==str(numero) and numero [::1]

ricerca=list(lambda numero: numero==str(numero) and numero [::1], lista)
print(ricerca)


#numero=1253
#numero1=str(numero)
#numero1_capovolto=numero1 [::-1]
#print(numero1_capovolto)



















#es4_data una lista di dizionari contenente dei dati su dei file (data da thomas) creare un programma che permetta
#in base al nome, al percorso o al peso.  (menù di scelte opzionali)