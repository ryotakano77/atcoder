H, W = (int(e) for e in input().split())

matrix = []
for _ in range(H):
    row = [int(e) for e in input().split()]
    matrix.append(row)

sum_row = []
for h in range(H):
    sum_row.append(sum(matrix[h]))

sum_col = []
for w in range(W):
    col_w = [matrix[i][w] for i in range(H)]
    sum_col.append(sum(col_w))

for h in range(H):
    ans_h = []
    for w in range(W):
        ans_hw = sum_row[h] + sum_col[w] - matrix[h][w]
        ans_h.append(str(ans_hw))

    print(" ".join(ans_h))