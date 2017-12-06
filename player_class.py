class Player():

    def __init__(self):

        self.__team = ''
        self.__turn = 0
        self.__x_wins = 0
        self.__o_wins = 0
        self.__ties = 0

    def get_o_wins(self):
        return self.__o_wins

    def get_x_wins(self):
        return self.__x_wins

    def get_ties(self):
        return self.__ties
    
    def set_team(self):
        if self.__turn % 2 == 0:
            self.__team = 'X'
        else:
            self.__team = 'O'
        return self.__team


    def inc_turn(self):
        self.__turn += 1

    def inc_x_wins(self):
        self.__x_wins += 1

    def inc_o_wins(self):
        self.__o_wins +=1

    def inc_ties(self):
        self.__ties +=1

    def reset(self):
        self.__team = ''
        self.__turn = 0

