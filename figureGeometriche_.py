import math



figura = ""
while figura != "q" and figura != "quadrato" and figura != "triangolo" and figura != "rettangolo" and figura != "r" and figura != "t":
    print("Che figura geometrica vuoi disegnare? (Rettangolo, Quadrato, Triangolo) ", end ="")
    figura = input()

    match figura.lower().strip():
        case "quadrato" | "q":
            lato = ""
            while not(str(lato).isdigit()) or int(lato) < 1:
                print("Di quanto vuoi il lato? ", end ="")
                lato = input()
                if not(str(lato).isdigit()) or int(lato) < 1:
                    print("Errore, inserire un lato valido!")
                else:
                    lato = int(lato)
                    sim = ""
                    while len(sim) < 1:
                        print("Che simbolo vuoi usare per disegnarlo? ", end ="")
                        sim = input()
                        if len(sim) < 1:
                            print("Errore, inserire un simbolo valido!")
                        else:
                            for i in range(0, lato, 1):
                                for j in range(0, lato, 1):
                                    print(sim, end="")
                                print("")

        case "rettangolo" | "r":
            base = ""
            while not(str(base).isdigit()) or int(base) < 1:
                print("Di quanto vuoi la base? ", end ="")
                base = input()
                if not(str(base).isdigit()) or int(base) < 1:
                    print("Errore, inserire una base valida!")
                else:
                    base = int(base)
                    altezza = ""
                    while not(str(altezza).isdigit()) or int(altezza) < 1:
                        print("Di quanto vuoi l'altezza? ", end ="")
                        altezza  = input()
                        if not(str(altezza).isdigit()) or int(altezza) < 1:
                            print("Errore, inserire un'altezza valida!")
                        else:
                            altezza = int(altezza)
                            sim = ""
                            while len(sim) < 1:
                                print("Che simbolo vuoi usare per disegnarlo? ", end ="")
                                sim = input()
                                if len(sim) < 1:
                                    print("Errore, inserire un simbolo valido!")
                                else:
                                    for i in range(0, altezza, 1):
                                        for j in range(0, base, 1):
                                            print(sim, end="")
                                        print("")

        case "triangolo" | "t":
            metodo = ""
            while (metodo != "base" and metodo != "altezza" and metodo != "b" and metodo != "a"):
                print("Lo vuoi disegnare data l'altezza o data la base? (Base/Altezza) ", end ="")
                metodo = input()
                match metodo.lower().strip():
                    case "base" | "b":
                        base = ""
                        while not(str(base).isdigit()) or int(base) <= 0:
                            print("Di quanto vuoi la base? ", end ="")
                            base = input()
                            if not(str(base).isdigit()) or int(base) <= 0:
                                print("Errore, inserire una base positiva!")
                            else:
                                base = int(base)
                                sim = ""
                                while len(sim) < 1:
                                    print("Che simbolo vuoi usare per disegnarlo? ", end ="")
                                    sim = input()
                                    if len(sim) < 1:
                                        print("Errore, inserire un simbolo valido!")
                                    else:    
                                        for i in range(math.ceil(base / 2), 0, -1):
                                            for j in range((i-1)*(len(sim)), 0, -1):
                                                print(" ", end="")
                                            for j in range((math.ceil(base / 2) - i + 1) * 2 - base % 2, 0, -1):
                                                print(sim, end="")
                                            print("")

                    case "altezza" | "a":
                        altezza = ""
                        while not(str(altezza).isdigit()) or int(altezza) < 1:
                            print("Di quanto vuoi l'altezza? ", end ="")
                            altezza = input()
                            if not(str(altezza).isdigit()) or int(altezza) < 1:
                                print("Errore, inserire un'altezza valida!")
                            else:
                                altezza = int(altezza)
                                sim = ""
                                while len(sim) < 1:
                                    print("Che simbolo vuoi usare per disegnarlo? ", end ="")
                                    sim = input()
                                    if len(sim) < 1:
                                        print("Errore, inserire un simbolo valido!")
                                    else:
                                        for i in range(altezza, 0, -1):
                                            for j in range((i-1)*len(sim), 0, -1):
                                                print(" ", end="")
                                            for j in range((altezza - i + 1) * 2, 1, -1):
                                                print(sim, end="")
                                            print("")

                    case _:
                        print("Metodo non valido!")

        case _:
            print("Figura non valida!")