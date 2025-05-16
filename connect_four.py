# Week 4 - Enhancing the Game with Persistent Save/Load Functionality and Screen Clearing
#
# Instructions:
# 1. Add a free function to clear the screen.
#    - Define a function named `clear_screen`.
#    - Use the `os` module to clear the screen based on the operating system.
#    - Call this function whenever you need to clear the screen in the game.
# 2. Enhance the `MainMenu` class to save to disk.
##    - Import the `json`` moduel at the top of the script.
##    - Add a new attribute `save_file` to the `MainMenu` class to store the file path for saving games.
##    - Add a method named `save_to_file` to the `MainMenu` class.
##        - Open the `save_file` in write mode and use the `json` module to write the `saved_games` dictionary to the file.
##        - Use the `json.dump` method to write the dictionary to the file.
#        - Call the `save_to_file` method when the game is saved in the `save_game` method.
#    - Add a method named `load_saved_games` to the `MainMenu` class.
#        - Check if the save file exists.
#        - If the file exists, open the file in read mode and use the `json` module to load the saved games into the `saved_games` dictionary.
#        - If the file does not exist, return an empty dictionary.
#       Update the `__init__` method in the `MainMenu` class to load the saved games from the file and store them in the `saved_games` attribute.

import json
import os  
import re


# TODO: Call the `clear_screen` function whenever you need to clear the screen in the game.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Board:
    def __init__(self):
        # self.grid = [[' ' for _ in range(7)] for _ in range(6)] # Simple way to do the same thing.
        self.grid = []
        for row in range(6):
            self.grid.append([])
            for _ in range(7):
                self.grid[row].append(' ')

    def print_board(self):
        for i, row in enumerate(self.grid):
            print('|'.join(row))
            print('-' * 13)
        print('0 1 2 3 4 5 6')  # Add row numbers to the bottom

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
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.board.print_board()
            try:
                column = int(input(f"Player {self.current_player}, choose a column (0-6) or -1 to save and exit: "))
                if column == -1:
                    return 'save'
                if not self.board.drop_disc(column, self.current_player):
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 6.")
                continue
            winner = self.board.check_winner()
            if winner:
                self.board.print_board()
                print(f"Player {winner} wins!")
                return 'win'
            if self.board.is_full():
                self.board.print_board()
                print("The game is a draw!")
                return 'draw'
            self.switch_player()

    def deserialize(self, saved_game):
        self.board.grid = saved_game['board']
        self.current_player = saved_game['current_player']

    def serialize(self):
        return {'board': self.board.grid, 'current_player': self.current_player}

class MainMenu:
    def __init__(self):
        self.save_file = 'connectFourSave.json'
        # TODO: Load the saved games using the `load_saved_games` method.
        self.saved_games = self.load_saved_games()

        

    def show_menu(self):
        while True:
            print("1. Exit")
            print("2. Start New Game")
            if self.saved_games:
                print("3. Load Saved Game")
            choice = input("Enter your choice: ")
            if choice in ['1', '2'] or (choice == '3' and self.saved_games):
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_saved_game(self):
        while True:
            saved_game_names = list(self.saved_games.keys())
            print("Saved games:")
            for game_name in saved_game_names:
                print(f"- {game_name}")
            chosen_game_name = input("Enter the name of the saved game to load: ")
            if chosen_game_name in saved_game_names:
                return self.load_game(chosen_game_name)
            else:
                print("Invalid input. Please enter a valid game name.")

    def load_game(self, game_name):
        game_state = self.saved_games.get(game_name)
        game = Game()
        game.deserialize(game_state)
        return game
    
    def save_game(self, game_name, game):
        self.saved_games[game_name] = game.serialize()
        self.save_to_file()     

    def save_to_file(self):
        
        with open(self.save_file, "w")as file:
            json.dump(self.saved_games, file)

        # TODO: Use the json module to save the saved_games dictionary to the save file.
        

    def load_saved_games(self):
        #- Check if the save file exists.
        #- If the file exists, open the file in read mode and use the `json` module to load the saved games into the `saved_games` dictionary.
        #- If the file does not exist, return an empty dictionary.
        try:
            file_handle = open(self.save_file, "r")
            return json.load(file_handle)
        except:
            return {}
        
        #if os.path.exists(self.save_file):
        #    with open(self.save_file, "r") as file:
        #        return json.load(file)
        #else:
        #    return {}
        #    

    def play_game(self, game):
        outcome = game.play()
        if outcome == 'save':
            game_name = input("Enter the name of the game: ")
            self.save_game(game_name, game)
            print("Game saved.")
        elif outcome == 'draw':
            print("The game is a draw.")
        elif outcome in ['X', 'O']:
            print(f"Player {outcome} wins!")

    def run(self):
        while True:
            choice = self.show_menu()

            if choice == '1':
                break
            elif choice == '2':
                game = Game()
                self.play_game(game)
            elif choice == '3':
                saved_game = self.get_saved_game()
                self.play_game(saved_game)

if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.run()









obj = MainMenu()
print(obj.save_to_file())

obj = MainMenu()
print(obj.load_saved_games())













































