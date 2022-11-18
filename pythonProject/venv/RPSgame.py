from tkinter import *
from PIL import Image, ImageTk
import random
from random import randint
from tkinter import ttk # use ttk widgets
from tkinter import filedialog
from CNNmodel import *
from image_reshape import *
from algorithm import *

model = RPSCNN()
checkpoint = torch.load('C:/Users/ray/Downloads/checkpoint.pth')
model.load_state_dict(checkpoint)
dic={0:"R",1:"P",2:"S"}

def compete_board(user_choice, computer_choice):
    global human_score
    global computer_score
    if(user_choice == "R" and computer_choice == "S"):
        human_score = human_score + 1
        outcome_label.config(fg="black", text="win!")
        return 'w'
    elif(user_choice == "S" and computer_choice == "P"):
        human_score = human_score + 1
        outcome_label.config(fg="black", text="win!")
        return 'w'
    elif (user_choice == "P" and computer_choice == "R"):
        human_score = human_score + 1
        outcome_label.config(fg="black", text="win!")
        return 'w'
    elif(user_choice == computer_choice):
        outcome_label.config(fg="black", text="Tie!")
        return 't'
    else:
        computer_score = computer_score + 1
        outcome_label.config(fg="black", text="lost!")
        return 'l'

counter = 0
result_temp = ''
previous_choice_temp = ''
user_choice = ''
computer_choice = ''
def outcome_handler():
    global win_rate_of_RPS
    global result_temp
    global counter
    global previous_choice_temp
    global computer_choice
    if counter == 0:
        computer_choice = random.choice(["R", "P", "S"])
        counter = counter + 1
        # check win/lose
        result_temp = compete_board(user_choice, computer_choice)
        previous_choice_temp = user_choice
    else:
        if (previous_choice_temp == 'R'):
            position = 0
        elif (previous_choice_temp == 'P'):
            position = 1
        else:
            position = 2

        transMatrix = update_matrix(previous_choice_temp, user_choice, result_temp)
        machineChoice_range = random.randint(1, 100) # create a random number
        win_rate_of_RPS[0] = transMatrix[position][0] # calcuate winning rate of R
        win_rate_of_RPS[1] = transMatrix[position][1] # calcuate winning rate of P
        win_rate_of_RPS[2] = transMatrix[position][2] # calcuate winning rate of S
        rangeR = win_rate_of_RPS[0] * 100 # convert to %
        rangeP = win_rate_of_RPS[1] * 100 + rangeR
        # if random choice's wining rate < palyer's R slection
        if (machineChoice_range <= rangeR):
            computer_choice = 'P' # AI pick P
        elif (machineChoice_range <= rangeP): # if random choice's wining rate < palyer's P slection
            computer_choice = 'S' # AI pick S
        else: #if random choice's wining rate >  palyer's S slection
            computer_choice = 'R'
        # check win/lose
        result_temp = compete_board(user_choice, computer_choice)
        previous_choice_temp = user_choice

    # show the choices to the screen
    computer_choice_label.config(fg="red",
                           text="Computer choice: " + str(computer_choice))
    player_choice_label.config(fg="red",
                           text="Player choice: " + str(user_choice))

    # show the scores
    human_score_label.config(fg="black", text="Player score: "+ str(human_score))
    computer_score_label.config(fg="black", text="Computer score: "+ str(computer_score))


def open():
    global my_image
    global user_choice
    f_types = [('PNG Files', '*.png'), ('Jpg Files', '*.jpg')]  # all files = ("all files, "*.*")
    window.fileName = filedialog.askopenfilename(filetypes=f_types,
                                               title="select a file",
                                               initialdir="c:/Users/ray/Downloads/Rock-Paper-Scissors")
    # resize the image
    image = Image.open(window.fileName)
    image = image.resize((200,200), Image.ANTIALIAS)
    # show the image
    my_image = ImageTk.PhotoImage(image)
    my_image_label = Label(image = my_image) # create space for showing image
    my_image_label.grid(row=3, sticky=N)
    # rps label text (true label)
    original_label, input_image = reshape_image(window.fileName)
    rps_label = Label(window, text="Original label: " + original_label)
    rps_label.grid(row=4, sticky=N)
    # rps label text (predicted label)
    outputs = model(input_image)
    _,predictions = torch.max(outputs.data,1)
    predictions=predictions.detach().numpy()
    rps_label2 = Label(window, text="Predicted label: " + dic[predictions[0]])
    rps_label2.grid(row=5, sticky=N)
    user_choice = dic[predictions[0]]

window = Tk()
window.title("RPS Game")
#window.geometry("800x600")
window.iconbitmap("rps.ico") # path to banner

# text in screen
# stickly N = center of the screen
# pady = spaces
# padx = how big your label
Label(window, text="Rock, Paper, Scissors Game Against AI",
      bg="yellow", fg="black",
      font=("Calibri", 14, "bold")).grid(row=0, sticky=N, pady=10, padx=200)
Label(window, text="Select an image & run the model", width=30,
      font=("Calibri", 12)).grid(row=1, sticky=N, pady=10, padx=200)

# button text
Button(window, text="Select an image", width=15,
       command=open).grid(row=2, sticky=N, padx=5, pady=5)

# score of player
human_score_label = Label(window, text="default message", font=("Calibri", 12))
human_score_label.grid(row=8, sticky=W)
# score of computer
computer_score_label = Label(window, text="default message", font=("Calibri", 12))
computer_score_label.grid(row=8, sticky=E)

# text for showing the choices
player_choice_label = Label(window, font=("Calibri, 12"))
player_choice_label.grid(row=7, sticky=W)
computer_choice_label = Label(window, font=("Calibri, 12"))
computer_choice_label.grid(row=7, sticky=E)

# text for showing "loss/win"
outcome_label = Label(window, font=("Calibri", 12))
outcome_label.grid(row=7, sticky=N)

# play
# text = button's discription
Button(window, text="Let's Play", width=15,
       command=lambda: outcome_handler()).grid(row=6, sticky=N, padx=5, pady=5)

# extra space
Label(window).grid(row=9)

window.mainloop()