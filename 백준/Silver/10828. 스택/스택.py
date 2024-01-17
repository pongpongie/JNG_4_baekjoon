import sys
input = sys.stdin.readline

N = int(input())

class Stack :
    def __init__(self):
        self.stk = []

    def push(self, x):
        self.stk.append(x)

    def pop(self):
        if len(self.stk) != 0:
            pop_item = self.stk.pop()
            print(pop_item)
        else: print(-1)

    def size(self):
        print(len(self.stk))
        
    def empty(self):
        if len(self.stk) == 0:
            print(1)
        else: print(0)

    def top(self):
        if len(self.stk) == 0:
            print(-1)
        else: print(self.stk[-1])
        
stack = Stack()

for _ in range(N):
    command = input().split()
    if command[0] == "push":
        stack.push(command[1])
    elif command[0] == "top":
        stack.top()
    elif command[0] == "size":
        stack.size()
    elif command[0] == "empty":
        stack.empty()
    elif command[0] == "pop":
        stack.pop()