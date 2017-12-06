from tkinter import *
from tkinter import messagebox
from tkinter import font
from board1 import Board
from player_class import Player
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

bwidth = 10
bheight = 5
class tttGUI():

    def __init__(self):
        
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
        self.__text1 = 'A1'
        self.__text2 = 'A2'
        self.__text3 = 'A3'
        self.__text4 = 'A4'
        self.__text5 = 'A5'
        self.__text6 = 'A6'
        self.__text7 = 'A7'
        self.__text8 = 'A8'
        self.__text9 = 'A9'
        self.__text_list = [self.__text1,self.__text2,self.__text3,self.__text4,self.__text5,self.__text6,self.__text7,self.__text8,self.__text9]
        self.__font = font.Font(family="Comic Sans MS", size = 15, weight = 'bold')#bg = "PeachPuff")
        self.__x_image = PhotoImage(file = 'x_image.gif')
        self.__o_image = PhotoImage(file = 'o_image.gif')
        self.player = Player()
        self.board = Board()
        

        self.__button1 = Button(self.__top, text = self.__text1,font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(1,self.__text1))
        self.__button1.config(width = bwidth,height = bheight, bg = 'white')
        self.__button1.pack(side = 'left')
        self.__button2 = Button(self.__top, text = self.__text2,font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(2,self.__text2))
        self.__button2.config(width = bwidth,height = bheight, bg = 'white')
        self.__button2.pack(side = 'left')
        self.__button3 = Button(self.__top, text = self.__text3, font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(3,self.__text3))
        self.__button3.config(width = bwidth,height = bheight, bg = 'white')
        self.__button3.pack(side = 'left')
        self.__button4 = Button(self.__middle, text = self.__text4,font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(4,self.__text4))
        self.__button4.config(width = bwidth,height = bheight, bg = 'white')
        self.__button4.pack(side = 'left')
        self.__button5 = Button(self.__middle, text = self.__text5,font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(5,self.__text5))
        self.__button5.config(width = bwidth,height = bheight, bg = 'white')
        self.__button5.pack(side = 'left')
        self.__button6 = Button(self.__middle, text = self.__text6,font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(6,self.__text6))
        self.__button6.config(width = bwidth,height = bheight, bg = 'white')
        self.__button6.pack(side = 'left')
        self.__button7 = Button(self.__bottom, text = self.__text7,font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(7,self.__text7))
        self.__button7.config(width = bwidth,height = bheight, bg = 'white')
        self.__button7.pack(side = 'left')
        self.__button8 = Button(self.__bottom, text = self.__text8,font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(8,self.__text8))
        self.__button8.config(width = bwidth,height = bheight, bg = 'white')
        self.__button8.pack(side = 'left')
        self.__button9 = Button(self.__bottom, text = self.__text9,font = self.__font, state  = DISABLED, \
                                command=lambda: self.button_click(9,self.__text9))
        self.__button9.config(width = bwidth,height = bheight, bg = 'white')
        self.__button9.pack(side = 'left')

        self.__button_list = [self.__button1, self.__button2, self.__button3,
                              self.__button4, self.__button5, self.__button6,
                              self.__button7, self.__button8, self.__button9
                              ]

        #Start game button
        self.__start_game_text = StringVar()
        self.__start_game_text.set('Start Game')
        self.__start_game_button = Button(self.__startframe, text = self.__start_game_text.get(),\
                                          command = self.start_game)

        #Reset game button
        self.__reset_game_text = StringVar()
        self.__reset_game_text.set('Reset Game')
        self.__reset_game_button = Button(self.__startframe, text = self.__reset_game_text.get(),\
                                          command = self.reset_game)
        #Graph button
        self.__graph_wins_button = Button(self.__startframe, text = 'Graph', command = self.graph_wins)
        
        #X wins labels
        self.__x_win_label = Label(self.__startframe, text = 'X: ')
        self.__num_x_wins = IntVar()
        self.__num_x_wins.set(self.player.get_x_wins())
        self.__x_win = Label(self.__startframe, textvariable =self.__num_x_wins)
        #O wins labels
        self.__num_o_wins = IntVar()
        self.__num_o_wins.set(self.player.get_o_wins())
        self.__o_win_label = Label(self.__startframe,text = 'O: ')
        self.__o_win = Label(self.__startframe, textvariable = self.__num_o_wins)
        #Ties labels
        self.__num_ties = IntVar()
        self.__num_ties.set(self.player.get_ties())
        self.__num_ties_label = Label(self.__startframe,text= 'Tie: ')
        self.__ties = Label(self.__startframe, textvariable = self.__num_ties)
        #Pack start,end,graph buttons and x,o,ties labels
        self.__start_game_button.pack(side='left')
        self.__reset_game_button.pack(side='left')
        self.__graph_wins_button.pack(side='left')
        self.__x_win_label.pack(side='left')
        self.__x_win.pack(side='left')
        self.__o_win_label.pack(side = 'left')
        self.__o_win.pack(side = 'left')
        self.__num_ties_label.pack(side = 'left')
        self.__ties.pack(side = 'left')
        self.__window.mainloop()

    #Update the number of wins x has
    #Invokes set()
    def update_x_wins(self): 
        self.__num_x_wins.set(self.player.get_x_wins())
        
    def update_o_wins(self):
        self.__num_o_wins.set(self.player.get_o_wins())

    def update_ties(self):
        self.__num_ties.set(self.player.get_ties())
        
    def start_game(self):
        for button in self.__button_list:
            button.config(state = NORMAL)

    def reset_game(self):
        i=0
        for button in self.__button_list:
            button.config(state = DISABLED,text=self.__text_list[i])
            i+=1
        self.board.reset()
        self.player.reset()
        self.update_x_wins()
        self.update_o_wins()

    #Responsible for all button functions
    def button_click(self, button_id,text):
        self.player.inc_turn()
        team = self.player.set_team()
        if team == 'X':
            self.board.add_x(button_id)
            if button_id == 1:
                self.__button1.config(state = DISABLED,text = team)#image=self.__x_image)
            elif button_id == 2:
                self.__button2.config(state = DISABLED,text = team)
            elif button_id == 3:
                self.__button3.config(state = DISABLED,text = team)
            elif button_id == 4:
                self.__button4.config(state = DISABLED,text = team)
            elif button_id == 5:
                self.__button5.config(state=DISABLED,text = team)
            elif button_id == 6:
                self.__button6.config(state=DISABLED,text = team)
            elif button_id == 7:
                self.__button7.config(state=DISABLED,text = team)
            elif button_id == 8:
                self.__button8.config(state=DISABLED,text = team)
            elif button_id == 9:
                self.__button9.config(state=DISABLED,text = team)
        else:
            self.board.add_o(button_id)
            if button_id == 1:
                self.__button1.config(state = DISABLED,text = team)
            elif button_id == 2:
                self.__button2.config(state = DISABLED, text = team)
            elif button_id == 3:
                self.__button3.config(state = DISABLED, text = team)
            elif button_id == 4:
                self.__button4.config(state=DISABLED,text = team)
            elif button_id == 5:
                self.__button5.config(state=DISABLED,text = team)
            elif button_id == 6:
                self.__button6.config(state=DISABLED,text = team)
            elif button_id == 7:
                self.__button7.config(state=DISABLED,text = team)
            elif button_id == 8:
                self.__button8.config(state=DISABLED,text = team)
            elif button_id == 9:
                self.__button9.config(state=DISABLED,text = team)
        if self.board.check_for_wins():
            #DISABLE BUTTONS
            if self.board.x_wins():
                message = "X wins!"
                self.player.inc_x_wins()
                self.update_x_wins()
            else:
                message = "O wins!"
                self.player.inc_o_wins()
                self.update_o_wins()
            messagebox.showinfo("Winner!", message)
            self.reset_game()
        elif (not self.board.check_for_wins()) and (self.board.full_board()):
            message = "Tie!"
            self.player.inc_ties()
            messagebox.showinfo("No winner...", message)
            self.reset_game()
            self.update_ties()
        
    def graph_wins(self):
        objects = ('X', 'O','Ties')
        y_pos = np.arange(len(objects))
        x = int(self.player.get_x_wins())
        o = int(self.player.get_o_wins())
        ties = int(self.player.get_ties())
        performance = [x,o,ties]
        plt.bar(y_pos, performance, align='center', alpha=1.0)
        plt.xticks(y_pos, objects)
        plt.ylabel('Number of Wins')
        plt.title('Number of X and O Wins')
        plt.show()
        
tttGUI()         
            
                
            
            
        
