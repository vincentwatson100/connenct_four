





class board:
    def __init__(self, grid, print_board, drop_disc):
        self.grid = grid
        self.print_board = print_board 
        self.drop_disc = drop_disc





num = ('0 1 2 3 4 5 6')
x = ('x')
o = ('o')
disc= input(f'are you {x} or {o}:')
print(disc)

for _ in range(6):


    print('| | | | | | | |')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _')


print(num)
column = input('column number:')

print(column)

for _ in range(1,6):
    if column == '0':
        print('True')
    elif column == '1':
        print('True')
    elif column == '2':
        print('True')
    elif column == '3':
        print('True')
    elif column == '4':
        print('True')
    elif column == '5':
        print('True')
    elif column == '6':
        print('True')

    else:
        input('False, try again')

  



































