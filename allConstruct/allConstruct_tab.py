import os

def allConstruct(target, wordBank):
    """Return a 2D array containing all of the ways that the target can be constructed
    by concatenating elements of the wordBank array.
    """
    # initialize the table
    table = [[] for _ in range(len(target) + 1)]
    
    # assign default values to the table
    table[0] = [[]]
    prefix = ''

    # iterate through the table
    for i in range(len(target)):
        # get the suffix
        suffix = target.replace(prefix, '', 1)
        for word in wordBank:
            if suffix.startswith(word):
                newCombinations = list(map(lambda way: [*way, word], table[i]))
                # check out of bound
                if (i + len(word) <= len(target)):
                    table[i + len(word)].extend(newCombinations)
        # prepare prefix for the next suffix
        prefix += target[i]
    
    return table[len(target)]

if __name__ == '__main__':
    os.system('cls')
    print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    # --> [
    #       ['purp', 'le']
    #       ['p', 'ur', 'p', 'le']
    #     ]
    print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
    # # --> [
    # #       ['ab', 'cd', 'ef']
    # #       ['ab', 'c', 'def']
    # #       ['abc', 'def']
    # #       ['abcd', 'ef']
    # #     ]
    print(allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    # # --> []
    print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))
    # # --> []