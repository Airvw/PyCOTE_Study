l = []
count = 0
max = 0
for i in range(4):
    a = list(map(int, input().split()))
    # a, b = input().split()
    l.append(a)
for i in range(4):
    if(l[i][0] == 0):
        count += l[i][1]
        if(max < count):
            max = count
    elif(l[i][0] != 0):
        count -= l[i][0]
        count += l[i][1]
        if(max < count):
            max = count
print(max)