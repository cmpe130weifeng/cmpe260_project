# cmpe260_project
 </br>
Reinforcement Rock-Paper-Scissors AI with Image Recognition </br>
Team member: Weifeng Ma  </br>
</br>
The Rock-Paper-Scissor AI that implemented with a reinforcement mechanism. In this project, I will make the Rock-Paper-Scissors that apply the concept of reinforcement learning I learned from this class. I’ll implement the AI by using a reinforcement learning approach. To get better understanding of deep learning, I also implement image recognition that uses an image of rock/paper/scissors as input. The game itself will keep track of human choices and come up with the choice with the highest chance to win humans. </br>
</br>
Please use the RPS_Claasifier.ipynb to train the model, and save the pickle file for later usage. For training the model, you can get the dataset from: https://www.kaggle.com/datasets/sanikamal/rock-paper-scissors-dataset </br>
(If you don't have time, you can download the model directly from my driver: https://drive.google.com/file/d/1oCRw-rTHQlIpkf0qDMI9SdWJ0WOBJvLN/view?usp=share_link)
</br>
</br>
After you got the model, change the path of model in RPSgame.py to your path. </br>

```
checkpoint = torch.load('C:/Users/ray/Downloads/checkpoint.pth')
```

After you add model, run RPSgame.py. </br>
![output_screenshot](https://user-images.githubusercontent.com/32551600/202608327-851b5854-fab0-403f-9fd6-d9e4887f4047.png) </br>
Select an image from you device(R/P/S) to produce an input, and then click "Let's Play" to play the game.
</br>
</br>


