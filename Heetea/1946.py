import sys
T =  int(sys.stdin.readline())
for k in range(T):
    N = int(sys.stdin.readline())
    L = [sys.stdin.readline().rstrip().split() for i in range(N)]
    for i in range(N):
        L[i] = list(map(int, L[i]))
    L.sort()
    min_inter = int(L[0][1])
    D = len(L)
    for i in L:
        if int(i[1]) < min_inter:
            min_inter =int(i[1])
        elif int(i[1]) > min_inter:
            D = D-1
    print(D)
