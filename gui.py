import tkinter as tk
from tkinter import font as f
import tkinter.scrolledtext as st
from tkinter import *
from tkinter import messagebox
from methods import *

LARGE_FONT = ("Bradley Hand ITC", 15, 'bold')
pink = "#FF10F0"
black = "black"
white = 'white'
grey = "lightgrey"
lightgrey = "#D3D3D3"
game_dict = {"Level2": {"theme": "red", "digits": 2, "guesses": 6, "score": 10},
             "Level3": {"theme": "blue", "digits": 3, "guesses": 10, "score": 15},
             "Level4": {"theme": "yellow", "digits": 4, "guesses": 14, "score": 20},
             "Level5": {"theme": "green", "digits": 5, "guesses": 20, "score": 25},
             "Level6": {"theme": "orange", "digits": 6, "guesses": 25, "score": 30},
             "Level7": {"theme": "purple", "digits": 7, "guesses": 32, "score": 40}}

#Set scores. Save Scores in a database for Highscore
#For every Bagel, -2, Pico, 0, Fermi, +1,highest score that can ever be attained 226
#Breakdown Guess button into smaller functions
#Update the other frames
#Try inheritance to create only one game page

class BagelsGame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RulePage, GameOptionPage, Page2, Page3, Page4, Page5, Page6, Page7):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.controller.title("Bagels Game")
        self.controller.geometry("600x600")
        self.controller.attributes("-alpha", 0.8)
        self.controller.resizable(False, False)
        self.bagel_font = f.Font(family='bauhaus 93', size=50, weight='normal')
        self.start_widgets()

    def start_widgets(self):
        self.space_lbl = Label(self, height=4, bg=black)
        self.space_lbl.pack()

        self.game_lbl = Label(self, text='BAGELS', font=self.bagel_font, bg=black, fg=white)
        self.game_lbl.pack(pady=10)

        self.rule_lbl = Label(self, text='The rules are simple. Click to View >>>', font='Ebrima 15 bold', bg=black,
                              fg=white, cursor="hand2")
        self.rule_lbl.pack(pady=10)
        self.rule_lbl.bind("<Button>", lambda e: self.controller.show_frame(RulePage))

        self.play_lbl = Label(self, text='<<< PRESS PLAY >>>', font='fixedsys 20 bold', bg=black, fg=white,
                              cursor="hand2")
        self.play_lbl.pack(pady=60)
        self.play_lbl.bind("<Button>", lambda e: self.controller.show_frame(GameOptionPage))

        self.exit_lbl = Label(self, text="<< QUIT >>", font='fixedsys 16 bold', bg=black, fg=white, cursor="hand2")
        self.exit_lbl.pack()
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())


class RulePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.rulepage_widgets()

    def rulepage_widgets(self):
        self.rule_lbl_frame = LabelFrame(self, text="About Bagels", height=50, width=60, bg=black,
                                         font='Ebrima 18 bold', fg=white)
        self.rule_lbl_frame.pack(padx=30, pady=20)

        self.rule_lbl = Label(self.rule_lbl_frame,
                              text='Bagels, a deductive logic game. '
                                   '\nBy Al Sweigart al@inventwithpython.com. '
                                   '\n\nI am thinking of a number with no repeated digits. '
                                   '\nTry to guess what it is. '
                                   '\n\nHere are some clues: '
                                   '\nPico - One digit is correct but in the wrong position. '
                                   '\nFermi - One digit is correct and in the right position. '
                                   '\nBagels - No digit is correct. '
                                   '\nFor example; '
                                   '\nIf, secret number - 248'
                                   '\nguess - 843...'
                                   '\nclues would be 1 Fermi 1 Pico.',
                              font=LARGE_FONT, fg=white, justify=LEFT, bg=black)
        self.rule_lbl.pack(pady=20, padx=20)

        self.play_lbl = Label(self, text="<<< PRESS PLAY >>>", font='fixedsys 20 bold', bg=black, fg=white,
                              cursor="hand2")
        self.play_lbl.pack(pady=20)
        self.play_lbl.bind("<Button>", lambda e: self.controller.show_frame(GameOptionPage))

        self.exit_lbl = Label(self, text="<< QUIT >>", font='fixedsys 16 bold', bg=black, fg=white, )
        self.exit_lbl.pack(pady=8)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())


class GameOptionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        self.option_widgets()

    def option_widgets(self):
        self.go_lbl1 = Label(self, text="Select Game Mode", font='Ebrima 25 bold', bg="black", fg=white)
        self.go_lbl1.pack(pady=20)
        self.miniframe = Frame(self, bg="black")
        self.miniframe.pack(padx=10, pady=10)

        self.btn2 = Button(self.miniframe,
                           text=f'{game_dict["Level2"]["digits"]} Digits\n{game_dict["Level2"]["guesses"]} guesses',
                           font="SitkaText 16 bold", bg=game_dict["Level2"]["theme"],
                           height=8, width=12, command=lambda: self.controller.show_frame(Page2))
        self.btn2.grid(row=0, column=0, padx=4, pady=6)
        self.changeOnHover(self.btn2, game_dict["Level2"]["theme"])

        self.btn3 = Button(self.miniframe,
                           text=f'{game_dict["Level3"]["digits"]} Digits\n{game_dict["Level3"]["guesses"]} guesses',
                           font="SitkaText 16 bold", bg=game_dict["Level3"]["theme"],
                           height=8, width=12, command=lambda: self.controller.show_frame(Page3))
        self.btn3.grid(row=0, column=1, padx=4, pady=6)
        self.changeOnHover(self.btn3, game_dict["Level3"]["theme"])

        self.btn4 = Button(self.miniframe,
                           text=f'{game_dict["Level4"]["digits"]} Digits\n{game_dict["Level4"]["guesses"]} guesses',
                           font="SitkaText 16 bold", bg=game_dict["Level4"]["theme"],
                           height=8, width=12, command=lambda: self.controller.show_frame(Page4))
        self.btn4.grid(row=0, column=2, padx=4, pady=6)
        self.changeOnHover(self.btn4, game_dict["Level4"]["theme"])

        self.btn5 = Button(self.miniframe,
                           text=f'{game_dict["Level5"]["digits"]} Digits\n{game_dict["Level5"]["guesses"]} guesses',
                           font="SitkaText 16 bold", bg=game_dict["Level5"]["theme"],
                           height=8, width=12, command=lambda: self.controller.show_frame(Page5))
        self.btn5.grid(row=1, column=0, padx=4, pady=6)
        self.changeOnHover(self.btn5, game_dict["Level5"]["theme"])

        self.btn6 = Button(self.miniframe,
                           text=f'{game_dict["Level6"]["digits"]} Digits\n{game_dict["Level6"]["guesses"]} guesses',
                           font="SitkaText 16 bold", bg=game_dict["Level6"]["theme"],
                           height=8, width=12, command=lambda: self.controller.show_frame(Page6))
        self.btn6.grid(row=1, column=1, padx=4, pady=6)
        self.changeOnHover(self.btn6, game_dict["Level6"]["theme"])

        self.btn7 = Button(self.miniframe,
                           text=f'{game_dict["Level7"]["digits"]} Digits\n{game_dict["Level7"]["guesses"]} guesses',
                           font="SitkaText 16 bold", bg=game_dict["Level7"]["theme"],
                           height=8, width=12, command=lambda: self.controller.show_frame(Page7))
        self.btn7.grid(row=1, column=2, padx=4, pady=6)
        self.changeOnHover(self.btn7, game_dict["Level7"]["theme"])

        self.exit_game = Label(self.miniframe, text="<<< Return to Home >>> ",
                               font="fixedsys 16 normal", fg=white, bg="black", cursor="hand2")
        self.exit_game.grid(row=2, column=0, columnspan=3, sticky=E, pady=5)
        self.exit_game.bind("<Button>", lambda e: self.controller.show_frame(StartPage))

    # function to change properties of button on hover
    def changeOnHover(self, button, leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=black, foreground=leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=leave_color, foreground=black))


