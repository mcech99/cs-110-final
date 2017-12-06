class Board():
    WINNING_LISTS = [[1,2,3],[4,5,6],[7,8,9],
                     [1,4,7],[2,5,8],[3,6,9],
                     [1,5,9],[3,5,7]
                     ]
    
    def __init__(self):

        self.__x_list = []
        self.__o_list = []

    def set_list(self,button_list):
        self.__list = button_list

    def full_board(self):
        temp_list = self.__x_list + self.__o_list
        return len(temp_list) == 9

    def add_x(self,button_id):
        self.__x_list.append(button_id)

    def add_o(self,button_id):
        self.__o_list.append(button_id)

    def x_wins(self):
        for lists in Board.WINNING_LISTS:
            if lists[0] in self.__x_list and lists[1] in self.__x_list and lists[2] in self.__x_list:
                return True
    def o_wins(self):
        for lists in Board.WINNING_LISTS:
            if lists[0] in self.__o_list and lists[1] in self.__o_list and lists[2] in self.__o_list:
                return True 

    def check_for_wins(self):
        return self.x_wins() or self.o_wins()

    def reset(self):
        self.__x_list = []
        self.__o_list = []
            
        
        
