while True:
    lato1 = int(input("Inserisci lato 1: "))
    lato2 = int(input("Inserisci lato 2: "))
    lato3 = int(input("Inserisci lato 3: "))
    if lato1<0:
        print("Errore: Lato 1 é minore di 0, mettilo positivo.")
        continue;
    if lato2<0:
        print("Errore: Lato 2 é minore di 0, mettilo positivo.")
        continue;
    if lato3<0:
        print("Errore: Lato 3 é minore di 0, mettilo positivo.")
        continue;
    if lato1 + lato2 < lato3:
        print("Errore: La somma di lato 1 e lato 2 é minore di lato 3.")
        continue;
    if lato1 + lato3 < lato2:
        print("Errore: La somma di lato 1 e lato 3 é minore di lato 2.")
        continue;
    if lato3 + lato2 < lato1:
        print("Errore: La somma di lato 2 e lato 3 é minore di lato 1.")
        continue;
    break;

print("Bravo")
#è uno dei modi per fare il DO...WHILE