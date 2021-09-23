import sys

nazwa_restauracji = str(input("podaj nazwe restauracji: "))
nazwa_pizzy = str(input("podaj nazwe pizzy: "))
rozmiar_pizzy = float(input("podaj rozmiar pierwszej pizzy w cm: "))
cena_pizzy = float(input("podaj cene pierwszej pizzy: "))
stosunek1 = (cena_pizzy/(3.14*((rozmiar_pizzy/200)*(rozmiar_pizzy/200))))
a = int(input("jeżeli chcesz wpisac inna restauracje wcisnij 1 jezeli nie to 0: "))


while (a == 1):
    nazwa_restauracji2 = str(input("podaj nazwe restauracji: "))
    nazwa_pizzy2 = str(input("Podaj nazwe pizzy: "))
    rozmiar_pizzy2 = float(input("podaj rozmiar pizzy w cm: "))
    cena_pizzy2 = float(input("podaj cene pizzy: "))
    stosunek2 = (cena_pizzy2/(3.14*((rozmiar_pizzy2/200)*(rozmiar_pizzy2/200))))
    if stosunek2 < stosunek1:
        nazwa_restauracji = nazwa_restauracji2
        nazwa_pizzy = nazwa_pizzy2
        rozmiar_pizzy = rozmiar_pizzy2
        cena_pizzy = cena_pizzy2


    a = int(input("jeżeli są inne rozmiary pizz wcisnij 1 jezeli nie to 0: "))

rozmiar_pizzy = str(rozmiar_pizzy)
cena_pizzy = str(cena_pizzy)

lista = [nazwa_restauracji, nazwa_pizzy, rozmiar_pizzy, cena_pizzy]

print(f"Restauracja: {lista[0]} pizza: {lista[1]} rozmiar: {lista[2]}cm cena: {lista[3]}zl")

