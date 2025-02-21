print("Inserisci un numero: ")
numero = int(input())

if numero % 2 == 0:
    print("pari")
else:
    print("dispari")


if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
elif numero == 0:
    print("zero")
else:
    print("altro?")