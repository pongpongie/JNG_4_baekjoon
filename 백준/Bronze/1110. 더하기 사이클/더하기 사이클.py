import sys
from collections import deque
# input = sys.stdin.readline


origin = deque()
N = input()
cnt = 0

if len(N) == 1:
    origin.append("0")
    origin.append(N[-1])
else: 
    origin.append(N[0])
    origin.append(N[1])

while True:
    new_num = deque()
    sum_num = int(origin[0]) + int(origin[-1])
    new_num.append(origin[-1])
    new_num.append(str(sum_num)[-1])
    cnt += 1
    origin = new_num
    if int(N) == int(new_num[0] + new_num[-1]):
        break
     
print(cnt)