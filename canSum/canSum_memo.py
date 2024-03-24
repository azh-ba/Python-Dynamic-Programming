import os

def canSum(targetSum, numbers, memo={}, level=0):
    """Return True if the targetSum can be computed using numbers.
    False if otherwise.
    targetSum       int
    numbers         list
    memo            dict        {key:value} = {7:False}
    level           int         note the current level of the recursive tree.
                                increase whenever travel down from the root.
                                decrease whenever travel up to the root.
                                if travel back to the root, delete memo.
    """
    # increase level whenever travel further down the recursive tree
    level += 1

    # base case: result is saved in memo --> decrease level, return memo
    if targetSum in memo:
        level -= 1
        return memo[targetSum]
    
    # base case: targetSum = 0 --> decrease level, return True
    if targetSum == 0:  
        level -= 1
        return True
    
    # base case: targetSum < 0 --> decrease level, return False
    if targetSum < 0:
        level -= 1
        return False
    
    # branching
    for num in numbers:
        remainder = targetSum - num
        # case: if remainder is reachable --> save result to memo, decrease level, then return True
        if canSum(remainder, numbers, memo, level) == True:
            memo[targetSum] = True
            level -= 1
            # if reached the root (level == 0) --> delete the memo for further usage
            if level == 0:
                memo.clear()
            return True
        
    # no possible ways
    memo[targetSum] = False
    level -= 1
    # if reached the root (level == 0) --> delete the memo for further usage
    if level == 0:
        memo.clear()
    return False

if __name__ == '__main__':
    os.system('cls')
    print(canSum(7, [2, 3]))            # --> True
    print(canSum(7, [5, 3, 4, 7]))      # --> True
    print(canSum(7, [2, 4]))            # --> False
    print(canSum(8, [2, 3, 5]))         # --> True
    print(canSum(300, [7, 14]))         # --> False