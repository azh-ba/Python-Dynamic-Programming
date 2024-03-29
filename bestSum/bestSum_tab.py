import os

def bestSum(targetSum, numbers):
    """Return an array containing the shortest combination of numbers that
    add up to exacly the targetSum.
    """
    # initialize table

    table = [None] * (targetSum + 1)

    # assign default values to the table
    table[0] = []
    for num in numbers:
        table[num] = [num]

    # iterate through the table
    for i in range(len(table)):
        # check table[i != 0] is not None
        if (i != 0) and (table[i] is not None):
            for num in numbers:
                # check out of bound
                if (i + num) <= targetSum:
                    # check table[i + num] is not None
                    if table[i + num] is not None:
                        table[i + num] = table[i] + [num] if len(table[i] + [num]) < len(table[i + num]) else table[i + num]
                    else:
                        table[i + num] = table[i] + [num]

    return table[targetSum]

if __name__ == '__main__':
    os.system('cls')
    print(bestSum(7, [5, 3, 4, 7]))          # --> [7]
    print(bestSum(8, [2, 3, 5]))             # --> [3, 5]
    print(bestSum(8, [1, 4, 5]))             # --> [4, 4]
    print(bestSum(100, [1, 2, 5, 25]))       # --> [25, 25, 25, 25]