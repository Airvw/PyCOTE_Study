case = int(input())

for i in range(case):
    N, X = list(map(int, input().split()))
    land = [[x] for x in range(N)]
    cnt = 0
    for j in range(N):
        land[j] = list(map(int, input().split()))

    for k in range(N):
        T = False  # down
        W = True #whole
        seq = 1
        for l in range(N-1):
            if land[k][l] == land[k][l+1]:
                seq += 1
            elif land[k][l] == land[k][l+1] + 1:
                if T == True and seq < X:
                    T = False
                    W = False
                    break
                elif l >= N-X:
                    W = False
                    break
                else: 
                    T = True
                seq = 1
            elif land[k][l] +1 == land[k][l+1]:
                if T == False and seq >=X:
                    seq = 1
                elif T == True and seq >= 2*X:
                    seq = 1
                    T = False
                else:
                    W = False
                    break
            elif abs(land[k][l] - land[k][l+1]) > 1:
                W = False
                break
        if W:
            cnt += 1
    print(cnt)
        
    landT = list(zip(*land))

    for k in range(N):
        T = False  # down
        W = True #whole
        seq = 1
        for l in range(N-1):
            if landT[k][l] == landT[k][l+1]:
                seq += 1
            elif landT[k][l] == landT[k][l+1] + 1:
                if T == True and seq < X:
                    T = False
                    W = False
                    break
                elif l >= N-X:
                    W = False
                    break
                else: 
                    T = True
                seq = 1
            elif landT[k][l] +1 == landT[k][l+1]:
                if T == False and seq >=X:
                    seq = 1
                elif T == True and seq >= 2*X:
                    seq = 1
                    T = False
                else:
                    W = False
                    break
            elif abs(landT[k][l] - landT[k][l+1]) > 1:
                W = False
                break
        if W:
            cnt += 1

    print('#%d %d' %(i+1, cnt))
