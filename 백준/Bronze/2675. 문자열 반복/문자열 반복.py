cases = int(input())

for i in range(cases):
    temp = input().split()
    word = ""
    R = int(temp[0])
    S = str(temp[1])
    for j in range(len(S)):
        word += S[j]*R
    print(word)
