import random
import sys

# this library use for update winning rate of each round
from pip._vendor.distlib.compat import raw_input

human_score = 0
computer_score = 0
win_rate_of_RPS = [1/3,1/3,1/3] # store each round's winning rate

# dictionaries for each result's matrix
# the purpose of these matrixes is to keep track of each pairs and score
# and then we use them to update winning rate
# the initial value is 1, we need to use laplace smoothing
win_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}
tie_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}
lose_matrix = {'RR': 1, 'RP': 1, 'RS': 1, 'PR': 1, 'PP': 1, 'PS': 1, 'SR': 1, 'SP': 1, 'SS': 1}

# transition matrix, is used to calcuate the lose/win/tie rate
t_win_matrix = [[0,0,0],[0,0,0],[0,0,0]]
t_lose_matrix = [[0,0,0],[0,0,0],[0,0,0]]
t_tie_matrix = [[0,0,0],[0,0,0],[0,0,0]]

# this function used for updating the matrix(win,lose,tie)
def update_matrix(previous_choice, current_choice, result):
    if result == "w": # if the player won
        # every key is a pair(ex:PS); the first charater is previous choice
        # the scond charater is the current choice of the user
        for key, value in win_matrix.items():
            # if this key is what we want
            if ('%s%s' % (previous_choice, current_choice) == key):
                # so this key's value will add 1
                win_matrix['%s%s' % (previous_choice, current_choice)] += 1
    elif result == "t": # if the player tie
        for key, value in tie_matrix.items():
            if ('%s%s' % (previous_choice, current_choice) == key):
                tie_matrix['%s%s' % (previous_choice, current_choice)] += 1
    else: # if the player lost
        for key, value in lose_matrix.items():
            if ('%s%s' % (previous_choice, current_choice) == key):
                lose_matrix['%s%s' % (previous_choice, current_choice)] += 1

    return update_transition_matrix(result) # we need to update transition matrix

def update_transition_matrix(result): # result is last round's result
    # make it global for update the transition matrix
    global t_win_matrix
    global t_lose_matrix
    global t_tie_matrix

    if result == "w": # if the player won
        # we will calculate how likely the player will pick rock
        rock = win_matrix['RR'] + win_matrix['RS'] + win_matrix['RP']
        # same here, we calculate the percentage of selecting paper
        paper = win_matrix['PR'] + win_matrix['PS'] + win_matrix['PP']
        # calculate the percentage of selecting scissors
        scissors = win_matrix['SR'] + win_matrix['SS'] + win_matrix['SP']
        choice = ['R', 'P', 'S']
        # in the matrix, row = what would payer pick
        # column is what would the computer pick
        for row_index, whole_row in enumerate(t_win_matrix):
            for col_index, item in enumerate(whole_row):
                # calcuate the sum of each row
                a = int(win_matrix['%s%s' % (choice[row_index], choice[col_index])])
                if (row_index == 0): # if palyer select rock
                    c = a / rock # we calcuate winning rate of rock
                elif (row_index == 1): # if palyer select paper
                    c = a / paper # we calcuate winning rate of paper
                else: # if player select scissors
                    c = a / scissors # we calcuate wining rate of scissors
                whole_row[col_index] = float(c) # convert to float
        return (t_win_matrix)
    elif result == "t": # if the game is tie
        # same here, we update the matrix winning rate of each choices
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

    else: # if the player lost
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








