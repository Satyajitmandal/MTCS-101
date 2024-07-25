
def generate_fibonacci_list(n):
    fib_list = []
    a, b = 0, 1
    for i in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

def largest_fibonacci(fib_list):
    return max(fib_list)

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fib_list = generate_fibonacci_list(n)

largest_fib = largest_fibonacci(fib_list)

print(f"The first {n} Fibonacci numbers are: {fib_list}")
print(f"The largest Fibonacci number in the list is: {largest_fib}")
