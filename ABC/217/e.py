Q = int(input())
q = []
ans = []
head = -1

def q1(q, x, head):
    if not q:
        head = x
    q.append(x)
    return q, head

def q2(q, head):
    ans.append(head)
    if q:
        q = q[1:]
        head = q[0]
    else:
        q = []
        head = -1
    return q, head

def q3(q):
    q.sort()
    head = q[0]
    return q, head

for _ in range(Q):
    s = input()
    if s[0] == "1":
        num = int(s[2])
        q, head = q1(q, num, head)
    elif s[0] == "2":
        q, head = q2(q, head)
    else:
        q, head = q3(q)

for e in ans:
    print(e)