from tkinter import *
from board_class import Board
from player import Player

class tttGUI:
    # Constructor --------------------------------------------------------------

    # params:  self

    def __init__(self):
        # Window and frames
        self.__window = Tk()
        self.__window.title("tic tac toe")
        self.__top = Frame(self.__window)
        self.__middle = Frame(self.__window)
        self.__bottom = Frame(self.__window)
        self.__startframe = Frame(self.__window)
        self.__top.pack()
        self.__middle.pack()
        self.__bottom.pack()
        self.__startframe.pack()
        # Buttons for game
        self.__text1 = 'A1'
        self.__text2 = 'A2'
        self.__text3 = 'A3'
        self.__text4 = 'A4'
        self.__text5 = 'A5'
        self.__text6 = 'A6'
        self.__text7 = 'A7'
        self.__text8 = 'A8'
        self.__text9 = 'A9'
        self.__button_a1 = Button(self.__top, text= self.__text1, state = DISABLED)
        self.__button_a1.config(width = '20', height = '10')
        self.__button_a1.pack(side = 'left')
        self.__button_a2 = Button(self.__top, text=self.__text2, state = DISABLED)
        self.__button_a2.config(width = '20', height = '10')
        self.__button_a2.pack(side = 'left')
        self.__button_a3 = Button(self.__top, text=self.__text3, state = DISABLED)
        self.__button_a3.config(width = '20', height = '10')
        self.__button_a3.pack(side = 'left')
        self.__button_a4 = Button(self.__middle, text=self.__text4, state = DISABLED)
        self.__button_a4.config(width = '20', height = '10')
        self.__button_a4.pack(side = 'left')
        self.__button_a5 = Button(self.__middle, text=self.__text5, state = DISABLED)
        self.__button_a5.config(width = '20', height = '10')
        self.__button_a5.pack(side = 'left')
        self.__button_a6 = Button(self.__middle, text=self.__text6, state = DISABLED)
        self.__button_a6.config(width = '20', height = '10')
        self.__button_a6.pack(side = 'left')
        self.__button_a7 = Button(self.__bottom, text=self.__text7, state = DISABLED)
        self.__button_a7.config(width = '20', height = '10')
        self.__button_a7.pack(side = 'left')
        self.__button_a8 = Button(self.__bottom, text=self.__text8, state = DISABLED)
        self.__button_a8.config(width = '20', height = '10')
        self.__button_a8.pack(side = 'left')
        self.__button_a9 = Button(self.__bottom, text=self.__text9, state = DISABLED)
        self.__button_a9.config(width = '20', height = '10')
        self.__button_a9.pack(side = 'left')
        
        self.__button_list = [self.__button_a1, self.__button_a2, self.__button_a3, \
                              self.__button_a4, self.__button_a5, self.__button_a6, \
                              self.__button_a7, self.__button_a8, self.__button_a9]
        # Start Game Button
        self.__start_game_text = StringVar()
        self.__start_game_text.set('Start Game')
        self.__start_game_button = Button(self.__startframe, text = self.__start_game_text.get(), \
                                          command = self.start_game)
        self.__start_game_button.pack()

        # Players
        team1 = Board.TEAMS[0]
        team2 = Board.TEAMS[1]
        self.__player1 = Player(team1)
        self.__player2 = Player(team2)

    def start_game(self):       
        for button in self.__button_list:
            button.config(state = NORMAL)

    def choose_button_1(self):
        if self.__player1:
            self.__text1 = 'x'
            self.__button_a1.config(state = DISABLED, text = self.__text1)


tttGUI()
