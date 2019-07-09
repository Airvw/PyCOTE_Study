import math as mt

whole_days = int(input())
korean = float(input())
math = float(input())
korean_per_day = float(input())
math_per_day = float(input())


amount_of_korean = korean / korean_per_day
amount_of_math = math / math_per_day

if amount_of_korean >= amount_of_math:
    print(whole_days - mt.ceil(amount_of_korean))
else:
    print(whole_days - mt.ceil(amount_of_math))
