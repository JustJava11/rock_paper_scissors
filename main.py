from tkinter import *
from random import choice

root = Tk()
root.title('game')
root.geometry('800x500')
root.resizable(width=False, height=False)
root['bg'] = 'black'

def play_game(player_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(options)
    labelText.configure(text=f'Computer chose: {computer_choice}')
    check_winner(player_choice, computer_choice)

def check_winner(player, computer):
    if player == computer:
        result = "It's a Draw!"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"
    resultLabel.configure(text=result)

labelText = Label(root, text='', foreground='white', font=('Comic Sans MS', 20), background='black')
resultLabel = Label(root, text='', foreground='white', font=('Comic Sans MS', 20), background='black')

stone = Button(root,
               text='Rock',
               background='white',
               font=('Comic Sans MS', 20),
               command=lambda: play_game('Rock'))

paper = Button(root,
               text='Paper',
               background='white',
               font=('Comic Sans MS', 20),
               command=lambda: play_game('Paper'))

scissors = Button(root,
                  text='Scissors',
                  background='white',
                  font=('Comic Sans MS', 20),
                  command=lambda: play_game('Scissors'))

labelText.place(x=250, y=200)
resultLabel.place(x=320, y=160)
stone.place(x=200, y=300, width=120, height=60)
paper.place(x=340, y=300, width=120, height=60)
scissors.place(x=480, y=300, width=120, height=60)

root.mainloop()
