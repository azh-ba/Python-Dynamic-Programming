import os
import re

def canConstruct(target, wordBank):
    """Return a boolean indicating whether or not the target can be
    constructed by concatenating elements of the wordBank array.
    """
    # initialize the table
    table = [False] * (len(target) + 1)
    
    # assign default values for the table
    table[0] = True

    # iterate through the table
    for i in range(len(table)):
        if i >= len(target):
            break
        else:
            target_letter = target[i]
            for word in wordBank:
                # check word is a prefix of the target
                if word[0] == target_letter:
                    # check out of bound
                    if (i + len(word)) <= len(target):
                        table[i + len(word)] = True
    
    return table[len(target)]

if __name__ == '__main__':
    os.system('cls')
    # print(canConstruct('abcdef', [
    # 'ab', 
    # 'abc', 
    # 'cd', 
    # 'def', 
    # 'abcd'
    # ]))         # --> True
    print(canConstruct('skateboard', [
        'bo', 
        'rd', 
        'ate', 
        't', 
        'ska', 
        'sk', 
        'boar'
    ]))         # --> False
    # print(canConstruct('', [
    #     'cat', 
    #     'dog', 
    #     'mouse'
    # ]))         # --> True
    # print(canConstruct('enterapotentpot', [
    #     'a', 
    #     'p', 
    #     'ent', 
    #     'enter', 
    #     'ot', 
    #     'o', 
    #     't'
    # ]))         # --> True
    # print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    #     'e',
    #     'ee',
    #     'eee',
    #     'eeee',
    #     'eeeee',
    #     'eeeeee'
    # ]))         # --> False