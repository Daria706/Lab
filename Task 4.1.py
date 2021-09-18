sp = list(map(int,input('Введите элементы списка ').split()))
sum = 0
pr = 1
for x in sp:
    sum+=x
    pr*=x
print(sum)
print(pr)