class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.btn_font = f.Font(family='Modern No. 20', size=22, weight='bold')
        self.top_btn_font = f.Font(family='Modern No. 20', size=14, weight='bold')
        self.text_font = ("Ebrima", 12, 'bold')
        self.entry_font = ("Ebrima", 50, 'bold')
        self.guess_input = StringVar()
        self.score = 0
        self.btn_width = 4
        self.entry_width = game_dict["Level2"]["digits"]
        self.entry_font_color = game_dict["Level2"]["theme"]
        self.digits = game_dict["Level2"]["digits"]
        self.max_guesses = game_dict["Level2"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.game_widgets()

    def reset_game(self):
        self.score = 0
        self.max_guesses = game_dict["Level2"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.reset_widgets()

    def reset_widgets(self):
        self.guess_entry.delete(0, END)
        self.text_view.delete('1.0', END)
        self.guess_btn.config(state="normal")
        self.guess_entry.config(state="normal")
        self.score_lbl.config(text=f"Score: {self.score}")
        self.guess_lbl.config(text=f'Guesses left: {game_dict["Level2"]["guesses"]}', fg=white)

    def button_replay(self):
        self.reset_game()

    def button_back(self):
        self.guess_entry.delete(0)

    def num_button_click(self, num):
        current = self.guess_entry.get()
        self.guess_entry.delete(0, END)
        self.guess_entry.insert(0, str(current) + str(num))

    def button_clear(self):
        self.guess_entry.delete(0, END)

    def update_score(self, clues):
        if clues == "Bagels":
            self.score -= 2
        else:
            for i in clues.split(" "):
                if i == "Fermi":
                    self.score += 1
        self.score_lbl.config(text=f"Score: {self.score}")

    def win_score(self):
        self.score += game_dict["Level2"]["score"]
        self.score_lbl.config(text=f"Score: {self.score}")

    def game_end_action(self):
        self.guess_btn.config(state="disabled")
        self.guess_entry.config(state="disabled")

    def validate_guess(self, entry):
        if len(entry) >= self.digits:
            guess = entry[:self.digits]
            return guess
        else:
            return False

    def max_guess_counter(self):
        self.max_guesses -= 1
        self.guess_lbl.config(text=f"Guesses left: {self.max_guesses}")

    def max_guess_check(self):
        if self.max_guesses == 2:
            self.guess_lbl.config(fg="red")
        elif self.max_guesses == 0:
            self.text_view.insert(END, f"Out of Guesses\nSecret Number is {self.secret_num}")
            self.game_end_action()

    def guess_status(self, guess):
        if check_guess(guess, self.secret_num):
            return "win"
        else:
            clues = clues_generator(guess, self.secret_num)
            self.text_view.insert(END, f"{guess}\n{clues}\n\n")
            return clues

    def guess_action(self, entry):
        guess = self.validate_guess(entry)
        if guess is not False:
            self.button_clear()
            self.max_guess_counter()
            clues = self.guess_status(guess)
            if clues == "win":
                self.win_score()
                self.text_view.insert(END, f"{guess} is correct!\n")
                self.game_end_action()
            else:
                self.update_score(clues)
                self.max_guess_check()
        else:
            messagebox.showwarning('Bagels Game', f'Must make a {self.digits} digit guess')

    def guess_btn_action(self):
        entry = self.guess_entry.get()
        self.guess_action(entry)

    def changeOnHover(self, button, leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=black, foreground=leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=leave_color, foreground=black))

    def game_widgets(self):
        self.main_frame = Frame(self, bg=black)
        self.main_frame.pack()

        self.right_frame = Frame(self.main_frame, bg=black, bd=4, pady=8)
        self.right_frame.pack(side=RIGHT, anchor=S, padx=8, pady=4)

        self.left_frame = Frame(self.main_frame, bg=black, padx=6)
        self.left_frame.pack(side=LEFT, anchor=N)

        self.guess_frame = Frame(self.left_frame, bg=black, padx=4)
        self.guess_frame.pack(side=BOTTOM, anchor=S, pady=6)

        self.top_frame = Frame(self.left_frame, bg=black)
        self.top_frame.pack(side=TOP, fill='x')
        self.mid_frame = Frame(self.left_frame, bg=black)
        self.mid_frame.pack(pady=30)
        self.num_frame = Frame(self.left_frame, bg=black)
        self.num_frame.pack(padx=2, pady=18)

        self.top_btn_frame = Label(self.right_frame, bg=black)
        self.top_btn_frame.pack(side=TOP)

        self.replay_btn = Button(self.top_btn_frame, text="REPLAY", font=self.top_btn_font, padx=14,
                                 command=self.button_replay)
        self.replay_btn.grid(row=0, column=0, padx=2)
        self.changeOnHover(self.replay_btn, "white")

        self.mode_btn = Button(self.top_btn_frame, text="Mode", font=self.top_btn_font, padx=14,
                               command=lambda: self.controller.show_frame(GameOptionPage))
        self.mode_btn.grid(row=0, column=1, padx=2)
        self.changeOnHover(self.mode_btn, "white")

        self.text_view = st.ScrolledText(self.right_frame, bg=lightgrey, fg=game_dict["Level2"]["theme"],width=18, height=20, borderwidth=3,
                                         font=LARGE_FONT)
        self.text_view.pack()

        self.exit_lbl = Label(self.right_frame, text="<< Exit >>", bg=black, fg=white, font='fixedsys 14 bold',
                              cursor="hand2")
        self.exit_lbl.pack(anchor=SE, pady=3)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())

        # ============================================================================================================

        self.guess_lbl = Label(self.top_frame, text=f'Guesses left: {game_dict["Level2"]["guesses"]}', fg=white, font=self.text_font, bg=black)
        self.guess_lbl.pack(side=LEFT, padx=4)

        self.score_lbl = Label(self.top_frame, text=f"Score: {self.score}", fg=white, font=self.text_font, bg=black)
        self.score_lbl.pack(side=RIGHT, padx=4)

        self.lbl1 = Label(self.mid_frame, text="Enter Your Guess: ", bg=black, fg=white, font="Ebrima 22 bold")
        self.lbl1.pack(padx=5, pady=10)

        self.guess_entry = Entry(self.mid_frame, textvariable=self.guess_input, fg=self.entry_font_color,
                                 width=self.entry_width,
                                 font=self.entry_font, borderwidth=4, insertontime=0)
        self.guess_entry.pack()
        self.guess_entry.bind("<Key>", func=lambda e: "break")

        # ======================================================================================================================================

        self.bt0 = Button(self.num_frame, text="0", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(0))
        self.bt0.grid(row=0, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt0, "white")

        self.bt1 = Button(self.num_frame, text="1", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(1))
        self.bt1.grid(row=0, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt1, "white")

        self.bt2 = Button(self.num_frame, text="2", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(2))
        self.bt2.grid(row=0, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt2, "white")

        self.bt3 = Button(self.num_frame, text="3", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(3))
        self.bt3.grid(row=0, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt3, "white")

        self.bt4 = Button(self.num_frame, text="4", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(4))
        self.bt4.grid(row=1, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt4, "white")

        self.bt5 = Button(self.num_frame, text="5", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(5))
        self.bt5.grid(row=1, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt5, "white")

        self.bt6 = Button(self.num_frame, text="6", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(6))
        self.bt6.grid(row=1, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt6, "white")

        self.bt7 = Button(self.num_frame, text="7", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(7))
        self.bt7.grid(row=1, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt7, "white")

        self.bt8 = Button(self.num_frame, text="8", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(8))
        self.bt8.grid(row=2, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt8, "white")

        self.bt9 = Button(self.num_frame, text="9", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(9))
        self.bt9.grid(row=2, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt9, "white")

        self.clr_btn = Button(self.num_frame, text="CLR", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                              width=self.btn_width, height=1, command=lambda: self.button_clear())
        self.clr_btn.grid(row=2, column=2, padx=1, pady=1)
        self.changeOnHover(self.clr_btn, "white")

        self.back_btn = Button(self.num_frame, text="", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                               width=self.btn_width, height=1, command=self.button_back)
        self.back_btn.grid(row=2, column=3, padx=1, pady=1)
        self.changeOnHover(self.back_btn, "white")

        self.guess_btn = Button(self.guess_frame, text="Guess", relief="raised", bd=2, bg=grey, fg=black,
                                font=self.btn_font, width=18, command=self.guess_btn_action)
        self.guess_btn.pack()
        self.changeOnHover(self.guess_btn, "white")


