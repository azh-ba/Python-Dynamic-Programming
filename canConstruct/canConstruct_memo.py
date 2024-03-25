import os

def canConstruct(target, wordBank, memo=None):
    """Return True if the target can be constructed by using elements in the wordBank.
    Return False if otherwise.
    """
    # initialize memo
    if memo is None:
        memo = {}

    # base case: if target is in memo --> return memo
    if target in memo:
        return memo[target]

    # base case: if target is '' --> return True
    if target == '':
        return True
    
    # branching
    for word in wordBank:
        # check pre-fix of the element with the target
        if target.startswith(word):
            suffix = str(target.replace(word, '', 1))
            # case: possible to construct --> return True
            if canConstruct(suffix, wordBank, memo):
                memo[target] = True
                return True
            
    # no possible way
    memo[target] = False
    return False

if __name__ == '__main__':
    os.system('cls')
    print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))                       # --> True
    print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))        # --> False
    print(canConstruct('', ['cat', 'dog', 'mouse']))                                        # --> True
    print(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))      # --> True
    print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee'
    ]))                                                                                     # --> False