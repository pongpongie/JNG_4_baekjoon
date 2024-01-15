N = int(input())
num_list = input().split()

prime_cnt = 0
for i in range(len(num_list)):
    div_cnt = 0
    each_num = int(num_list[i])
    for j in range(1, each_num + 1) :
        if each_num % j == 0:
            div_cnt += 1
    if div_cnt == 2:
        prime_cnt += 1
print(prime_cnt)