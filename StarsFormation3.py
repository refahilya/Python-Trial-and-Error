#8 Nov 2022

def starsFormation3(n):
    for i in range (n):
        print("*" * (i + 1))
    for i in range (n):
        n -= 1
        print("*" * n)

starsFormation3 (4)
