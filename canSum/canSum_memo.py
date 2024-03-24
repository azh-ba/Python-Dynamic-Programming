import os

def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

# def canSum(targetSum, numbers, memo={}):
#     """Return True if the targetSum can be computed using numbers.
#     False if otherwise.
#     targetSum       int
#     numbers         list
#     memo            dict{key:value} = {7:False}
#     """
#     # base case: result is saved in memo --> return memo
#     if targetSum in memo:
#         return memo[targetSum]
    
#     # base case: targetSum = 0 --> return True
#     if targetSum == 0:  
#         return True
    
#     # base case: targetSum < 0 --> return False
#     if targetSum < 0:
#         return False
    
#     # branching
#     for num in numbers:
#         remainder = targetSum - num
#         # case: if remainder is reachable --> save result to memo, then return True
#         if canSum(remainder, numbers, memo) == True:
#             memo[targetSum] = True
#             return True
        
#     # no possible ways
#     memo[targetSum] = False
#     return False

if __name__ == '__main__':
    os.system('cls')
    print(canSum(7, [2, 3]))            # --> True
    # print(canSum(7, [5, 3, 4, 7]))      # --> True
    print(canSum(7, [2, 4]))            # --> False
    # print(canSum(8, [2, 3, 5]))         # --> True
    # print(canSum(300, [7, 14]))         # --> False