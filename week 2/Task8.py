import sys

def are_anagrams():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    
    if len(s1) != len(s2):
        print("NO")
        return

    if sorted(s1) == sorted(s2):
        print("YES")
    else:
        print("NO")

are_anagrams()