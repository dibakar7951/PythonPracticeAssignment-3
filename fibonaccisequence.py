def fibonaccisequence(n):
    sequence = [0, 1] 
    for i in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)
    return sequence[:n]

n = int(input("Enter the count of fibonacci sequence to generate: "))
print(fibonaccisequence(n))