a=input("metti dividendo")
c=input("metti divisore")

try:
   b=float(a)/int(c)
   print(b) 
except ValueError:
   print("Error")
except ZeroDivisionError:
   print("non posso dividere per zero")
#posso usare anche except quello generale, quindi:
except Exception:
   print("Tutte le altre")
   


   
