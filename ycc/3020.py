N, H = map(int,input().split())

Cave = [[0]*N for _ in range(H)]

for i in range(int(N/2)):

    suk = int(input())
    for j in range((H-1),(H-1-suk),-1):
        Cave[j][2*i] = 1

    jong = int(input())
    for k in range(0,jong,1):
        Cave[k][2*i+1] = 1

score=[]
sumnum=0
for m in range(H):
    sumnum = 0
    for n in range(N):

        if Cave[m][n] == 1:
            sumnum+=1
    score.append(sumnum)

score.sort()
min_=score[0]
numnum=score.count(min_)
print(Cave)
print(min_,numnum)

