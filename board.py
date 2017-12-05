class Board():
    ttt = [
    ['A1','A2','A3'],
    ['B1','B2','B3'],
    ['C1','C2','C3']
    ]
    TEAMS = ['X','O']

    def __init__(self,space,team):
        self.__space = space
        self.__team = team #X or O
        self.__current_board = Board.ttt[:]


    def get_space(self,space):
        return space

    def get_team(self,team):
        return team

    def get_position(self,space):
        index0 = int(ord(space[0]))-65
        index1 = int(space[1])-1
        position = [index0,index1]
        return position

    def get_current_board(self):
        return self.__current_board

    def valid_space(self,space):
        return (space in Board.ttt[0] or space in Board.ttt[1] or space in Board.ttt[2])

    def valid_team(self):
        return self.__team.upper() in TEAMS

    def open_space(self,space):
        return not (self.__current_board[self.get_position(space)[0]][self.get_position(space)[1]] in Board.TEAMS)

    #Mutators
    def set_winning_lists(self,x):
        winning_lists = [
            [x[0][0],x[0][1],x[0][2]],
            [x[1][0],x[1][1],x[1][2]],
            [x[2][0],x[2][1],x[2][2]],
            [x[0][0],x[1][0],x[2][0]],
            [x[0][1],x[1][1],x[2][1]],
            [x[0][2],x[1][2],x[2][2]],
            [x[0][0],x[1][1],x[2][2]],
            [x[0][2],x[1][1],x[2][0]]
            ]
        return winning_lists

    def choose_space(self,space,team):
      position = self.get_position(space)
      self.__current_board[position[0]][position[1]] = team.upper()

    def reset_board(self):
        self.__current_board = [
            ['A1','A2','A3'],
            ['B1','B2','B3'],
            ['C1','C2','C3']
            ]

    def o_wins(self):
        winning_lists = self.set_winning_lists(self.__current_board)
        for lists in winning_lists:
            if(lists[0]=='O' and lists[1]=='O' and lists[2]=='O'):
                return True

    def x_wins(self):
        winning_lists = self.set_winning_lists(self.__current_board)
        for lists in winning_lists:
            if (lists[0]=='X' and lists[1]=='X' and lists[2]=='X'):
                return True

    def check_for_wins(self):
        return self.x_wins() or self.o_wins()

    def full_board(self):
        num = 0
        temp_board = self.__current_board[:]
        for lists in temp_board:
            list2 = [1 for i in lists if (i=='X' or i=='O')]
            for i in list2:
                num+=i
        return num==9
            

    def print_board(self): 
        for lists in self.__current_board:
            for i in lists:
                print("|%2s" %i, end = "")
            print("|\n")

class Player():
    TEAMS = ['X','O']
    def __init__(self,team):
        self.__team = team

    def get_team(self):
        return self.__team

    def valid_team(self):
        return self.__team in Player.TEAMS

        

X_MESSAGE = "X wins!"
O_MESSAGE = "O wins!"
TIE_MESSAGE = "Tie!"

def main():
    
    x_wins = 0
    o_wins = 0
    ties = 0
    space = ''
    team = ''
    board = Board(space,team)
    answer = 'x'
    team1 = input("player 1 choose a team")
    while not board.valid_team:
        team1 = input("choose either x or o")
    if team1.upper() == 'X':
        team2 = 'O'
    else:
        team2 = 'X'
    player1 = Player(team1)
    player2 = Player(team2)
    print("Player 1 is %s\nPlayer 2 is %s" %(player1.get_team(),player2.get_team()))
    players = [player1,player2]
    while answer:
        board.reset_board()
        while (not board.check_for_wins()) and (not board.full_board()):
            player_num = 0
            for player in players:
                if not board.check_for_wins() and not board.full_board():
                    player_num += 1
                    board.print_board()
                    space = input("Player %d choose a space: " %player_num)
                    while not board.valid_space(space):                     
                        space = input("choose a valid space: ")
                    while not board.open_space(space):
                        space = input("choose an open space: ")
                    team = player.get_team()
                    board.choose_space(space,team)
                else:
                    if board.check_for_wins():
                        if board.x_wins():
                            x_wins += 1
                            print(X_MESSAGE)
                        elif board.o_wins():
                            o_wins += 1
                            print(O_MESSAGE)
                        else:
                            ties += 1
                            print(TIE_MESSAGE)
                        
        print("X: %d\nO: %d\nTies: %d" %(x_wins,o_wins,ties))
        answer = input("Press any key to play again or <enter> to quit")

main()
                
            
    
        
    
        

 
    
        
            