class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.btn_font = f.Font(family='Modern No. 20', size=22, weight='bold')
        self.top_btn_font = f.Font(family='Modern No. 20', size=14, weight='bold')
        self.text_font = ("Ebrima", 12, 'bold')
        self.entry_font = ("Ebrima", 50, 'bold')
        self.guess_input = StringVar()
        self.score = 0
        self.btn_width = 4
        self.entry_width = game_dict["Level3"]["digits"]
        self.entry_font_color = game_dict["Level3"]["theme"]
        self.digits = game_dict["Level3"]["digits"]
        self.max_guesses = game_dict["Level3"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.game_widgets()

    def reset_game(self):
        self.score = 0
        self.max_guesses = game_dict["Level3"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.reset_widgets()

    def reset_widgets(self):
        self.guess_entry.delete(0, END)
        self.text_view.delete('1.0', END)
        self.guess_btn.config(state="normal")
        self.guess_entry.config(state="normal")
        self.score_lbl.config(text=f"Score: {self.score}")
        self.guess_lbl.config(text=f'Guesses left: {game_dict["Level3"]["guesses"]}', fg=white)

    def button_replay(self):
        self.reset_game()

    def button_back(self):
        self.guess_entry.delete(0)

    def num_button_click(self, num):
        current = self.guess_entry.get()
        self.guess_entry.delete(0, END)
        self.guess_entry.insert(0, str(current) + str(num))

    def button_clear(self):
        self.guess_entry.delete(0, END)

    def update_score(self, clues):
        if clues == "Bagels":
            self.score -= 2
        else:
            for i in clues.split(" "):
                if i == "Fermi":
                    self.score += 1
        self.score_lbl.config(text=f"Score: {self.score}")

    def win_score(self):
        self.score += game_dict["Level3"]["score"]
        self.score_lbl.config(text=f"Score: {self.score}")

    def game_end_action(self):
        self.guess_btn.config(state="disabled")
        self.guess_entry.config(state="disabled")

    def validate_guess(self, entry):
        if len(entry) >= self.digits:
            guess = entry[:self.digits]
            return guess
        else:
            return False

    def max_guess_counter(self):
        self.max_guesses -= 1
        self.guess_lbl.config(text=f"Guesses left: {self.max_guesses}")

    def max_guess_check(self):
        if self.max_guesses == 2:
            self.guess_lbl.config(fg="red")
        elif self.max_guesses == 0:
            self.text_view.insert(END, f"Out of Guesses\nSecret Number is {self.secret_num}")
            self.game_end_action()

    def guess_status(self, guess):
        if check_guess(guess, self.secret_num):
            return "win"
        else:
            clues = clues_generator(guess, self.secret_num)
            self.text_view.insert(END, f"{guess}\n{clues}\n\n")
            return clues

    def guess_action(self, entry):
        guess = self.validate_guess(entry)
        if guess is not False:
            self.button_clear()
            self.max_guess_counter()
            clues = self.guess_status(guess)
            if clues == "win":
                self.win_score()
                self.text_view.insert(END, f"{guess} is correct!\n")
                self.game_end_action()
            else:
                self.update_score(clues)
                self.max_guess_check()
        else:
            messagebox.showwarning('Bagels Game', f'Must make a {self.digits} digit guess')

    def guess_btn_action(self):
        entry = self.guess_entry.get()
        self.guess_action(entry)

    def changeOnHover(self, button, leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=black, foreground=leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=leave_color, foreground=black))

    def game_widgets(self):
        self.main_frame = Frame(self, bg=black)
        self.main_frame.pack()

        self.right_frame = Frame(self.main_frame, bg=black, bd=4, pady=8)
        self.right_frame.pack(side=RIGHT, anchor=S, padx=8, pady=4)

        self.left_frame = Frame(self.main_frame, bg=black, padx=6)
        self.left_frame.pack(side=LEFT, anchor=N)

        self.guess_frame = Frame(self.left_frame, bg=black, padx=4)
        self.guess_frame.pack(side=BOTTOM, anchor=S, pady=6)

        self.top_frame = Frame(self.left_frame, bg=black)
        self.top_frame.pack(side=TOP, fill='x')
        self.mid_frame = Frame(self.left_frame, bg=black)
        self.mid_frame.pack(pady=30)
        self.num_frame = Frame(self.left_frame, bg=black)
        self.num_frame.pack(padx=2, pady=18)

        self.top_btn_frame = Label(self.right_frame, bg=black)
        self.top_btn_frame.pack(side=TOP)

        self.replay_btn = Button(self.top_btn_frame, text="REPLAY", font=self.top_btn_font, padx=14,
                                 command=self.button_replay)
        self.replay_btn.grid(row=0, column=0, padx=2)
        self.changeOnHover(self.replay_btn, "white")

        self.mode_btn = Button(self.top_btn_frame, text="Mode", font=self.top_btn_font, padx=14,
                               command=lambda: self.controller.show_frame(GameOptionPage))
        self.mode_btn.grid(row=0, column=1, padx=2)
        self.changeOnHover(self.mode_btn, "white")

        self.text_view = st.ScrolledText(self.right_frame, bg=lightgrey, fg=game_dict["Level3"]["theme"],width=18, height=20, borderwidth=3,
                                         font=LARGE_FONT)
        self.text_view.pack()

        self.exit_lbl = Label(self.right_frame, text="<< Exit >>", bg=black, fg=white, font='fixedsys 14 bold',
                              cursor="hand2")
        self.exit_lbl.pack(anchor=SE, pady=3)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())

        # ============================================================================================================

        self.guess_lbl = Label(self.top_frame, text=f'Guesses left: {game_dict["Level3"]["guesses"]}', fg=white, font=self.text_font, bg=black)
        self.guess_lbl.pack(side=LEFT, padx=4)

        self.score_lbl = Label(self.top_frame, text=f"Score: {self.score}", fg=white, font=self.text_font, bg=black)
        self.score_lbl.pack(side=RIGHT, padx=4)

        self.lbl1 = Label(self.mid_frame, text="Enter Your Guess: ", bg=black, fg=white, font="Ebrima 22 bold")
        self.lbl1.pack(padx=5, pady=10)

        self.guess_entry = Entry(self.mid_frame, textvariable=self.guess_input, fg=self.entry_font_color,
                                 width=self.entry_width,
                                 font=self.entry_font, borderwidth=4, insertontime=0)
        self.guess_entry.pack()
        self.guess_entry.bind("<Key>", func=lambda e: "break")

        # ======================================================================================================================================

        self.bt0 = Button(self.num_frame, text="0", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(0))
        self.bt0.grid(row=0, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt0, "white")

        self.bt1 = Button(self.num_frame, text="1", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(1))
        self.bt1.grid(row=0, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt1, "white")

        self.bt2 = Button(self.num_frame, text="2", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(2))
        self.bt2.grid(row=0, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt2, "white")

        self.bt3 = Button(self.num_frame, text="3", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(3))
        self.bt3.grid(row=0, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt3, "white")

        self.bt4 = Button(self.num_frame, text="4", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(4))
        self.bt4.grid(row=1, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt4, "white")

        self.bt5 = Button(self.num_frame, text="5", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(5))
        self.bt5.grid(row=1, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt5, "white")

        self.bt6 = Button(self.num_frame, text="6", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(6))
        self.bt6.grid(row=1, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt6, "white")

        self.bt7 = Button(self.num_frame, text="7", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(7))
        self.bt7.grid(row=1, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt7, "white")

        self.bt8 = Button(self.num_frame, text="8", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(8))
        self.bt8.grid(row=2, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt8, "white")

        self.bt9 = Button(self.num_frame, text="9", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(9))
        self.bt9.grid(row=2, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt9, "white")

        self.clr_btn = Button(self.num_frame, text="CLR", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                              width=self.btn_width, height=1, command=lambda: self.button_clear())
        self.clr_btn.grid(row=2, column=2, padx=1, pady=1)
        self.changeOnHover(self.clr_btn, "white")

        self.back_btn = Button(self.num_frame, text="", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                               width=self.btn_width, height=1, command=self.button_back)
        self.back_btn.grid(row=2, column=3, padx=1, pady=1)
        self.changeOnHover(self.back_btn, "white")

        self.guess_btn = Button(self.guess_frame, text="Guess", relief="raised", bd=2, bg=grey, fg=black,
                                font=self.btn_font, width=18, command=self.guess_btn_action)
        self.guess_btn.pack()
        self.changeOnHover(self.guess_btn, "white")


