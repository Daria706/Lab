n: list[int] =[1, 3, 5, 6, 11, 9, 1, 12]
def num(n):
    a = 1
    s = 0
    for k in n:
        a *= k % 2
        s += k * a
    return s
print("Сумма = ", num(n))

