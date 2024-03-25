import os

def bestSum(targetSum, numbers, memo=None):
    """Return a list of numbers that its sum is equal to targetSum,
    and the length of the list is the shortest (least amount of number).
    Return None if no such list exists.
    result      list[]      save results
    memo        dict{}      {key:value} = {targetSum:[...]}
    """
    # initalize memo
    if memo is None:
        memo = {}

    # base case: targetSum in memo --> return memo
    if targetSum in memo:
        return memo[targetSum]
    
    # base case: targetSum = 0 --> return []
    if targetSum == 0:
        return []
    
    # base case: targetSum < 0 --> return None
    if targetSum < 0:
        return None
    
    shortest_combination = None

    # branching
    for num in numbers:
        remainder = targetSum - num
        result = bestSum(remainder, numbers, memo)
        # case: if result is not empty
        if result is not None:
            # create a copy of 'result' with num appended, then save to 'combination' for later comparison
            # DO NOT USE 'combination = result.append(num)', because in every iteration the same list will be used to modifications, which is not desired.
            combination = list(result) + [num]
            # compare to shortest_combination --> update
            if (shortest_combination is None) or (len(combination) <= len(shortest_combination)):
                shortest_combination = combination

    memo[targetSum] = shortest_combination
    return shortest_combination

if __name__ == '__main__':
    os.system('cls')
    print(bestSum(7, [5, 3, 4, 7]))          # --> [7]
    print(bestSum(8, [2, 3, 5]))             # --> [3, 5]
    print(bestSum(8, [1, 4, 5]))             # --> [4, 4]
    print(bestSum(100, [1, 2, 5, 25]))       # --> [25, 25, 25, 25]