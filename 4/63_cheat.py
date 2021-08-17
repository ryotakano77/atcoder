from collections import Counter

H, W = tuple(map(int, input().split()))

field = []
for _ in range(H):
    field.append(tuple(map(int, input().split())))

ans = 0

for i in range(1, 2 ** H):

    row_num = 0

    field_i = []
    for j in range(H):
        if i >> j & 1:
            field_i.append(field[j])
            row_num += 1

    nums_i = []
    for j in range(W):
        s = {field_i[r][j] for r in range(row_num)}
        if len(s) == 1:
            nums_i.append(s.pop())

    if nums_i:
        c = Counter(nums_i)
        types = c.most_common()[0][1]
        num = types * row_num

        ans = max(ans, num)

print(ans)