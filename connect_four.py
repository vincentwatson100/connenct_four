#
#
#
#
#
##import re
#
#class board:
#    def __init__(self):
#        self.grid = [[]]
#        for row in range(6):
#            self.grid.append([])
#            for _ in range(7):
#                self.grid[row].append('')
#
#    def print_board(self):
#        for row in self.grid:
#            print('|'.join(row))
#            print('-'*13)
#            print('0 1 2 3 4 5 6')
#    def drop_disc(self, column, disc):
#        if column < 0 or column >= 7 or self.grid[0][column] != ' ':
#            return False
#        for row in reversed(self.grid):
#            if row[column] == ' ':
#                row[column] = disc
#                return True
#            return False
#        def check_winner(self):
#            rows = [''.join0(row)for row in self.grid]
#            cols = [''.join([self.grid[row][col]for row in range(6)])for col in range(7)]
#            rising_diags = [''.join([self.grid[row-i][i] for i in range(max(row-5, 0), min(row+1, 7))]) for row in range(3, 11) if min(row+1, 7) - max(row-5, 0) >= 4]
#            
#            falling_diags = [''.join([self.grid[row+i][i] for i in range(max(-row, 0), min(6-row, 7))]) for row in range(-3, 6) if min(6-row, 7) - max(-row, 0) >= 4]
#            for line in rows + cols + rising_diags + falling_diags:
#                match = re.search(r'X{4}|O{4}})', line)
#                if match:
#                    return match.group()[0]
#            return None
#        def is_full(self):
#            for col in range(7):
##                if self.grid[0][col] == ' ':
##                    return False
##            return True
#
#import re
#
#class Board:
#    def __init__(self, grid):
#        # self.grid = [[' ' for _ in range(7)] for _ in range(6)] # Simple way to do the same thing.
#        self.grid = [[]]
#        for row in range(6):
#            self.grid.append([])
#            for _ in range(7):
#                self.grid[row].append(' ')
#                print(grid)
#
#    def print_board(self, print_board):
#        for row in self.grid:
#            print('|'.join(row))
#            print('-' * 13)
#        print('0 1 2 3 4 5 6')
#        print(print_board)
#
#    def drop_disc(self, column, disc):
#        if column < 0 or column >= 7 or self.grid[0][column] != ' ':
#            return False
#        for row in reversed(self.grid):
#            if row[column] == ' ':
#                row[column] = disc
#                return True
#        return False
#
#    def check_winner(self, rows, cols):
#        rows = [''.join(row) for row in self.grid]
#        cols = [''.join([self.grid[row][col] for row in range(6)]) for col in range(7)]
#        rising_diags = [''.join([self.grid[row-i][i] for i in range(max(row-5, 0), min(row+1, 7))]) for row in range(3, 11) if min(row+1, 7) - max(row-5, 0) >= 4]
#        falling_diags = [''.join([self.grid[row+i][i] for i in range(max(-row, 0), min(6-row, 7))]) for row in range(-3, 6) if min(6-row, 7) - max(-row, 0) >= 4]
#        print(cols)
#        print(rows)
#        for line in rows + cols + rising_diags + falling_diags:
#            match = re.search(r'(X{4}|O{4})', line)
#            if match:
#                return match.group()[0]
#        return None
#    
#    def is_full(self, col):
#        for col in range(7):
#            if self.grid[0][col] == ' ':
#                return False
#        return True
#        print(col)
#print(Board.print_board)
#obj = Board()
#print(obj.print_board())
#
#
import os
import re

def clear_screen():
    os.system('cls')



class Board:
    def __init__(self):
        # self.grid = [[' ' for _ in range(7)] for _ in range(6)] # Simple way to do the same thing.
        self.grid = []
        for row in range(6):
            self.grid.append([])
            for _ in range(7):
                self.grid[row].append(' ')

    def print_board(self):
        for row in self.grid:
            print('|'.join(row))
            print('-' * 13)
        print('0 1 2 3 4 5 6')

    def drop_disc(self, column, disc):
        if column < 0 or column >= 7 or self.grid[0][column] != ' ':
            return False
        for row in reversed(self.grid):
            if row[column] == ' ':
                row[column] = disc
                return True
        return False

    def check_winner(self):
        rows = [''.join(row) for row in self.grid]
        cols = [''.join([self.grid[row][col] for row in range(6)]) for col in range(7)]
        rising_diags = [''.join([self.grid[row-i][i] for i in range(max(row-5, 0), min(row+1, 7))]) for row in range(3, 11) if min(row+1, 7) - max(row-5, 0) >= 4]
        falling_diags = [''.join([self.grid[row+i][i] for i in range(max(-row, 0), min(6-row, 7))]) for row in range(-3, 6) if min(6-row, 7) - max(-row, 0) >= 4]

        for line in rows + cols + rising_diags + falling_diags:
            match = re.search(r'(X{4}|O{4})', line)
            if match:
                return match.group()[0]
        return None
    
    def is_full(self):
        for col in range(7):
            if self.grid[0][col] == ' ':
                return False
        return True


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'      
    
    
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = 'X'
        

  
        
    def play(self):
        has_game_finished = False
        while True:
            #
            self.board.print_board()
            #
            try:
                column = int(input(f"Player{self.current_player}, choose a column 0-6 "))
                result_of_drop = self.board.drop_disc(column, self.current_player)
                if not result_of_drop:
                    print("Invalid move. Try again")
                    continue
            except:
            
                print("Invalid input. please enter a number from 0-6")
                continue
            winner = self.board.check_winner()
            if winner:
                self.board.print_board()
                print(f"player {winner} wins!!!!!!!!!!!!!!")
                break
            if self.board.is_full():
                print(" if was a tie: There was no winner try again soon!!!")
                print("better luck next time")
                break
            
            self.switch_player()
        

        def serialize(self):
            return {'board': self.board.grid, 'current_player': self.current_player}
        
    #def serialize(self):
        #return {'board': self.board.grid, 'current_player': self.current_player}


            





obj = Game()
obj.board.print_board()

obj = Game()
obj.play()

board = Board()
winner = board.check_winner()
print(winner)


obj = Board()
print(obj.is_full())


























































