import os

def fib_tab(number):
    """Return the n-th (number-th) value of the Fibonacci series."""
    table = [0] * (number + 1)
    table[1] = 1
    for i in range(number):
        table[i + 1] += table[i]
        if (i + 2) <= number:
            table[i + 2] += table[i]
    return table[number]


if __name__ == '__main__':
    os.system('cls')
    print(fib_tab(10))      # --> 55
    print(fib_tab(50))      # --> 12586269025