N = input()

if '0' in N:
    N = list(map(int, N))
    if sum(N) % 3==0:
        N.sort(reverse=True)
        N = list(map(str, N))
        print(''.join(N))
    else:
        print(-1)
else:
    print(-1)
