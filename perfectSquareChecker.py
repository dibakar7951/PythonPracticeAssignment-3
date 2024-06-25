import math

def isPerfectSquare(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

num = int(input("Enter a number: "))
if isPerfectSquare(num):
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")
