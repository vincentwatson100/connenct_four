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
#                if self.grid[0][col] == ' ':
#                    return False
#            return True

import re

class Board:
    def __init__(self):
        # self.grid = [[' ' for _ in range(7)] for _ in range(6)] # Simple way to do the same thing.
        self.grid = [[]]
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



  



































