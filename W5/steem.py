
def main():
    print('''This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:

    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.''')
    user_input = take_user_input()
    #print(user_input)
    score = 0
    #score += positive_numbers(user_input) + negative_numbers(user_input)
    score += positive_numbers(user_input)
    score += negative_numbers(user_input) 
    print(f'Your score is {score}')
    print(f'A score below 15 may indicate problematic low self-esteem.')

def take_user_input():
    question_list = []
    q1 = input("I feel that I am a person of worth, at least on an equal plane with others. Enter D, d, a, or A: ")
    question_list.append(q1)
    q2 = input("I feel that I have a number of good qualities. Enter D, d, a, or A: ")
    question_list.append(q2)
    q3 = input("All in all, I am inclined to feel that I am a failure. Enter D, d, a, or A: ")
    question_list.append(q3)
    q4= input("I am able to do things as well as most other people. Enter D, d, a, or A: ")
    question_list.append(q4)
    q5 = input("I feel I do not have much to be proud of. Enter D, d, a, or A: ")
    question_list.append(q5)
    q6 = input("I take a positive attitude toward myself. Enter D, d, a, or A: ")
    question_list.append(q6)
    q7 = input("On the whole, I am satisfied with myself. Enter D, d, a, or A: ")
    question_list.append(q7)
    q8 = input("I wish I could have more respect for myself. Enter D, d, a, or A: ")
    question_list.append(q8)
    q9 = input("I certainly feel useless at times. Enter D, d, a, or A: ")
    question_list.append(q9)
    q10 = input("At times I think I am no good at all. Enter D, d, a, or A: ")
    question_list.append(q10)
    return question_list
    
def positive_numbers(user_input):
    number = 0
    for i in range(10): 
        if (i == 0 or i == 1 or i == 3 or i == 5 or i == 6):
            if user_input[i] == "D":
                number += 0
            elif user_input[i] == "d":
                number += 1
            elif user_input[i] == "a":
                number += 2
            elif user_input[i] == "A":
                number += 3 
    print(number)
    return number
                
            
def negative_numbers(user_input):
    number = 0
    for i in range(10):
        if (i == 2 or i == 4 or i == 7 or i == 8 or i == 9):
            if user_input[i] == 'D':
                number += 3
            elif user_input[i] == 'd':
                number += 2
            elif user_input[i]== 'a':
                number += 1
            elif user_input[i]  == 'A':
                number += 0
    return number 









