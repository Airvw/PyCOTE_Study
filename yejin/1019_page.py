page_of_book = int(input())

count = [0] * 10 

for page in range(1, page_of_book + 1):
    page = str(page)
    for j in range(0, len(page)): 
        index = int(page[j])
        count[index] += 1

for i in range(0, len(count)):
    print("%d " %count[i], end='')
