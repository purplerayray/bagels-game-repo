import tkinter as tk
from tkinter import font as f
import tkinter.scrolledtext as st
from tkinter import *

LARGE_FONT = ("Bradley Hand ITC", 15, 'bold')
pink = "#FF10F0"
black = "black"
white = 'white'
grey = "lightgrey"
lightgrey = "#D3D3D3"


class BagelsGame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RulePage, GameOptionPage, GamePage):
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
        self.bagel_font = f.Font(family='bauhaus 93', size=50, weight='normal')
        self.start_widgets()

    def start_widgets(self):
        self.space_lbl = Label(self, height=4, bg=black)
        self.space_lbl.pack()

        self.game_lbl = Label(self, text='BAGELS', font=self.bagel_font, bg=black, fg=white)
        self.game_lbl.pack(pady=10)

        self.rule_lbl = Label(self, text='The rules are simple. Click to View >>>', font='Ebrima 15 bold', bg=black, fg=white, cursor="hand2")
        self.rule_lbl.pack(pady=10)
        self.rule_lbl.bind("<Button>", lambda e: self.controller.show_frame(RulePage))

        self.play_lbl = Label(self, text='<<< PRESS PLAY >>>', font='fixedsys 20 bold', bg=black, fg=white, cursor="hand2")
        self.play_lbl.pack(pady=60)
        self.play_lbl.bind("<Button>", lambda e: self.controller.show_frame(GameOptionPage))

        self.exit_lbl = Label(self, text="<< QUIT >>", font='fixedsys 16 bold', bg=black, fg=white, cursor="hand2")
        self.exit_lbl.pack()
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())


class RulePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.Rulepage_widgets()

    def Rulepage_widgets(self):
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

        self.play_lbl = Label(self, text="<<< PRESS PLAY >>>", font='fixedsys 20 bold', bg=black, fg=white, cursor="hand2")
        self.play_lbl.pack(pady=20)
        self.play_lbl.bind("<Button>", lambda e: self.controller.show_frame(GameOptionPage))

        self.exit_lbl = Label(self, text="<< QUIT >>", font='fixedsys 16 bold', bg=black, fg=white,)
        self.exit_lbl.pack(pady=8)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())


class GameOptionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        self.option_widgets()

    def game_option(self, num):
        global max_digit
        max_digit = num
        self.controller.show_frame(GamePage)

    def option_widgets(self):
        self.go_lbl1 = Label(self, text="Select Game Mode", font='Ebrima 25 bold', bg="black", fg=white)
        self.go_lbl1.pack(pady=20)
        self.miniframe = Frame(self, bg="black")
        self.miniframe.pack(padx=10, pady=10)

        self.btn2 = Button(self.miniframe, text="2 Digits\n6 guesses", font="SitkaText 16 bold", bg="red",
                           height=8, width=12, command=lambda: self.controller.show_frame(GamePage))
        self.btn2.grid(row=0, column=0, padx=4, pady=6)
        self.changeOnHover(self.btn2, "red")
        self.btn3 = Button(self.miniframe, text="3 Digits\n10 guesses", font="SitkaText 16 bold", bg="blue",
                           height=8, width=12, command=lambda: self.controller.show_frame(GamePage))
        self.btn3.grid(row=0, column=1, padx=4, pady=6)
        self.changeOnHover(self.btn3, "blue")
        self.btn4 = Button(self.miniframe, text="4 Digits\n14 guesses", font="SitkaText 16 bold", bg="yellow",
                           height=8, width=12, command=lambda: self.controller.show_frame(GamePage))
        self.btn4.grid(row=0, column=2, padx=4, pady=6)
        self.changeOnHover(self.btn4, "yellow")
        self.btn5 = Button(self.miniframe, text="5 Digits\n20 guesses", font="SitkaText 16 bold", bg="green",
                           height=8, width=12, command=lambda: self.game_option(4))
        self.btn5.grid(row=1, column=0, padx=4, pady=6)
        self.changeOnHover(self.btn5, "green")
        self.btn6 = Button(self.miniframe, text="6 Digits\n25 guesses", font="SitkaText 16 bold", bg="orange",
                           height=8, width=12, command=lambda: self.controller.show_frame(GamePage))
        self.btn6.grid(row=1, column=1, padx=4, pady=6)
        self.changeOnHover(self.btn6, "orange")
        self.btn7 = Button(self.miniframe, text="7 Digits\n32 guesses", font="SitkaText 16 bold", bg="purple",
                           height=8, width=12, command=lambda: self.controller.show_frame(GamePage))
        self.btn7.grid(row=1, column=2, padx=4, pady=6)
        self.changeOnHover(self.btn7, "purple")

        self.exit_game = Label(self.miniframe, text="<<< Return to Home >>> ",
                               font="fixedsys 16 normal", fg=white, bg="black", cursor="hand2")
        self.exit_game.grid(row=2, column=0, columnspan=3, sticky=E, pady=5)
        self.exit_game.bind("<Button>", lambda e: self.controller.show_frame(StartPage))

    # function to change properties of button on hover
    def changeOnHover(self, button, leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=black, foreground=leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=leave_color, foreground=black))


class GamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=black)
        self.controller = controller
        self.btn_font = f.Font(family='Modern No. 20', size=22, weight='bold')
        self.top_btn_font = f.Font(family='Modern No. 20', size=14, weight='bold')
        self.text_font = ("Ebrima", 12, 'bold')
        self.entry_font = ("Ebrima", 50, 'bold')
        self.guess_input = StringVar()
        self.width = 4
        self.entry_width = 7   # max_digit
        self.vcmd = (self.register(self.onValidate), '%P')
        self.game_widgets()


    def onValidate(self, P):
        if len(P) == 4:
            # Entry with 1 digit is ok
            return True
        else:
            # Anything else, reject it
            return False

    def get_mode(self):
        print(max_digit)

    def button_click(self, num):
        current = self.clue_entry.get()
        self.clue_entry.delete(0, END)
        self.clue_entry.insert(0, str(current) + str(num))

    def button_clear(self):
        self.clue_entry.delete(0, END)

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
        self.mid_frame = Frame(self.left_frame, bg=black)  # will contain a row of text fields
        self.mid_frame.pack(pady=30)
        self.num_frame = Frame(self.left_frame, bg=black)
        self.num_frame.pack(padx=2, pady=18)

        self.top_btn_frame = Label(self.right_frame, bg=black)
        self.top_btn_frame.pack(side=TOP)

        self.replay_btn = Button(self.top_btn_frame, text="REPLAY", font=self.top_btn_font, padx=14)
        self.replay_btn.grid(row=0, column=0, padx=2)
        self.changeOnHover(self.replay_btn, "white")

        self.mode_btn = Button(self.top_btn_frame, text="Mode", font=self.top_btn_font, padx=14, command=lambda: self.controller.show_frame(GameOptionPage))
        self.mode_btn.grid(row=0, column=1, padx=2)
        self.changeOnHover(self.mode_btn, "white")

        self.text_view = st.ScrolledText(self.right_frame, bg=lightgrey, width=18, height=20, borderwidth=3, font=LARGE_FONT)
        self.text_view.pack()

        self.exit_lbl = Label(self.right_frame, text="<< Exit >>", bg=black, fg=white, font='fixedsys 14 bold', cursor="hand2")
        self.exit_lbl.pack(anchor=SE, pady=3)
        self.exit_lbl.bind("<Button>", lambda e: self.controller.destroy())

        # ============================================================================================================

        self.guess_lbl = Label(self.top_frame, text="Guesses left: 10", fg=white, font=self.text_font, bg=black)
        self.guess_lbl.pack(side=LEFT, padx=4)

        self.score_lbl = Label(self.top_frame, text="Score: 10", fg=white, font=self.text_font, bg=black)
        self.score_lbl.pack(side=RIGHT, padx=4)

        self.lbl1 = Label(self.mid_frame, text="Enter Your Guess: ", bg=black, fg=white, font="Ebrima 22 bold")
        self.lbl1.pack(padx=5, pady=10)

        self.clue_entry = Entry(self.mid_frame, textvariable=self.guess_input, width=self.entry_width,
                                font=self.entry_font, borderwidth=4, insertontime=0,
                                validate="focus", validatecommand=self.vcmd)
        self.clue_entry.pack()
        self.clue_entry.bind("<Key>", func=lambda e: "break")

        # ======================================================================================================================================
        self.clue_view = Text(self.num_frame, height=1, width=28, borderwidth=4, font=LARGE_FONT)
        self.clue_view.grid(row=0, column=0, columnspan=4, pady=4)

        self.bt0 = Button(self.num_frame, text="0", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(0))
        self.bt0.grid(row=1, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt0, "white")

        self.bt1 = Button(self.num_frame, text="1", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(1))
        self.bt1.grid(row=1, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt1, "white")

        self.bt2 = Button(self.num_frame, text="2", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(2))
        self.bt2.grid(row=1, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt2, "white")

        self.bt3 = Button(self.num_frame, text="3", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(3))
        self.bt3.grid(row=1, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt3, "white")

        self.bt4 = Button(self.num_frame, text="4", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(4))
        self.bt4.grid(row=2, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt4, "white")

        self.bt5 = Button(self.num_frame, text="5", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(5))
        self.bt5.grid(row=2, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt5, "white")

        self.bt6 = Button(self.num_frame, text="6", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(6))
        self.bt6.grid(row=2, column=2, padx=2, pady=2)
        self.changeOnHover(self.bt6, "white")

        self.bt7 = Button(self.num_frame, text="7", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(7))
        self.bt7.grid(row=2, column=3, padx=2, pady=2)
        self.changeOnHover(self.bt7, "white")

        self.bt8 = Button(self.num_frame, text="8", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(8))
        self.bt8.grid(row=3, column=0, padx=2, pady=2)
        self.changeOnHover(self.bt8, "white")

        self.bt9 = Button(self.num_frame, text="9", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=self.width, height=1,
                          command=lambda: self.button_click(9))
        self.bt9.grid(row=3, column=1, padx=2, pady=2)
        self.changeOnHover(self.bt9, "white")

        self.clr_btn = Button(self.num_frame, text="CLR", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font,
                          width=9, height=1, command=lambda: self.button_clear())
        self.clr_btn.grid(row=3, column=2, columnspan=2, padx=1, pady=1)
        self.changeOnHover(self.clr_btn, "white")

        self.guess_btn = Button(self.guess_frame, text="Guess", relief="raised", bd=2, bg=grey, fg=black, font=self.btn_font, width=18, command=lambda: self.get_mode())
        self.guess_btn.pack()
        self.changeOnHover(self.guess_btn, "white")


app = BagelsGame()
app.mainloop()