**COUNTCONSTRUCT_PROBLEM**

Write a function `countConstruct(target, wordBank)` that accepts a target string and an array of strings.

The function should return the number of ways that the `target` can be constructed by concatenating elements of the `wordbank` array.

You may reuse elements of `wordBank` as many times as needed.

```py
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
```