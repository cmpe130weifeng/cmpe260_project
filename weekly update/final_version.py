import random
import sys

from pip._vendor.distlib.compat import raw_input

human_score = 0
computer_score = 0
win_rate_of_RPS = [1/3,1/3,1/3]

# dictionaries for each result's matrix
win_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}
tie_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}
lose_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}

t_win_matrix = [[0,0,0],[0,0,0],[0,0,0]]
t_lose_matrix = [[0,0,0],[0,0,0],[0,0,0]]
t_tie_matrix = [[0,0,0],[0,0,0],[0,0,0]]

def generate_random_choice():
    computer_choice = random.choice(["R", "P", "S"]) # create a random choice
    print("Computer's choice is", computer_choice)
    return computer_choice

def prompt_choice():
    my_choice = raw_input("Enter you choice (R/P/S),"
                          "Or hit ENTER to quit: ").upper()
    if len(my_choice) > 1:
        print ("Error! Only 1 characters allowed!")
        sys.exit()
    if not my_choice:
        print("You quit the game.")
        sys.exit()
    if (my_choice == "R") or (my_choice=="S") or (my_choice=="P"):
        return my_choice
    else:
        print("Must be R/S/P!")
        #sys.exit()
        prompt_choice()

def compete_board(user_choice, AI_choice):
    global human_score
    global computer_score
    if(user_choice == "R" and AI_choice == "S"):
        human_score = human_score + 1
        return 'w'
    elif(user_choice == "S" and AI_choice == "P"):
        human_score = human_score + 1
        return 'w'
    elif (user_choice == "P" and AI_choice == "R"):
        human_score = human_score + 1
        return 'w'
    elif(user_choice == AI_choice):
        print("Game tie.")
        return 't'
    else:
        computer_score = computer_score + 1
        return 'l'

def update_matrix(previous_choice, current_choice, result):

    if result == "w":
        for key, value in win_matrix.items():
            if ('%s%s' % (previous_choice, current_choice) == key):
                win_matrix['%s%s' % (previous_choice, current_choice)] += 1
    elif result == "t":
        for key, value in tie_matrix.items():
            if ('%s%s' % (previous_choice, current_choice) == key):
                tie_matrix['%s%s' % (previous_choice, current_choice)] += 1
    else:
        for key, value in lose_matrix.items():
            if ('%s%s' % (previous_choice, current_choice) == key):
                lose_matrix['%s%s' % (previous_choice, current_choice)] += 1

    return update_transition_matrix(result)

def update_transition_matrix(result):
    global t_win_matrix
    global t_lose_matrix
    global t_tie_matrix

    if result == "w":
        rock = win_matrix['RR'] + win_matrix['RS'] + win_matrix['RP']
        paper = win_matrix['PR'] + win_matrix['PS'] + win_matrix['PP']
        scissors = win_matrix['SR'] + win_matrix['SS'] + win_matrix['SP']
        choice = ['R', 'P', 'S']
        for row_index, whole_row in enumerate(t_win_matrix):
            for col_index, item in enumerate(whole_row):
                a = int(win_matrix['%s%s' % (choice[row_index], choice[col_index])])
                if (row_index == 0):
                    c = a / rock
                elif (row_index == 1):
                    c = a / paper
                else:
                    c = a / scissors
                whole_row[col_index] = float(c)
        return (t_win_matrix)
    elif result == "t":
        rock = tie_matrix['RR'] + tie_matrix['RS'] + tie_matrix['RP']
        paper = tie_matrix['PR'] + tie_matrix['PS'] + tie_matrix['PP']
        scissors = tie_matrix['SR'] + tie_matrix['SS'] + tie_matrix['SP']
        choice = ['R', 'P', 'S']
        for row_index, whole_row in enumerate(t_tie_matrix):
            for col_index, item in enumerate(whole_row):
                a = int(tie_matrix['%s%s' % (choice[row_index], choice[col_index])])
                if (row_index == 0):
                    c = a / rock
                elif (row_index == 1):
                    c = a / paper
                else:
                    c = a / scissors
                whole_row[col_index] = float(c)
        return (t_tie_matrix)

    else:
        rock = lose_matrix['RR'] + lose_matrix['RS'] + lose_matrix['RP']
        paper = lose_matrix['PR'] + lose_matrix['PS'] + lose_matrix['PP']
        scissors = lose_matrix['SR'] + lose_matrix['SS'] + lose_matrix['SP']
        choice = ['R', 'P', 'S']
        for row_index, whole_row in enumerate(t_lose_matrix):
            for col_index, item in enumerate(whole_row):
                a = int(lose_matrix['%s%s' % (choice[row_index], choice[col_index])])
                if (row_index == 0):
                    c = a / rock
                elif (row_index == 1):
                    c = a / paper
                else:
                    c = a / scissors
                whole_row[col_index] = float(c)
        return (t_lose_matrix)

def rps_machine_learning():
    global win_rate_of_RPS
    previous_choice = ''

    user_choice = prompt_choice()
    computer_choice = generate_random_choice()
    result = compete_board(user_choice, computer_choice)
    show_score()
    previous_choice = user_choice

    while(1):
        if(previous_choice == 'R'):
            temp = 0
        elif(previous_choice == 'P'):
            temp = 1
        else:
            temp = 2
        user_choice = prompt_choice()

        transMatrix = update_matrix(previous_choice, user_choice, result)
        machineChoice_range = random.randint(1, 100)
        win_rate_of_RPS[0] = transMatrix[temp][0]
        win_rate_of_RPS[1] = transMatrix[temp][1]
        win_rate_of_RPS[2] = transMatrix[temp][2]
        rangeR = win_rate_of_RPS[0] * 100
        rangeP = win_rate_of_RPS[1] * 100 + rangeR
        if (machineChoice_range <= rangeR):
            AI_choice = 'P'
        elif (machineChoice_range <= rangeP):
            AI_choice = 'S'
        else:
            AI_choice = 'R'

        print("Computer's choice is", AI_choice)
        result = compete_board(user_choice, AI_choice)
        show_score()
        previous_choice = user_choice


def show_score():
    global human_score
    global computer_score
    print("Human score is", human_score)
    print("Computer score is", computer_score)

def main():
    rps_machine_learning()


main()
