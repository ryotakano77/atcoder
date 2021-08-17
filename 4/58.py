N, K = tuple(map(int, input().split()))

if N == 0:
    print(0)
    exit()

def original_add(a: int) -> int:
    sum_of_rank = sum([int(e) for e in str(a)])
    return a + sum_of_rank

results = [N]
n = N
while True:
    result = original_add(n)
    mod = result % (10 ** 5)
    if mod in results:
        idx = results.index(mod)
        roop = len(results) - idx
        if K <= idx:
            print(results[K])
            exit()
        else:
            # ループのスタートに来るまでを引く
            K -= idx
            # ループした後のあまり
            K %= roop
            print(results[idx+K])
            exit()
    else:
        results.append(mod)
        n = mod

