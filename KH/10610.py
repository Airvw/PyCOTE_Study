str_num = input()
l = []
sum = 0
result = ""
for i in str_num:
    l.append(i)
    sum += int(i)
l.sort(reverse=True)
if sum % 3 == 0:
    if (l[-1] == '0'):
        for i in l:
            result += i
        print(int(result))
    else:
        print("-1")
else:
    print("-1")
