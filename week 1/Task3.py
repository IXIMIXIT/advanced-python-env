A = float(input())

integer_part = int(A)                 #a=12.8 int=12
fractional_part = A - integer_part    #frac=12.8-12=0.8

new_number = fractional_part * 100 + integer_part / 100 #8*100+12/100=8.12
print(new_number)