class Page4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.btn_font = f.Font(family='Modern No. 20', size=22, weight='bold')
        self.top_btn_font = f.Font(family='Modern No. 20', size=14, weight='bold')
        self.text_font = ("Ebrima", 12, 'bold')
        self.entry_font = ("Ebrima", 50, 'bold')
        self.guess_input = StringVar()
        self.score = 0
        self.btn_width = 4
        self.entry_width = game_dict["Level4"]["digits"]
        self.entry_font_color = game_dict["Level4"]["theme"]
        self.digits = game_dict["Level4"]["digits"]
        self.max_guesses = game_dict["Level4"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.game_widgets()

    def reset_game(self):
        self.score = 0
        self.max_guesses = game_dict["Level4"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.reset_widgets()

    def reset_widgets(self):
        self.guess_entry.delete(0, END)
        self.text_view.delete('1.0', END)
        self.guess_btn.config(state="normal")
        self.guess_entry.config(state="normal")
        self.score_lbl.config(text=f"Score: {self.score}")
        self.guess_lbl.config(text=f'Guesses left: {game_dict["Level4"]["guesses"]}', fg=white)

    def button_replay(self):
        self.reset_game()

    def button_back(self):
        self.guess_entry.delete(0)

    def num_button_click(self, num):
        current = self.guess_entry.get()
        self.guess_entry.delete(0, END)
        self.guess_entry.insert(0, str(current) + str(num))

    def button_clear(self):
        self.guess_entry.delete(0, END)

    def update_score(self, clues):
        if clues == "Bagels":
            self.score -= 2
        else:
            for i in clues.split(" "):
                if i == "Fermi":
                    self.score += 1
        self.score_lbl.config(text=f"Score: {self.score}")

    def win_score(self):
        self.score += game_dict["Level4"]["score"]
        self.score_lbl.config(text=f"Score: {self.score}")

    def game_end_action(self):
        self.guess_btn.config(state="disabled")
        self.guess_entry.config(state="disabled")

    def validate_guess(self, entry):
        if len(entry) >= self.digits:
            guess = entry[:self.digits]
            return guess
        else:
            return False

    def max_guess_counter(self):
        self.max_guesses -= 1
        self.guess_lbl.config(text=f"Guesses left: {self.max_guesses}")

    def max_guess_check(self):
        if self.max_guesses == 2:
            self.guess_lbl.config(fg="red")
        elif self.max_guesses == 0:
            self.text_view.insert(END, f"Out of Guesses\nSecret Number is {self.secret_num}")
            self.game_end_action()

    def guess_status(self, guess):
        if check_guess(guess, self.secret_num):
            return "win"
        else:
            clues = clues_generator(guess, self.secret_num)
            self.text_view.insert(END, f"{guess}\n{clues}\n\n")
            return clues

    def guess_action(self, entry):
        guess = self.validate_guess(entry)
        if guess is not False:
            self.button_clear()
            self.max_guess_counter()
            clues = self.guess_status(guess)
            if clues == "win":
                self.win_score()
                self.text_view.insert(END, f"{guess} is correct!\n")
                self.game_end_action()
            else:
                self.update_score(clues)
                self.max_guess_check()
        else:
            messagebox.showwarning('Bagels Game', f'Must make a {self.digits} digit guess')

    def guess_btn_action(self):
        entry = self.guess_entry.get()
        self.guess_action(entry)

    def changeOnHover(self, button, leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=black, foreground=leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=leave_color, foreground=black))

    def game_widgets(self):
        self.main_frame = Frame(self, bg=black)
        self.main_frame.pack()

        self.right_frame = Frame(self.main_frame, bg=black, bd=4, pady=8)
        self.right_frame.pack(side=RIGHT, anchor=S, padx=8, pady=4)

        self.left_frame = Frame(self.main_frame, bg=black, padx=6)
        self.left_frame.pack(side=LEFT, anchor=N)

        self.guess_frame = Frame(self.left_frame, bg=black, padx=4)
        self.guess_frame.pack(side=BOTTOM, anchor=S, pady=6)

        self.top_frame = Frame(self.left_frame, bg=black)
        self.top_frame.pack(side=TOP, fill='x')
        self.mid_frame = Frame(self.left_frame, bg=black)
        self.mid_frame.pack(pady=30)
        self.num_frame = Frame(self.left_frame, bg=black)
        self.num_frame.pack(padx=2, pady=18)

        self.top_btn_frame = Label(self.right_frame, bg=black)
        self.top_btn_frame.pack(side=TOP)

        self.replay_btn = Button(self.top_btn_frame, text="REPLAY", font=self.top_btn_font, padx=14,
                                 command=self.button_replay)
        self.replay_btn.grid(row=0, column=0, padx=2)
        self.changeOnHover(self.replay_btn, "white")

        self.mode_btn = Button(self.top_btn_frame, text="Mode", font=self.top_btn_font, padx=14,
                               command=lambda: self.controller.show_frame(GameOptionPage))
        self.mode_btn.grid(row=0, column=1, padx=2)
        self.changeOnHover(self.mode_btn, "white")

        self.text_view = st.ScrolledText(self.right_frame, bg=lightgrey, fg=game_dict["Level4"]["theme"],width=18, height=20, borderwidth=3,
                                         font=LARGE_FONT)
        self.text_view.pack()

        self.exit_lbl = Label(self.right_frame, text="<< Exit >>", bg=black, fg=white, font='fixedsys 14 bold',
                              cursor="hand2")
        self.exit_lbl.pack(anchor=SE, pady=3)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())

        # ============================================================================================================

        self.guess_lbl = Label(self.top_frame, text=f'Guesses left: {game_dict["Level4"]["guesses"]}', fg=white, font=self.text_font, bg=black)
        self.guess_lbl.pack(side=LEFT, padx=4)

        self.score_lbl = Label(self.top_frame, text=f"Score: {self.score}", fg=white, font=self.text_font, bg=black)
        self.score_lbl.pack(side=RIGHT, padx=4)

        self.lbl1 = Label(self.mid_frame, text="Enter Your Guess: ", bg=black, fg=white, font="Ebrima 22 bold")
        self.lbl1.pack(padx=5, pady=10)

        self.guess_entry = Entry(self.mid_frame, textvariable=self.guess_input, fg=self.entry_font_color,
                                 width=self.entry_width,
                                 font=self.entry_font, borderwidth=4, insertontime=0)
        self.guess_entry.pack()
        self.guess_entry.bind("<Key>", func=lambda e: "break")

        # ======================================================================================================================================

        self.bt0 = Button(self.num_frame, text="0", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(0))
        self.bt0.grid(row=0, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt0, "white")

        self.bt1 = Button(self.num_frame, text="1", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(1))
        self.bt1.grid(row=0, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt1, "white")

        self.bt2 = Button(self.num_frame, text="2", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(2))
        self.bt2.grid(row=0, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt2, "white")

        self.bt3 = Button(self.num_frame, text="3", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(3))
        self.bt3.grid(row=0, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt3, "white")

        self.bt4 = Button(self.num_frame, text="4", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(4))
        self.bt4.grid(row=1, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt4, "white")

        self.bt5 = Button(self.num_frame, text="5", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(5))
        self.bt5.grid(row=1, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt5, "white")

        self.bt6 = Button(self.num_frame, text="6", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(6))
        self.bt6.grid(row=1, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt6, "white")

        self.bt7 = Button(self.num_frame, text="7", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(7))
        self.bt7.grid(row=1, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt7, "white")

        self.bt8 = Button(self.num_frame, text="8", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(8))
        self.bt8.grid(row=2, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt8, "white")

        self.bt9 = Button(self.num_frame, text="9", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(9))
        self.bt9.grid(row=2, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt9, "white")

        self.clr_btn = Button(self.num_frame, text="CLR", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                              width=self.btn_width, height=1, command=lambda: self.button_clear())
        self.clr_btn.grid(row=2, column=2, padx=1, pady=1)
        self.changeOnHover(self.clr_btn, "white")

        self.back_btn = Button(self.num_frame, text="", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                               width=self.btn_width, height=1, command=self.button_back)
        self.back_btn.grid(row=2, column=3, padx=1, pady=1)
        self.changeOnHover(self.back_btn, "white")

        self.guess_btn = Button(self.guess_frame, text="Guess", relief="raised", bd=2, bg=grey, fg=black,
                                font=self.btn_font, width=18, command=self.guess_btn_action)
        self.guess_btn.pack()
        self.changeOnHover(self.guess_btn, "white")


