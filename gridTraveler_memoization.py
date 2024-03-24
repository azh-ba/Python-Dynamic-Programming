def gridTraveler(row, col, memo = {}):
    """Return the number of unique ways to move from top left corner 
    to the bottom right corner in a row*col matrix.
    """
    key = str(row) + ',' + str(col)
    # base case: if memo has the saved result --> return saved results
    if key in memo:
        return memo[key]

    # base case: if row or col is equal to 0 --> return 0
    if row == 0 or col == 0:
        return 0
    
    # base case: if (row, col) = (1, 1) --> return 1
    if row == 1 and col == 1:
        return 1
    
    # save result to memo
    memo[key] = gridTraveler(row - 1, col, memo) + gridTraveler(row, col - 1, memo)

    return memo[key]
    
if __name__ == '__main__':
    print(gridTraveler(1, 1))       # --> 1
    print(gridTraveler(2, 3))       # --> 3
    print(gridTraveler(3, 2))       # --> 3
    print(gridTraveler(3, 3))       # --> 6
    print(gridTraveler(18, 18))     # --> 2333606220