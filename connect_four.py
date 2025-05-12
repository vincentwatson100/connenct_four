import json
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
        
    def deserialize(self, saved_game):
        self.board.grid = saved_game['board']
        self.current_player = saved_game['current_player']
        


    def serialize(self):
        return {'board': self.board.grid, 'current_player': self.current_player}
        

class MainMenu:
    def __init__(self):
        self.board = board

    def show_menu(self):
        while True:
            print("1.Exit")
            print("2.Start a new Game")
            print("3. Load a saved game")
            if self.saved_games:
                print("3. Load a saved game")
            try:
                choice = int(input("Enter you choice:"))
                if choice in [1, 2] or (choice == 3 and self.saved_games):
                    return choice
                else:
                    raise TypeError
            except:
                print("please enter a valid number")


    
    
    
    
    
    
    def get_saved_game(self):
        while True:
            saved_game_names = list(self.saved_games.keys())
            print("Saved games:")

            for game_name in saved_game_names:
                print(f"- {game_name}")
            chosen_game_name = input("Enter the name of the game to load:")
            if chosen_game_name in saved_game_names:
                return self.load_game(chosen_game_name)
            else:
                print("invalid input. Please enter a valid game name:")
    def save_game(self, game_name: str, game: Game):
        
        self.saved_games[game_name] = game.serialize()
    
    
    
    
    def load_game(self, game_name):
        saved_games = {}# TODO: Load the game state from the saved games dictionary and return a new Game instance.
        return self.game_name(saved_games)
        
        game_state = self.saved_games[game_name]
        game = Game()
        game.deserialize(game_state)
        return game

        # The key used to save the game will be the `game_name`.
        # The value will be serialized game using `game.serialize()`.
        pass
    def play_game(self, game=Game()):
        outcome = game.play()
        if outcome == "save":
            game_name = input("Please enter a game name")
            self.save_game(game_name, game)
            print(f"game was saved as {game_name}")
            print("save the game")
        elif outcome == "draw":
            print("The game is a draw. No one wins.")
        elif outcome in ["X", "o"]:
            print(f"Congratulations Player {outcome} wins!!!")

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == 1:
                break
            elif choice == 2:
                self.play_game()
            elif choice == 3:
                saved_game = self.get_saved_game()
                self.play_game(saved_game)
    def save_file(self):
        pass
    def save_to_file(self):
        pass





if __name__ == "__main__":

    main_menu = MainMenu()
    main_menu.run()

obj = Game()
obj.board.print_board()

obj = Game()
obj.play()

board = Board()
winner = board.check_winner()
print(winner)


obj = Board()
print(obj.is_full())

obj = MainMenu()
print(obj.show_menu())




























































