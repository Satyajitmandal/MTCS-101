def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n=int(input("Enter no of fibonacci num to be printed:"))

fib_sequence = fibonacci_iterative(n)
print(f"The first {n} Fibonacci numbers are: {fib_sequence}")
