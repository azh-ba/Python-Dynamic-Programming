import os

def countConstruct(target, wordBank):
    """Return the number of ways that the target can be constructed by concatenating
    elements of the wordBank array.
    """
    # initialize the table
    table = [0] * (len(target) + 1)

    # assign default values for the table
    table[0] = 1
    prefix = ''

    # iterate through the table
    for i in range(len(target)):
        # get the suffix (new target)
        suffix = target.replace(prefix, '', 1)
        for word in wordBank:
            # check if word is in the suffix
            if suffix.startswith(word):
                # check out of bound
                if (i + len(word)) <= len(target):
                    table[i + len(word)] += table[i]
        # prepare prefix for the next suffix
        prefix += target[i]

    return table[len(target)]



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