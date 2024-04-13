import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_c = list_a + list_b
list_c.sort()
print(* list_c)