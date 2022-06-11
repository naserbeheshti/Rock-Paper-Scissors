import random
import tkinter as tk
from tkinter import ttk


class Player:
    def __init__(self, player_name, player_score):
        self.name = player_name
        self.score = player_score
        self.human_selection = None

    def save_player(self):
        f1 = open(self.name, "w")
        f1.write(self.name + " : " + str(self.score))
        f1.close()

    def play_round(self, human_selection):
        if self.human_selection is None:
            my_list = [1, 2, 3]
            x = random.choice(my_list)
            return x
        elif self.human_selection is not None:
            return self.human_selection

    def calc_score(self, selection, other1, other2):
        if selection == 1 and other1 != 3 and other2 != 3:
            self.score = self.score + 1
            self.save_player()
            return None
        if selection == 2 and other1 != 1 and other2 != 1:
            self.score = self.score + 1
            self.save_player()
            return None
        if selection == 3 and other1 != 1 and other2 != 1:
            self.score = self.score + 1
            self.save_player()
            return None


# root window
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title('Stone game')

# title label with a specific font
label = tk.Label(
    root,
    text='Stone Game by Naser Beheshti',
    font=("Helvetica", 14),
)

label.pack(ipadx=10, ipady=10)

# get player name
name = tk.StringVar()

global i
v = tk.StringVar(root, "1")
Player1 = Player("Human", 0)
Player2 = Player("AI1", 0)
Player3 = Player("AI2", 0)
global m
m = [3]
global players


def set_radio():
    pass


round_counter = 0


def play_clicked():
    """ callback when the login button clicked
    """
    # result_label.config(text=name.get())
    # m.clear()
    Player1.name = name.get()
    m.append(Player1.play_round(v))
    m.append(Player2.play_round(None))
    m.append(Player3.play_round(None))
    m.sort()
    Player1.calc_score(m[0], m[1], m[2])
    Player2.calc_score(m[1], m[0], m[2])
    Player3.calc_score(m[2], m[0], m[1])
    m.clear()
    players = [
        [Player1.name, Player1.score],
        [Player2.name, Player2.score],
        [Player3.name, Player3.score]
    ]
    players.sort(key=lambda x: x[1])

    result_label.config(text=
                        str(round_counter) + "/n" +
                        players[2][0] + " : " + str(players[2][1]) + " " +
                        players[1][0] + " : " + str(players[1][1]) + " " +
                        players[0][0] + " : " + str(players[0][1]))
    players.clear()


# action frame
play = ttk.Frame(root)
play.pack(padx=10, pady=10, fill='x', expand=True)
r1 = ttk.Radiobutton(play, text="Stone  ", variable=v, value=1, command=set_radio())
r1.pack()
r2 = ttk.Radiobutton(play, text="Scissor", variable=v, value=2, command=set_radio())
r2.pack()
r3 = ttk.Radiobutton(play, text="Paper  ", variable=v, value=3, command=set_radio())
r3.pack()

# Name
name_label = ttk.Label(play, text="Your Name :")
name_label.pack(fill='x', expand=True)

name_entry = ttk.Entry(play, textvariable=name)
name_entry.pack(fill='x', expand=True)
name_entry.focus()

# play button
play_button = ttk.Button(play, text="Play", command=play_clicked)
play_button.pack(fill='x', expand=True, pady=10)

# result label
result_label = tk.Label(
    root,
    text='',
)

result_label.pack(ipadx=10, ipady=10)

root.mainloop()
