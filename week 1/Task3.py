A = float(input())

integer_part = int(A)
fractional_part = A - integer_part

new_number = fractional_part * 100 + integer_part / 100
print(new_number)
