import math 
print('inserisci numeri che vuoi usare e poi scrivi esci')
lista = []
numero=True
while numero :
    valori=input()
    if type(valori)==int or type(valori)==float :  
        lista.append(valori)
        print('sono qui')
    if type(valori )== str:
        if valori== "esci":
            #lista.pop()
            numero = False
       


print(f'questa è la tua lista {lista}')  
