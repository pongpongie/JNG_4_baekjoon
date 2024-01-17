array = []

for _ in range(9):
    array.append(int(input()))


result = sum(array) % 100

for i in range(0, 9):
    for j in range(i+1, 9):
        if result == array[i] + array[j]:
            array.remove(array[i])
            array.remove(array[j-1])
            break
    if len(array) == 7:
        break

array.sort()

for i in range(7):
    print(array[i])
