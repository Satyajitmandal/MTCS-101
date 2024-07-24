def fibonacci_recursive(n, call_count):
    call_count[0] += 1 
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1, call_count) + fibonacci_recursive(n-2, call_count)
    
def fibonacci_with_call_count(n):
    call_count = 0  
    fib_number = fibonacci_recursive(n, call_count)
    return fib_number, call_count[0]
 
n = int (input("Enter the postion of ficonacci num to be printed:"))
fib_number, calls = fibonacci_with_call_count(n)
print(f"Fibonacci number at position {n} is {fib_number}")
print(f"Number of function calls made: {calls}")


