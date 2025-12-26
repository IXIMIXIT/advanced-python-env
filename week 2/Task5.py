n = int(input())
valid_letters = "ABCEHKMOPTXY"

for i in range(n):
    plate = input().strip()
    
    if len(plate) != 6:
        print("No")
        continue

    check1 = plate[0] in valid_letters
    check2 = plate[1:4].isdigit()
    check3 = plate[4] in valid_letters
    check4 = plate[5] in valid_letters

    if check1 and check2 and check3 and check4:
        print("Yes")
    else:
        print("No")