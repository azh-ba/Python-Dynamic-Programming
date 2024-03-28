import os

def howSum(targetSum, numbers):
    """Return an array containing any combination of elements that add up to exactly
    the targetSum. Return None if there is no combination possible.
    """
    # initialize the table
    table = [None] * (targetSum + 1)

    # assign default values to the table
    table[0] = []
    for num in numbers:
        table[num] = [num]
    
    # iterate through the table
    for i in range(len(table)):
        # check if the element is not None
        if (table[i] is not None) and (i != 0):
            for num in numbers:
                # check out of bound
                if (i + num) <= targetSum:
                    table[i + num] = table[i] + [num]

    return table[targetSum]

if __name__ == '__main__':
    os.system('cls')
    print(howSum(7, [2, 3]))            # --> [3, 2, 2]
    print(howSum(7, [5, 3, 4, 7]))      # --> [4, 3]
    print(howSum(7, [2, 4]))            # --> None
    print(howSum(8, [2, 3, 5]))         # --> [2, 2, 2, 2]
    print(howSum(300, [7, 14]))         # --> None