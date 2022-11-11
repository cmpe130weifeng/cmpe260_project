import random
from tkinter import *
from rock_paper_scissors_api import *

comp_score = 0
player_score = 0
number_of_tries = 0

def outcome_handler(user_choice):
    global comp_score
    global player_score
    global number_of_tries

    previous_choice = ''
    previous_result = ''
    if number_of_tries == 0:
        computer_choice = generate_random_choice()
        
        result = compete_board(user_choice, computer_choice)

        player_choice_label.config(fg="red", text="Player Choice: " + user_choice)
        computer_choice_label.config(fg="green", text="Computer Choice: " + computer_choice)

        player_score = show_score_human()
        player_score_label.config(text="Player: " + str(player_score)) 
        comp_score = show_score_computer()
        computer_score_label.config(text="Computer: " + str(comp_score))

        previous_choice = user_choice
        previous_result = result

    else:
        computer_choice = show_al_choice(previous_choice, user_choice, previous_result)
        result = compete_board(user_choice, computer_choice)

        player_choice_label.config(fg="red", text="Player Choice: " + user_choice)
        computer_choice_label.config(fg="green", text="Computer Choice: " + computer_choice)

        player_score = show_score_human()
        player_score_label.config(text="Player: " + str(player_score)) 
        comp_score = show_score_computer()
        computer_score_label.config(text="Computer: " + str(comp_score))

        previous_choice = user_choice
        previous_result = result
    
    number_of_tries += 1
    

master = Tk()
master.title("RPS")

Label(master, text="Rock, Paper, Scissors Game Against AI", font=("Calibri", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(master, text="Please Choose One Of Options To Start", font=("Calibri", 12)).grid(row=1, sticky=N, pady=10, padx=200)

player_score_label = Label(master, text="Player: 0", font=("Calibri", 12))
player_score_label.grid(row=2, sticky=W)

computer_score_label = Label(master, text="Computer: 0", font=("Calibri", 12))
computer_score_label.grid(row=2, sticky=E)

player_choice_label = Label(master, font=("Calibri, 12"))
player_choice_label.grid(row=3, sticky=W)

computer_choice_label = Label(master, font=("Calibri, 12"))
computer_choice_label.grid(row=3, sticky=E)

outcome_label = Label(master, font=("Calibri", 12))
outcome_label.grid(row=3, sticky=N)

Button(master, text="Rock", width=15, command=lambda: outcome_handler("R")).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text="Paper", width=15, command=lambda: outcome_handler("P")).grid(row=4, sticky=N, pady=5)
Button(master, text="Scissors", width=15, command=lambda: outcome_handler("S")).grid(row=4, sticky=E, padx=5, pady=5)

Label(master).grid(row=5)

master.mainloop()

