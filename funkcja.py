a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))
delta = (b*b)-(4*a*c)

if delta < 0:
    print("nie ma miejsc zerowych")
elif delta == 0:
    x = (b*-1)/(2*a)
    print(f"Miejsce zerowe to x={x}")
elif delta > 0:
    x = ((b*-1)-(delta**(1/2)))/(2*a)
    xx = ((b*-1)+(delta**(1/2)))/(2*a)
    print(f"Miejsca zerowe to x1={x} oraz x2={xx}")