class Page5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.btn_font = f.Font(family='Modern No. 20', size=22, weight='bold')
        self.top_btn_font = f.Font(family='Modern No. 20', size=14, weight='bold')
        self.text_font = ("Ebrima", 12, 'bold')
        self.entry_font = ("Ebrima", 50, 'bold')
        self.guess_input = StringVar()
        self.score = 0
        self.btn_width = 4
        self.entry_width = game_dict["Level5"]["digits"]
        self.entry_font_color = game_dict["Level5"]["theme"]
        self.digits = game_dict["Level5"]["digits"]
        self.max_guesses = game_dict["Level5"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.game_widgets()

    def reset_game(self):
        self.score = 0
        self.max_guesses = game_dict["Level5"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.reset_widgets()

    def reset_widgets(self):
        self.guess_entry.delete(0, END)
        self.text_view.delete('1.0', END)
        self.guess_btn.config(state="normal")
        self.guess_entry.config(state="normal")
        self.score_lbl.config(text=f"Score: {self.score}")
        self.guess_lbl.config(text=f'Guesses left: {game_dict["Level5"]["guesses"]}', fg=white)

    def button_replay(self):
        self.reset_game()

    def button_back(self):
        self.guess_entry.delete(0)

    def num_button_click(self, num):
        current = self.guess_entry.get()
        self.guess_entry.delete(0, END)
        self.guess_entry.insert(0, str(current) + str(num))

    def button_clear(self):
        self.guess_entry.delete(0, END)

    def update_score(self, clues):
        if clues == "Bagels":
            self.score -= 2
        else:
            for i in clues.split(" "):
                if i == "Fermi":
                    self.score += 1
        self.score_lbl.config(text=f"Score: {self.score}")

    def win_score(self):
        self.score += game_dict["Level5"]["score"]
        self.score_lbl.config(text=f"Score: {self.score}")

    def game_end_action(self):
        self.guess_btn.config(state="disabled")
        self.guess_entry.config(state="disabled")

    def validate_guess(self, entry):
        if len(entry) >= self.digits:
            guess = entry[:self.digits]
            return guess
        else:
            return False

    def max_guess_counter(self):
        self.max_guesses -= 1
        self.guess_lbl.config(text=f"Guesses left: {self.max_guesses}")

    def max_guess_check(self):
        if self.max_guesses == 2:
            self.guess_lbl.config(fg="red")
        elif self.max_guesses == 0:
            self.text_view.insert(END, f"Out of Guesses\nSecret Number is {self.secret_num}")
            self.game_end_action()

    def guess_status(self, guess):
        if check_guess(guess, self.secret_num):
            return "win"
        else:
            clues = clues_generator(guess, self.secret_num)
            self.text_view.insert(END, f"{guess}\n{clues}\n\n")
            return clues

    def guess_action(self, entry):
        guess = self.validate_guess(entry)
        if guess is not False:
            self.button_clear()
            self.max_guess_counter()
            clues = self.guess_status(guess)
            if clues == "win":
                self.win_score()
                self.text_view.insert(END, f"{guess} is correct!\n")
                self.game_end_action()
            else:
                self.update_score(clues)
                self.max_guess_check()
        else:
            messagebox.showwarning('Bagels Game', f'Must make a {self.digits} digit guess')

    def guess_btn_action(self):
        entry = self.guess_entry.get()
        self.guess_action(entry)

    def changeOnHover(self, button, leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=black, foreground=leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=leave_color, foreground=black))

    def game_widgets(self):
        self.main_frame = Frame(self, bg=black)
        self.main_frame.pack()

        self.right_frame = Frame(self.main_frame, bg=black, bd=4, pady=8)
        self.right_frame.pack(side=RIGHT, anchor=S, padx=8, pady=4)

        self.left_frame = Frame(self.main_frame, bg=black, padx=6)
        self.left_frame.pack(side=LEFT, anchor=N)

        self.guess_frame = Frame(self.left_frame, bg=black, padx=4)
        self.guess_frame.pack(side=BOTTOM, anchor=S, pady=6)

        self.top_frame = Frame(self.left_frame, bg=black)
        self.top_frame.pack(side=TOP, fill='x')
        self.mid_frame = Frame(self.left_frame, bg=black)
        self.mid_frame.pack(pady=30)
        self.num_frame = Frame(self.left_frame, bg=black)
        self.num_frame.pack(padx=2, pady=18)

        self.top_btn_frame = Label(self.right_frame, bg=black)
        self.top_btn_frame.pack(side=TOP)

        self.replay_btn = Button(self.top_btn_frame, text="REPLAY", font=self.top_btn_font, padx=14,
                                 command=self.button_replay)
        self.replay_btn.grid(row=0, column=0, padx=2)
        self.changeOnHover(self.replay_btn, "white")

        self.mode_btn = Button(self.top_btn_frame, text="Mode", font=self.top_btn_font, padx=14,
                               command=lambda: self.controller.show_frame(GameOptionPage))
        self.mode_btn.grid(row=0, column=1, padx=2)
        self.changeOnHover(self.mode_btn, "white")

        self.text_view = st.ScrolledText(self.right_frame, bg=lightgrey, fg=game_dict["Level5"]["theme"],width=18, height=20, borderwidth=3,
                                         font=LARGE_FONT)
        self.text_view.pack()

        self.exit_lbl = Label(self.right_frame, text="<< Exit >>", bg=black, fg=white, font='fixedsys 14 bold',
                              cursor="hand2")
        self.exit_lbl.pack(anchor=SE, pady=3)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())

        # ============================================================================================================

        self.guess_lbl = Label(self.top_frame, text=f'Guesses left: {game_dict["Level5"]["guesses"]}', fg=white, font=self.text_font, bg=black)
        self.guess_lbl.pack(side=LEFT, padx=4)

        self.score_lbl = Label(self.top_frame, text=f"Score: {self.score}", fg=white, font=self.text_font, bg=black)
        self.score_lbl.pack(side=RIGHT, padx=4)

        self.lbl1 = Label(self.mid_frame, text="Enter Your Guess: ", bg=black, fg=white, font="Ebrima 22 bold")
        self.lbl1.pack(padx=5, pady=10)

        self.guess_entry = Entry(self.mid_frame, textvariable=self.guess_input, fg=self.entry_font_color,
                                 width=self.entry_width,
                                 font=self.entry_font, borderwidth=4, insertontime=0)
        self.guess_entry.pack()
        self.guess_entry.bind("<Key>", func=lambda e: "break")

        # ======================================================================================================================================

        self.bt0 = Button(self.num_frame, text="0", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(0))
        self.bt0.grid(row=0, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt0, "white")

        self.bt1 = Button(self.num_frame, text="1", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(1))
        self.bt1.grid(row=0, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt1, "white")

        self.bt2 = Button(self.num_frame, text="2", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(2))
        self.bt2.grid(row=0, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt2, "white")

        self.bt3 = Button(self.num_frame, text="3", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(3))
        self.bt3.grid(row=0, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt3, "white")

        self.bt4 = Button(self.num_frame, text="4", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(4))
        self.bt4.grid(row=1, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt4, "white")

        self.bt5 = Button(self.num_frame, text="5", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(5))
        self.bt5.grid(row=1, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt5, "white")

        self.bt6 = Button(self.num_frame, text="6", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(6))
        self.bt6.grid(row=1, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt6, "white")

        self.bt7 = Button(self.num_frame, text="7", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(7))
        self.bt7.grid(row=1, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt7, "white")

        self.bt8 = Button(self.num_frame, text="8", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(8))
        self.bt8.grid(row=2, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt8, "white")

        self.bt9 = Button(self.num_frame, text="9", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(9))
        self.bt9.grid(row=2, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt9, "white")

        self.clr_btn = Button(self.num_frame, text="CLR", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                              width=self.btn_width, height=1, command=lambda: self.button_clear())
        self.clr_btn.grid(row=2, column=2, padx=1, pady=1)
        self.changeOnHover(self.clr_btn, "white")

        self.back_btn = Button(self.num_frame, text="", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                               width=self.btn_width, height=1, command=self.button_back)
        self.back_btn.grid(row=2, column=3, padx=1, pady=1)
        self.changeOnHover(self.back_btn, "white")

        self.guess_btn = Button(self.guess_frame, text="Guess", relief="raised", bd=2, bg=grey, fg=black,
                                font=self.btn_font, width=18, command=self.guess_btn_action)
        self.guess_btn.pack()
        self.changeOnHover(self.guess_btn, "white")


