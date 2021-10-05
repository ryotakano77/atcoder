N, D = tuple(map(int, input().split()))

ans = 0

# 頂点だけ別
if N - 1 >= D:
    ans += 2 ** D

# 頂点からの距離がiの部分
for i in range(1, N):
    ans_i = 0

    # 左側
    left_under = i + D
    if left_under <= N - 1:
        # 枝分かれはD回
        ans_i += 2 ** D

    # 右側
    # 登り途中
    if i + 1 >= D:
        ans_i += 1

    # 降り始め
    elif D - i >= N - 1:
        # 降りる数はD-i回
        ans_i += 2 ** (D - i - 1)

    num_i = 2 ** i # 個数
    ans += num_i * ans_i
    print(f"ans_{i}: {ans_i}")
    print(f"num_{i}: {num_i}")

print(ans)