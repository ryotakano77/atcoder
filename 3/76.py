N = int(input())
A = list(map(int, input().split()))
s = sum(A)
A *= 2
start, end = 0, 0
part = A[0]
if part * 10 == s:
    print("Yes")
    exit()

while start < N:
    # endを増やしていく
    while part * 10 < s:
        # ケツが増える
        end += 1
        part += A[end]

    # 同じになったかチェック
    if part * 10 == s:
        print("Yes")
        exit()
    
    # なってなかったらケツを下げて頭を上げる
    part -= A[end]
    part -= A[start]
    end -= 1
    start += 1

print("No")