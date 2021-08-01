H, W = (int(e) for e in input().split())

if H == 1:
    print(W)
    exit()

if W == 1:
    print(H)
    exit()
    
h = -(-H // 2)
w = -(-W // 2)

print(h * w)