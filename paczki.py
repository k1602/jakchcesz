sum = 0
pack = 0
pack_count = 0
lost_kg = 0
kontrola = 0

pack = input("podaj mase packi w kg")

while pack is True:
    if pack > 10 or pack < 1:
        print("error")
        break

