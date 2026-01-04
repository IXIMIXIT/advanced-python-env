# 7.2: Integer to 10-digit Octal
print("\nTask 7.2: Octal Converter")
n = int(input())
o = oct(n)[2:]
print(o.zfill(10))