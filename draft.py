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