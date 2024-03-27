import os

def gridTraveler(m, n):
    """Return the number of ways to travel in a m*n matrix, from top-left corner to
    bottom-right corner, by moving down and right only.
    """
    # default cases
    if (m == 0) or (n == 0):
        return 0
    if (m == 1) and (n == 1):
        return 1
    
    # initialize table
    table = [[0 for col in range(n + 1)] for row in range(m + 1)]
    table[1][1] = 1

    # assign values to the table
    for row in range(m + 1):
        for col in range(n + 1):
            if (row + 1) <= m:
                table[row + 1][col] += table[row][col]
            if (col + 1) <= n:
                table[row][col + 1] += table[row][col]
    
    return table[m][n]

if __name__ == '__main__':
    os.system('cls')
    print(gridTraveler(1, 1))       # --> 1
    print(gridTraveler(2, 3))       # --> 3
    print(gridTraveler(3, 2))       # --> 3
    print(gridTraveler(3, 3))       # --> 6
    print(gridTraveler(18, 18))     # --> 2333606220