'''
Title : Number Baseball Game
Author : Seungje
Date : 2022.03.05
Version : 1.0
Description : ...
How to play : 
'''

import random

def get_target_num(digits):
    '''
    set a target number with the given digits,
    that is a length of user's first input.
    The output has not duplicate numbers.
    input : int
    output : list of integers
    '''
    target = [random.randint(1,9) for idx in range(digits)]
    target_num = []
    for val in target:
        while val in target_num:
            val = random.randint(1,9)
        target_num.append(val)
    return target_num

def change_tolist(num_str):
    '''
    change to list from string, which is user's input
    And this checks user's input consists only numbers(1~9).
    input : string
    output : list of integers
    '''
    int_checker = ['1','2','3','4','5','6','7','8','9']
    result = False
    while not result:
        for val in num_str:
            if val not in int_checker:
                print("only number")
                result = False
                num_str = input(text2 + "\n" + text1)
                break
            else:
                result = True

    num_list = [int(val) for val in num_str]
    return num_list

def check_num(num):
    '''
    check a deplicate value in numbers that is user's input
    input : list of integers
    output : boolean

    '''
    num = num.copy()
    l_num = len(num)
    for idx in range(l_num):
        val = num.pop(0)
        if val in num:
            return False
        else:
            result = True
    return result

def check_ballcount(user_num, target_num, ballcount):
    '''
    check a number of strikes and balls
    input : list, list, list
    output : list
    '''
    l_num = len(user_num)
    for idx1 in range(l_num):
        for idx2 in range(l_num):
            if idx1 == idx2 and user_num[idx1] == target_num[idx2]:
                ballcount[0] += 1
            if idx1 != idx2 and user_num[idx1] == target_num[idx2]:
                ballcount[1] += 1
    return ballcount

def check_user_num(user_num, l_user_num):
    '''
    check whether user number of digits exceeds 10
    input : list
    output list, int
    '''
    while l_user_num > 9:
        user_num = change_tolist(
            input(text2 + "\n" + text1))
        l_user_num = len(user_num)
    while not check_num(user_num) or len(user_num) != l_user_num:
        user_num = change_tolist(
            input(text2 + "\n" + text1))
    return user_num, l_user_num

def init_baseball():
    '''
    initialize variables
    input : None
    output : list, list, list, int
    '''
    user_num = change_tolist(input(text1))
    l_user_num = len(user_num)
    user_num, l_user_num = check_user_num(user_num, l_user_num)
    target_num = get_target_num(l_user_num)
    repeat_num = 1
    return user_num, l_user_num, target_num, repeat_num

text1 = "input a number : "
text2 = "Sorry, It's not corrected number. Please again."

def run_baseball():
    '''
    execution function
    '''
    user_num, l_user_num, target_num, repeat_num = init_baseball()
    
    while True:
        ballcount = [0 for idx in range(2)]
        ballcount = check_ballcount(user_num, target_num, ballcount)
        if ballcount[0] == l_user_num:
            print(l_user_num, "Strike, OUT!!")
            print("You succeeded in", repeat_num,"attempts.")
            break
        else:
            print(ballcount[0], "Strike, ", ballcount[1], "Ball")
            repeat_num += 1
        user_num = change_tolist(input(text1))
        user_num, l_user_num = check_user_num(user_num, l_user_num)

if __name__ == "__main__":
    run_baseball()