class Page6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.btn_font = f.Font(family='Modern No. 20', size=22, weight='bold')
        self.top_btn_font = f.Font(family='Modern No. 20', size=14, weight='bold')
        self.text_font = ("Ebrima", 12, 'bold')
        self.entry_font = ("Ebrima", 50, 'bold')
        self.guess_input = StringVar()
        self.score = 0
        self.btn_width = 4
        self.entry_width = game_dict["Level6"]["digits"]
        self.entry_font_color = game_dict["Level6"]["theme"]
        self.digits = game_dict["Level6"]["digits"]
        self.max_guesses = game_dict["Level6"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.game_widgets()

    def reset_game(self):
        self.score = 0
        self.max_guesses = game_dict["Level6"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.reset_widgets()

    def reset_widgets(self):
        self.guess_entry.delete(0, END)
        self.text_view.delete('1.0', END)
        self.guess_btn.config(state="normal")
        self.guess_entry.config(state="normal")
        self.score_lbl.config(text=f"Score: {self.score}")
        self.guess_lbl.config(text=f'Guesses left: {game_dict["Level6"]["guesses"]}', fg=white)

    def button_replay(self):
        self.reset_game()

    def button_back(self):
        self.guess_entry.delete(0)

    def num_button_click(self, num):
        current = self.guess_entry.get()
        self.guess_entry.delete(0, END)
        self.guess_entry.insert(0, str(current) + str(num))

    def button_clear(self):
        self.guess_entry.delete(0, END)

    def update_score(self, clues):
        if clues == "Bagels":
            self.score -= 2
        else:
            for i in clues.split(" "):
                if i == "Fermi":
                    self.score += 1
        self.score_lbl.config(text=f"Score: {self.score}")

    def win_score(self):
        self.score += game_dict["Level6"]["score"]
        self.score_lbl.config(text=f"Score: {self.score}")

    def game_end_action(self):
        self.guess_btn.config(state="disabled")
        self.guess_entry.config(state="disabled")

    def validate_guess(self, entry):
        if len(entry) >= self.digits:
            guess = entry[:self.digits]
            return guess
        else:
            return False

    def max_guess_counter(self):
        self.max_guesses -= 1
        self.guess_lbl.config(text=f"Guesses left: {self.max_guesses}")

    def max_guess_check(self):
        if self.max_guesses == 2:
            self.guess_lbl.config(fg="red")
        elif self.max_guesses == 0:
            self.text_view.insert(END, f"Out of Guesses\nSecret Number is {self.secret_num}")
            self.game_end_action()

    def guess_status(self, guess):
        if check_guess(guess, self.secret_num):
            return "win"
        else:
            clues = clues_generator(guess, self.secret_num)
            self.text_view.insert(END, f"{guess}\n{clues}\n\n")
            return clues

    def guess_action(self, entry):
        guess = self.validate_guess(entry)
        if guess is not False:
            self.button_clear()
            self.max_guess_counter()
            clues = self.guess_status(guess)
            if clues == "win":
                self.win_score()
                self.text_view.insert(END, f"{guess} is correct!\n")
                self.game_end_action()
            else:
                self.update_score(clues)
                self.max_guess_check()
        else:
            messagebox.showwarning('Bagels Game', f'Must make a {self.digits} digit guess')

    def guess_btn_action(self):
        entry = self.guess_entry.get()
        self.guess_action(entry)

    def changeOnHover(self, button, leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=black, foreground=leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=leave_color, foreground=black))

    def game_widgets(self):
        self.main_frame = Frame(self, bg=black)
        self.main_frame.pack()

        self.right_frame = Frame(self.main_frame, bg=black, bd=4, pady=8)
        self.right_frame.pack(side=RIGHT, anchor=S, padx=8, pady=4)

        self.left_frame = Frame(self.main_frame, bg=black, padx=6)
        self.left_frame.pack(side=LEFT, anchor=N)

        self.guess_frame = Frame(self.left_frame, bg=black, padx=4)
        self.guess_frame.pack(side=BOTTOM, anchor=S, pady=6)

        self.top_frame = Frame(self.left_frame, bg=black)
        self.top_frame.pack(side=TOP, fill='x')
        self.mid_frame = Frame(self.left_frame, bg=black)
        self.mid_frame.pack(pady=30)
        self.num_frame = Frame(self.left_frame, bg=black)
        self.num_frame.pack(padx=2, pady=18)

        self.top_btn_frame = Label(self.right_frame, bg=black)
        self.top_btn_frame.pack(side=TOP)

        self.replay_btn = Button(self.top_btn_frame, text="REPLAY", font=self.top_btn_font, padx=14,
                                 command=self.button_replay)
        self.replay_btn.grid(row=0, column=0, padx=2)
        self.changeOnHover(self.replay_btn, "white")

        self.mode_btn = Button(self.top_btn_frame, text="Mode", font=self.top_btn_font, padx=14,
                               command=lambda: self.controller.show_frame(GameOptionPage))
        self.mode_btn.grid(row=0, column=1, padx=2)
        self.changeOnHover(self.mode_btn, "white")

        self.text_view = st.ScrolledText(self.right_frame, bg=lightgrey, fg=game_dict["Level6"]["theme"],width=18, height=20, borderwidth=3,
                                         font=LARGE_FONT)
        self.text_view.pack()

        self.exit_lbl = Label(self.right_frame, text="<< Exit >>", bg=black, fg=white, font='fixedsys 14 bold',
                              cursor="hand2")
        self.exit_lbl.pack(anchor=SE, pady=3)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())

        # ============================================================================================================

        self.guess_lbl = Label(self.top_frame, text=f'Guesses left: {game_dict["Level6"]["guesses"]}', fg=white, font=self.text_font, bg=black)
        self.guess_lbl.pack(side=LEFT, padx=4)

        self.score_lbl = Label(self.top_frame, text=f"Score: {self.score}", fg=white, font=self.text_font, bg=black)
        self.score_lbl.pack(side=RIGHT, padx=4)

        self.lbl1 = Label(self.mid_frame, text="Enter Your Guess: ", bg=black, fg=white, font="Ebrima 22 bold")
        self.lbl1.pack(padx=5, pady=10)

        self.guess_entry = Entry(self.mid_frame, textvariable=self.guess_input, fg=self.entry_font_color,
                                 width=self.entry_width,
                                 font=self.entry_font, borderwidth=4, insertontime=0)
        self.guess_entry.pack()
        self.guess_entry.bind("<Key>", func=lambda e: "break")

        # ======================================================================================================================================

        self.bt0 = Button(self.num_frame, text="0", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(0))
        self.bt0.grid(row=0, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt0, "white")

        self.bt1 = Button(self.num_frame, text="1", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(1))
        self.bt1.grid(row=0, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt1, "white")

        self.bt2 = Button(self.num_frame, text="2", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(2))
        self.bt2.grid(row=0, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt2, "white")

        self.bt3 = Button(self.num_frame, text="3", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(3))
        self.bt3.grid(row=0, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt3, "white")

        self.bt4 = Button(self.num_frame, text="4", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(4))
        self.bt4.grid(row=1, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt4, "white")

        self.bt5 = Button(self.num_frame, text="5", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(5))
        self.bt5.grid(row=1, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt5, "white")

        self.bt6 = Button(self.num_frame, text="6", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(6))
        self.bt6.grid(row=1, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt6, "white")

        self.bt7 = Button(self.num_frame, text="7", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(7))
        self.bt7.grid(row=1, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt7, "white")

        self.bt8 = Button(self.num_frame, text="8", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(8))
        self.bt8.grid(row=2, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt8, "white")

        self.bt9 = Button(self.num_frame, text="9", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(9))
        self.bt9.grid(row=2, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt9, "white")

        self.clr_btn = Button(self.num_frame, text="CLR", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                              width=self.btn_width, height=1, command=lambda: self.button_clear())
        self.clr_btn.grid(row=2, column=2, padx=1, pady=1)
        self.changeOnHover(self.clr_btn, "white")

        self.back_btn = Button(self.num_frame, text="", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                               width=self.btn_width, height=1, command=self.button_back)
        self.back_btn.grid(row=2, column=3, padx=1, pady=1)
        self.changeOnHover(self.back_btn, "white")

        self.guess_btn = Button(self.guess_frame, text="Guess", relief="raised", bd=2, bg=grey, fg=black,
                                font=self.btn_font, width=18, command=self.guess_btn_action)
        self.guess_btn.pack()
        self.changeOnHover(self.guess_btn, "white")


