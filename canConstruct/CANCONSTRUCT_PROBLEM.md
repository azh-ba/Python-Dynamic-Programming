**CANCONSTRUCT_PROBLEM**

Write a function `canConstruct(target, wordBank)` that accepts a target string and an array of strings.

The function should return a boolean indicating whether or not the `target` can be constructed by concatenating elements of the `wordBank` array.

You may resue elements of `wordBank` as many times as possible.

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