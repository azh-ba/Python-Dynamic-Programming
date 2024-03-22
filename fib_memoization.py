import os

def fib_recursion(n):
    """Return the n-th number in the Fibonacci sequence using recursion."""
    # base case: n = 1, 2 -> fib(n) = 1
    if n <= 2:
        return 1
    else:
        # return sum of the previous two numbers
        return fib_recursion(n - 1) + fib_recursion(n - 2)
    
if __name__ == '__main__':
    os.system('cls')
    print(fib_recursion(50))