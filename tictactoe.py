values = {'1 3': 0, '2 3': 1, '3 3': 2,
          '1 2': 3, '2 2': 4, '3 2': 5,
          '1 1': 6, '2 1': 7, '3 1': 8}

cells = input('Enter cells: ').strip()

cells = cells.replace('_', ' ')

list_ = list(cells)

wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]

output = f"""
---------
| {list_[0]} {list_[1]} {list_[2]} |
| {list_[3]} {list_[4]} {list_[5]} |
| {list_[6]} {list_[7]} {list_[8]} |
---------
"""


def update():
    if list_.count('X') > list_.count('O'):
        list_[values[coordinates]] = 'O'
    elif list_.count('X') < list_.count('O'):
        list_[values[coordinates]] = 'X'
    else:
        list_[values[coordinates]] = 'X'
    print(f"""
---------
| {list_[0]} {list_[1]} {list_[2]} |
| {list_[3]} {list_[4]} {list_[5]} |
| {list_[6]} {list_[7]} {list_[8]} |
---------
""")


def game_state():
    for i in range(8):
        print(i)
        print(list_[wins[i][0]], list_[wins[i][1]], list_[wins[i][2]])
        if list_[wins[i][0]] == 'X' and list_[wins[i][1]] == 'X' and list_[wins[i][2]] == 'X':
            print('X wins')
            exit()
        elif list_[wins[i][0]] == 'O' and list_[wins[i][1]] == 'O' and list_[wins[i][2]] == 'O':
            print('O wins')
            exit()
    if list_.count('_') == 0:
        print('Draw')
    else:
        print('Game not finished')


while True:
    print(output)
    while True:
        coordinates = input('Enter the coordinates: ').strip()
        try:
            if int(coordinates.replace(' ', '')[0]) > 3 or int(coordinates.replace(' ', '')[1]) > 3 or \
                  int(coordinates.replace(' ', '')[0]) < 1 or int(coordinates.replace(' ', '')[1]) < 1:
                print('Coordinates should be from 1 to 3!')
                continue
            elif cells[values[coordinates]] == 'X' or cells[values[coordinates]] == 'O':
                print('This cell is occupied! Choose another one!')
                continue
            else:
                update()
                game_state()
                exit()
        except ValueError:
            print('You should enter numbers!')
            continue
