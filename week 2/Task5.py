def validate_plate(plate):
    allowed_letters = "ABCEHKMOPTXY"
    if len(plate) != 6:
        return "No"
    
    # Pattern: L D D D L L
    checks = [
        plate[0] in allowed_letters,
        plate[1].isdigit(),
        plate[2].isdigit(),
        plate[3].isdigit(),
        plate[4] in allowed_letters,
        plate[5] in allowed_letters
    ]
    return "Yes" if all(checks) else "No"

import sys
input_data = sys.stdin.read().splitlines()
if input_data:
    n = int(input_data[0])
    for i in range(1, n + 1):
        print(validate_plate(input_data[i]))