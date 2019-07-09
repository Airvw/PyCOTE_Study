# l = int(input())
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# day = 0
# count = 0

# while ( not( a < 0 & b < 0)):
#     if a > 0:
#         a -= c
#     if b > 0:
#         b -= d
#     count +=1

# day = l - count - 1
# print(day)

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = a//c
if a%c != 0:
    e += 1
f = b//d
if b%d !=0:
    f += 1

if e < f:
    print(l - f )
else:
    print(l - e )