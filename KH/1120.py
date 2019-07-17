a, b = input().split()
d= len(b) -len(a)
max = 9999

for x in range(d + 1):
    count = 0
    for i in range(len(a)):
        if b[i + x] != a[i]:
            count+=1
    if count < max:
        max = count

print(max)