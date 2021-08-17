T = int(input())

def func():
    box = [0] * ((10**9) + 1)
    N = int(input())
    for _ in range(N):
        l, r = tuple(map(int, input().split()))
        if 0 in box[l:r+1]:
            box[l+box[l:r+1].index(0)] = 1
        else:
            return "No"
    return "Yes"

for _ in range(T):
    print(func())