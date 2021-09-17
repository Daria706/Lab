a = int(input())
k = 0
sum = 0
while a > 0:
   sum += a % 10
   a //= 10
   k += 1
print("Сумма цифр = ", sum)
print("Количество цифр = ", k)

