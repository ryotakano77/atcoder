plus = [[-1 for _ in range(10)] for _ in range(10)]
mul = [[[] for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        mod_plus = (i + j) % 10
        mod_mul = (i * j) % 10
        plus[i][mod_plus] = j
        mul[i][mod_mul].append(j)

def recursive(two_num: str):
    