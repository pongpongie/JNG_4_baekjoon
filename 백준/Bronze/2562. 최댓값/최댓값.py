lists = []
index = 0

for _ in range(9):
    a = int(input())
    lists.append(a)

max = lists[0]

for i in range(len(lists)):
    if max <= lists[i]:
        max = lists[i]
        index = i

print(max)
print(index+1)
