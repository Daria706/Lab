s = 0
a = 1
n: list[int] =[1, 3, 5, 6, 11, 9, 1, 12]
for number in range(n):
    a *= k % 2
    s += k * a
print(s)

