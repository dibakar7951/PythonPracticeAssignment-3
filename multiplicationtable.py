def multiplicationtableof10(n):
    for i in range(1,n+1):
        print (f"{i} x 10 = {i*10}")

n =int(input("Enter the max number: "))
multiplicationtableof10(n)