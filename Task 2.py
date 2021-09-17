a = float(input("Введите основание a"))
h = float(input("Введите высоту h"))
S = 0.5 * a * h
if S%2 == 0:
    S=S/2
    print("S=",S)
else:
    print("Не могу делить на 2!")