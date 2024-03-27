import os

def allConstruct(target, wordBank, memo=None):
    """Return a 2D list that contains all possible ways to construct the target
    from the elements in wordBank. Return empty list if no possible construct.
    target      string
    wordBank    list[string]
    """
    # initialize memo
    if memo is None:
        memo = {}
    
    # base case: if target in memo --> return memo
    if target in memo:
        return memo[target]
    
    # base case: target is an empty string --> return an empty 2D list
    if target == '':
        return [[]]
    
    # initialize result
    result = []

    # branching
    for word in wordBank:
        if target.startswith(word):
            suffix = str(target.replace(word, '', 1))
            suffix_ways = allConstruct(suffix, wordBank, memo)
            prefix_ways = list(map(lambda way: [word, *way], suffix_ways))
            result.extend(prefix_ways)
            # save result to memo
            memo[target] = result
    
    return result
    
if __name__ == '__main__':
    os.system('cls')
    print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    # --> [
    #       ['purp', 'le']
    #       ['p', 'ur', 'p', 'le']
    #     ]
    print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
    # --> [
    #       ['ab', 'cd', 'ef']
    #       ['ab', 'c', 'def']
    #       ['abc', 'def']
    #       ['abcd', 'ef']
    #     ]
    print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    # --> []
    print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
    # --> []