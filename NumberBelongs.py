def binary_search(A, x):
    left, right = 0, len(A) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if A[mid] == x:
            return True
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


input_string = input("Enter sorted elements separated by space or comma: ")

if ',' in input_string:
    A = [int(x) for x in input_string.split(',')]
else:
    A = [int(x) for x in input_string.split()]

x = int(input("Enter the number to search for: "))

if binary_search(A, x):
    print("Element exists in the array")
else:
    print("Element does not exist in the array")