class Page7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.btn_font = f.Font(family='Modern No. 20', size=22, weight='bold')
        self.top_btn_font = f.Font(family='Modern No. 20', size=14, weight='bold')
        self.text_font = ("Ebrima", 12, 'bold')
        self.entry_font = ("Ebrima", 50, 'bold')
        self.guess_input = StringVar()
        self.score = 0
        self.btn_width = 4
        self.entry_width = game_dict["Level7"]["digits"]
        self.entry_font_color = game_dict["Level7"]["theme"]
        self.digits = game_dict["Level7"]["digits"]
        self.max_guesses = game_dict["Level7"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.game_widgets()

    def reset_game(self):
        self.score = 0
        self.max_guesses = game_dict["Level7"]["guesses"]
        self.secret_num = get_secret_num(self.digits)
        self.reset_widgets()

    def reset_widgets(self):
        self.guess_entry.delete(0, END)
        self.text_view.delete('1.0', END)
        self.guess_btn.config(state="normal")
        self.guess_entry.config(state="normal")
        self.score_lbl.config(text=f"Score: {self.score}")
        self.guess_lbl.config(text=f'Guesses left: {game_dict["Level7"]["guesses"]}', fg=white)

    def button_replay(self):
        self.reset_game()

    def button_back(self):
        self.guess_entry.delete(0)

    def num_button_click(self, num):
        current = self.guess_entry.get()
        self.guess_entry.delete(0, END)
        self.guess_entry.insert(0, str(current) + str(num))

    def button_clear(self):
        self.guess_entry.delete(0, END)

    def update_score(self, clues):
        if clues == "Bagels":
            self.score -= 2
        else:
            for i in clues.split(" "):
                if i == "Fermi":
                    self.score += 1
        self.score_lbl.config(text=f"Score: {self.score}")

    def win_score(self):
        self.score += game_dict["Level7"]["score"]
        self.score_lbl.config(text=f"Score: {self.score}")

    def game_end_action(self):
        self.guess_btn.config(state="disabled")
        self.guess_entry.config(state="disabled")

    def validate_guess(self, entry):
        if len(entry) >= self.digits:
            guess = entry[:self.digits]
            return guess
        else:
            return False

    def max_guess_counter(self):
        self.max_guesses -= 1
        self.guess_lbl.config(text=f"Guesses left: {self.max_guesses}")

    def max_guess_check(self):
        if self.max_guesses == 2:
            self.guess_lbl.config(fg="red")
        elif self.max_guesses == 0:
            self.text_view.insert(END, f"Out of Guesses\nSecret Number is {self.secret_num}")
            self.game_end_action()

    def guess_status(self, guess):
        if check_guess(guess, self.secret_num):
            return "win"
        else:
            clues = clues_generator(guess, self.secret_num)
            self.text_view.insert(END, f"{guess}\n{clues}\n\n")
            return clues

    def guess_action(self, entry):
        guess = self.validate_guess(entry)
        if guess is not False:
            self.button_clear()
            self.max_guess_counter()
            clues = self.guess_status(guess)
            if clues == "win":
                self.win_score()
                self.text_view.insert(END, f"{guess} is correct!\n")
                self.game_end_action()
            else:
                self.update_score(clues)
                self.max_guess_check()
        else:
            messagebox.showwarning('Bagels Game', f'Must make a {self.digits} digit guess')

    def guess_btn_action(self):
        entry = self.guess_entry.get()
        self.guess_action(entry)

    def changeOnHover(self, button, leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=black, foreground=leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=leave_color, foreground=black))

    def game_widgets(self):
        self.main_frame = Frame(self, bg=black)
        self.main_frame.pack()

        self.right_frame = Frame(self.main_frame, bg=black, bd=4, pady=8)
        self.right_frame.pack(side=RIGHT, anchor=S, padx=8, pady=4)

        self.left_frame = Frame(self.main_frame, bg=black, padx=6)
        self.left_frame.pack(side=LEFT, anchor=N)

        self.guess_frame = Frame(self.left_frame, bg=black, padx=4)
        self.guess_frame.pack(side=BOTTOM, anchor=S, pady=6)

        self.top_frame = Frame(self.left_frame, bg=black)
        self.top_frame.pack(side=TOP, fill='x')
        self.mid_frame = Frame(self.left_frame, bg=black)
        self.mid_frame.pack(pady=30)
        self.num_frame = Frame(self.left_frame, bg=black)
        self.num_frame.pack(padx=2, pady=18)

        self.top_btn_frame = Label(self.right_frame, bg=black)
        self.top_btn_frame.pack(side=TOP)

        self.replay_btn = Button(self.top_btn_frame, text="REPLAY", font=self.top_btn_font, padx=14,
                                 command=self.button_replay)
        self.replay_btn.grid(row=0, column=0, padx=2)
        self.changeOnHover(self.replay_btn, "white")

        self.mode_btn = Button(self.top_btn_frame, text="Mode", font=self.top_btn_font, padx=14,
                               command=lambda: self.controller.show_frame(GameOptionPage))
        self.mode_btn.grid(row=0, column=1, padx=2)
        self.changeOnHover(self.mode_btn, "white")

        self.text_view = st.ScrolledText(self.right_frame, bg=lightgrey, fg=game_dict["Level7"]["theme"],width=18, height=20, borderwidth=3,
                                         font=LARGE_FONT)
        self.text_view.pack()

        self.exit_lbl = Label(self.right_frame, text="<< Exit >>", bg=black, fg=white, font='fixedsys 14 bold',
                              cursor="hand2")
        self.exit_lbl.pack(anchor=SE, pady=3)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())

        # ============================================================================================================

        self.guess_lbl = Label(self.top_frame, text=f'Guesses left: {game_dict["Level7"]["guesses"]}', fg=white, font=self.text_font, bg=black)
        self.guess_lbl.pack(side=LEFT, padx=4)

        self.score_lbl = Label(self.top_frame, text=f"Score: {self.score}", fg=white, font=self.text_font, bg=black)
        self.score_lbl.pack(side=RIGHT, padx=4)

        self.lbl1 = Label(self.mid_frame, text="Enter Your Guess: ", bg=black, fg=white, font="Ebrima 22 bold")
        self.lbl1.pack(padx=5, pady=10)

        self.guess_entry = Entry(self.mid_frame, textvariable=self.guess_input, fg=self.entry_font_color,
                                 width=self.entry_width,
                                 font=self.entry_font, borderwidth=4, insertontime=0)
        self.guess_entry.pack()
        self.guess_entry.bind("<Key>", func=lambda e: "break")

        # ======================================================================================================================================

        self.bt0 = Button(self.num_frame, text="0", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(0))
        self.bt0.grid(row=0, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt0, "white")

        self.bt1 = Button(self.num_frame, text="1", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(1))
        self.bt1.grid(row=0, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt1, "white")

        self.bt2 = Button(self.num_frame, text="2", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(2))
        self.bt2.grid(row=0, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt2, "white")

        self.bt3 = Button(self.num_frame, text="3", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(3))
        self.bt3.grid(row=0, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt3, "white")

        self.bt4 = Button(self.num_frame, text="4", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(4))
        self.bt4.grid(row=1, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt4, "white")

        self.bt5 = Button(self.num_frame, text="5", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(5))
        self.bt5.grid(row=1, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt5, "white")

        self.bt6 = Button(self.num_frame, text="6", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(6))
        self.bt6.grid(row=1, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt6, "white")

        self.bt7 = Button(self.num_frame, text="7", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(7))
        self.bt7.grid(row=1, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt7, "white")

        self.bt8 = Button(self.num_frame, text="8", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(8))
        self.bt8.grid(row=2, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt8, "white")

        self.bt9 = Button(self.num_frame, text="9", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.btn_width, height=1,
                          command=lambda: self.num_button_click(9))
        self.bt9.grid(row=2, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt9, "white")

        self.clr_btn = Button(self.num_frame, text="CLR", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                              width=self.btn_width, height=1, command=lambda: self.button_clear())
        self.clr_btn.grid(row=2, column=2, padx=1, pady=1)
        self.changeOnHover(self.clr_btn, "white")

        self.back_btn = Button(self.num_frame, text="", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                               width=self.btn_width, height=1, command=self.button_back)
        self.back_btn.grid(row=2, column=3, padx=1, pady=1)
        self.changeOnHover(self.back_btn, "white")

        self.guess_btn = Button(self.guess_frame, text="Guess", relief="raised", bd=2, bg=grey, fg=black,
                                font=self.btn_font, width=18, command=self.guess_btn_action)
        self.guess_btn.pack()
        self.changeOnHover(self.guess_btn, "white")


app = BagelsGame()
app.mainloop()
