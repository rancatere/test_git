import math
print(f"{math.ceil(2.102) =}")
print(f"{math.floor(4.02) =}")


print(f"rount(1.5) = {round(1.5)}")
print(f"rount(2.5) = {round(2.5)}")
print(f"rount(3.5) = {round(3.5)}")
print(f"rount(4.5) = {round(4.5)}")
print(f"rount(5.5) = {round(5.5)}")

print(round(253.932845, ndigits=2))
print(round(253932845, ndigits=-5))


print("un' \"anguria\"")
#se inizio una stringa con i " dovrò terminarla con i ", non posso usare
#nella stringa i " posso usare all'interno dei " quanti ' voglio
#posso anche iniziare una stringa con gli apici singoli ovvero '
#utilizzando \ (=escape) dice a python che il carattere subito dopo
#è solo del testo

print('un\'anguria')
print('sto per fare il carattere di escape -> \\ <- ho appena fatto il carattere di escape')
#utilizzo due volte lo slash per usare l'escape \\

#è possibile anche fare in questo modo la round:
print(f"{round(1.5) = }")
print(f"{round(2.5) = }")
print(f"{round(3.5) = }")
print(f"{round(4.5) = }")
print(f"{round(5.5) = }")

print(f"{round(253.932845, ndigits=2) = }")
print(f"{round(253932845, ndigits=-5) = }")

print(f"{2/3 = }")
#stampa 2/3 = 0.6666666666666666
#per formattarlo faccio così:
print(f"{2/3: .2f}")





a=2/3
print(f"{a: .2f}")
print(a)
#per cambiare il valore di a (la variabile) dovrò fare così:
a=round(a, ndigits=2)
print(a)

