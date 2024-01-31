import sys
input = sys.stdin.readline

n = int(input())

meeting = []

for i in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda a: (a[1], a[0]))

cnt = 1
end_time = meeting[0][1]
for i in range(1, n):
    if meeting[i][0] >= end_time:
        cnt += 1
        end_time = meeting[i][1]

print(cnt)