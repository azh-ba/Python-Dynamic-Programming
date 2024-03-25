import os

def howSum(targetSum, numbers, memo=None):
    """Return a list of numbers that its sum is equal to targetSum.
    Return None if no such list exists.
    result      list[]      save result
    """
    # initialize memo
    if memo is None:
        memo = {}

    # base case: targetSum is in memo --> return memo
    if targetSum in memo:
        return memo[targetSum]

    # base case: targetSum = 0 --> return an empty list
    if targetSum == 0:
        return []
    
    # base case: targetSum < 0 --> return None
    if targetSum < 0:
        return None
    
    # branching
    for num in numbers:
        remainder = targetSum - num
        # case: result[] has element --> return result[]
        result = howSum(remainder, numbers, memo)
        if result is not None:
            result.append(num)
            memo[targetSum] = result
            return memo[targetSum]
        
    # no possible way
    memo[targetSum] = None
    return None

if __name__ == '__main__':
    os.system('cls')
    print(howSum(7, [2, 3]))            # --> [3, 2, 2]
    print(howSum(7, [5, 3, 4, 7]))      # --> [4, 3]
    print(howSum(7, [2, 4]))            # --> None
    print(howSum(8, [2, 3, 5]))         # --> [2, 2, 2, 2]
    print(howSum(300, [7, 14]))         # --> None