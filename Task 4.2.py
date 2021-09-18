array = [1, 2.0, 3, 5, 0, 53.1, 0, 1.2]
s=0
k=0
for i in array:
    s+=i
    k+=1
sa=s/k
for i in range(len(array)):
    if array[i]==0:
        array[i]=sa
print(array)


