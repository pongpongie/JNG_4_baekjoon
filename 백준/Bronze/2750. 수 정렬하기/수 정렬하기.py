N = int(input())
array = []

for i in range(0, N):
    number = int(input()) 
    array.append(number)
    key = number
    j = i - 1
    while j > -1 and array[j] > key :
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = key

for i in range(len(array)):
    print(array[i])

