import os

def fib_recursion(n):
    """Return the n-th number in the Fibonacci sequence, using recursion."""
    # base case: n = 1, 2 -> fib(n) = 1
    if n <= 2:
        return 1
    else:
        # return sum of the previous two numbers
        return fib_recursion(n - 1) + fib_recursion(n - 2)

def fib_memoization(n, memo = {}):
    """Return the n-th number in the Fibonacci sequence, using memoization.
    memo    dict{key:value} = {1:1, 2:1, ...}    save results for later use
    """
    # base case: if key n exists in memo --> return value of memo at key n
    if n in memo:
        return memo[n]
    # base case: if n = 1, 2 --> return 1
    if n <= 2:
        return 1
    else:
        # save result in memo first, then return
        memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
        return memo[n]

if __name__ == '__main__':
    os.system('cls')
    print(fib_recursion(10))
    print(fib_memoization(50))