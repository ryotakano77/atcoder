from collections import deque

N, K = tuple(map(int, input().split()))
sequence = tuple(map(int, input().split()))

ans = [0] * N

last = 0
que = deque([sequence[0]])
d = {sequence[0]: 1}

# index:iのときどこまででK種類か
for i in range(N):

    # 足りない時，または足りてるけど伸ばせる時は右に伸ばす
    while last < N-1 and (len(d) < K or (len(d) == K and sequence[last+1] in d)):
        last += 1
        que.append(sequence[last])
        if not sequence[last] in d:
            d[sequence[last]] = 1
        else:
            d[sequence[last]] += 1

    # まず種類確認して，K種類だったらそこまで
     #if len(que) == K:
    ans[i] = last - i + 1
    # i番目の要素を抜く
    delete = que.popleft()
    if d[delete] == 1:
        del d[delete]
    else:
        d[delete] -= 1

print(max(ans))