N, L = (int(e) for e in input().split())
K = int(input())
div = [int(e) for e in input().split()]

ans_range_min = 1
ans_range_max = L // (K + 1)

def is_dividable(check):
    left = 0
    piece = 0
    for e in div:
        if e - left >= check:
            left = e
            piece += 1
    
    if piece > K:
        return True
    
    elif piece < K:
        return False

    elif L - left >= check:
        return True

    else:
        return False

while ans_range_max - ans_range_min > 1:
    check = (ans_range_min + ans_range_max) // 2
    if is_dividable(check):
        ans_range_min = check
    else:
        ans_range_max = check - 1

if is_dividable(ans_range_max):
    print(ans_range_max)

else:
    print(ans_range_min)