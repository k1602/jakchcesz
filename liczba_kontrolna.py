def sprawdz():
    pesel = []
    pesel = input("podaj pierwsze 10 liczb PESEL: ")
    mnoznik = 1
    
    for liczba in pesel:
        index = 0
        a = int(pesel[index])
        a = a * mnoznik
        while a > 9:
            a = a - 10
            

        pesel[index] = str(a)
        if mnoznik == 1:
            mnoznik = 3
        
        if mnoznik == 3:
            mnoznik = 7
        
        if mnoznik == 7:
            mnoznik = 9
        
        if mnoznik == 9:
            mnoznik = 1
    print(pesel)

sprawdz()
