N, Q = tuple(map(int, input().split()))
A = list(map(int, input().split()))

shift = 0
ans = []

def index(i):
    return (i - 1 + shift) % N

def func1(x, y):
    A[x], A[y] = A[y], A[x]

def func3(x):
    ans.append(A[x])

for _ in range(Q):
    t, x, y = tuple(map(int, input().split()))
    if t == 1:
        x = index(x)
        y = index(y)
        func1(x, y)
    elif t == 2:
        shift -= 1
    else:
        x = index(x)
        func3(x)

for e in ans:
    print(e)