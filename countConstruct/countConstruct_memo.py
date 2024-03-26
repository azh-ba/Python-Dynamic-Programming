import os

def countConstruct(target, wordBank, memo=None):
    """Return the number of possible ways to construct the target from
    a list of element in wordBank. Return 0 if not possible.
    target      string
    wordBank    list[string]
    total       int
    """
    # initialize memo
    if memo is None:
        memo = {}

    # base case: target is in memo --> return memo
    if target in memo:
        return memo[target]
    
    # initialize total
    total = 0

    # base case: target is an empty string --> return 1
    if target == '':
        return 1
    
    # branching
    for word in wordBank:
        # check if word is a prefix of the target
        if target.startswith(word):
            # create a new target, then recurse the function
            suffix = str(target.replace(word, '', 1))
            counts = countConstruct(suffix, wordBank, memo)
            if counts != 0:
                total += counts
            
    memo[target] = total
    return total

if __name__ == '__main__':
    os.system('cls')
    print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))     # --> 2
    print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))     # --> 1
    print(countConstruct('stakeboard', [
        'bo', 
        'rd', 
        'ate', 
        't', 
        'ska', 
        'sk', 
        'boar'
    ]))     # --> 0
    print(countConstruct('enterapotentpot', [
        'a', 
        'p', 
        'ent', 
        'enter', 
        'ot', 
        'o', 
        't'
    ]))     # --> 4
    print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e', 
        'ee', 
        'eee', 
        'eeee', 
        'eeeee'
    ]))     # --> 0