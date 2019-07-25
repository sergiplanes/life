import random

board_state = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]


def dead_state(width, height):
    dead_state = [[0 for x in range(width)] for y in range(height)]
    return dead_state


w = 5
h = 5
print(dead_state(w, h))


def random_state(width, height):
    # Build the board using your previous work
    state = dead_state(width, height)

    # TODO: randomize each element of `state` to either 0 or 1
    for i in range(len(state)):
        for j in range(len(state[i])):
            cell_state = 0
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            state[i][j] = cell_state
    return state


print(random_state(w, h))

print( )

def render(state):
    from colorama import Fore, Back, Style
    """
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')
    Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Style: DIM, NORMAL, BRIGHT, RESET_ALL
    """
    #print(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                print(Fore.LIGHTBLACK_EX + " ", end=' ')
            else:
                print(Fore.LIGHTGREEN_EX + "#", end=' ')
        print()
    print(Style.RESET_ALL)

#a_dead_state = dead_state(20, 30)
#render(a_dead_state)

print()

a_random_state = random_state(20, 30)
render(a_random_state)


def calculate(state, new_state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            current_cell_value = state[i][j]
            # TODO: calculate the number of live neighbors...


def next_board_state(state):
    """
    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
    """
    new_state = dead_state(len(state[0]),len(state))
    
    calculate(state,new_state)


next_board_state(a_random_state)