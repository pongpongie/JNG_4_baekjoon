# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
import sys
input = sys.stdin.readline

temp = input().split()
a = int(temp[0])
b = int(temp[1])

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

