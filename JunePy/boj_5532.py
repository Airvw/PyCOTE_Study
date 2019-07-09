#June
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
kor = A//C;
eng = B//D;
kor = kor+1 if A % C else kor
dayCount = kor if kor > eng else eng
print(L-dayCount)

