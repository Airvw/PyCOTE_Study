a = int(input())
b = list(map(int, input().split()))

b.sort()
sum = 0
for i in range(len(b)):
    for j in range(i + 1):
       sum += b[j]

print(sum)