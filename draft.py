import os

if __name__ == '__main__':
    os.system('cls')

    n = 4
    test_dict = {1: 1, 
                2: 1, 
                3: 2, 
                4: 3, 
                5: 5, 
                6: 8}

    print(n in test_dict)
    print(test_dict[n])
    print()

    original = [1, 2, 3]
    temp1 = original[:]
    temp2 = list(temp1) + [123]
    temp3 = temp2

    temp4 = original.append(4)
    print(temp4)
    print(temp1)
    print(temp2)
    print(temp3)
    print()

    word = 'sk'
    target = 'skateboard'
    new_target = str(target.replace(word, ''))
    print(word[0])
    print(target[0])
    print(word[0] == target[0])
    print(new_target)
    print(target)
    print()

    arr = [['hello', 'my', 'wonderful', 'friends'], ['nice', 'to', 'meet', 'you']]
    narr = []
    new = list(map(lambda way: ['oh', *way], arr))
    narr.extend(new)
    print(narr)
    