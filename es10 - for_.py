#STAMPARE TUTTI I NUMERI DA 1 A CIÓ CHE DICE L'UTENTE

limite = int(input("Inseerisci il numero positivo fino al quale vuoi che conti: "))

for i in range(1, limite+1, 1):
    print(i)
    if i%2 == 1:
        continue
    print("pari")