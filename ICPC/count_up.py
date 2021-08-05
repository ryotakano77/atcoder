def main():
    N = int(input())
    if N == 0:
        exit()
    
    ans = 0
    sequence = list(map(int, input().split()))
    for i in range(N-3):
        if sequence[i:i+4] == [2, 0, 2, 0]:
            ans += 1
    
    print(ans)

while True:
    main()