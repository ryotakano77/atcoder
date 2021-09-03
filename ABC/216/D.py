from collections import Counter

N, K = tuple(map(int, input().split()))
A = list(map(int, input().split()))
c = Counter(A)
keys = sorted(c.keys(), reverse=True)

def score_count(origin_score, next_score, num):
    # origin_scoreのものがnumこある
    count_single = origin_score - next_score
    count = num * count_single
    score_single = (origin_score + next_score + 1) * (count_single) // 2
    score = score_single * num
    return score, count

def score_struggle(biggest, num, countable):
    mean = countable // num
    score = (biggest + biggest - mean + 1) * mean // 2 * num
    score += (biggest - mean) * (countable % num)
    return score


num = 0
ans = 0

for i in range(len(keys)):
    
    biggest = keys[i]
    if i == len(keys) - 1:
        next_biggest = 0
    else:
        next_biggest = keys[i+1]

    num += c[biggest]

    score, count = score_count(biggest, next_biggest, num)

    if K >= count:
        K -= count
        ans += score

    else:
        score = score_struggle(biggest, num, K)
        ans += score
        K = 0
        print(ans)
        exit()

print(ans)