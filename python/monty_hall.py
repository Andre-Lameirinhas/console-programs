from random import randint
from typing import List
from sys import argv
from time import perf_counter


# TODO add randomness to opened door
def open_goat_door(doors: List[str], selected_door_n: int):
    opened_door_n = -1
    for n, content in enumerate(doors):
        if n != selected_door_n and content != 'car':
            opened_door_n = n
            break
    return opened_door_n


def generate_doors(n_doors: int):
    prize_door_n = randint(0, n_doors - 1)
    doors = []
    for n in range(n_doors):
        if n == prize_door_n:
            doors.append('car')
        else:
            doors.append('goat')
    return doors


def play_game(switch: bool, n_doors: int = 3):

    doors = generate_doors(n_doors)
    #print(doors)

    selected_door_n = randint(0, n_doors - 1)
    #print(f'selected door = {selected_door_n}')

    opened_door_n = open_goat_door(doors, selected_door_n)
    #print(f'opened door = {opened_door_n}')

    door_indices = [*range(n_doors)]
    door_indices.remove(selected_door_n)
    door_indices.remove(opened_door_n)
    switch_door_n = door_indices.pop()
    #print(f'switch door = {switch_door_n}')

    final_door_n = -1
    if switch:
        final_door_n = switch_door_n
        #print('You decided to switch doors')
    else:
        final_door_n = selected_door_n
        #print('You decided to stick to the first door')

    if doors[final_door_n] == 'car':
        #print('You win!')
        return 'win'
    else:
        #print('You lose...')
        return 'loss'


# TODO run both cases in parallel
if __name__ == '__main__':

    if len(argv) > 2:
        print('invalid number of args')
        exit(1)

    iterations = 10000

    if len(argv) == 2:
        iterations = int(argv[1])

    print(f'executing Monty Hall scenario {iterations} times')

    start = perf_counter()

    stick_wins = 0
    for i in range(iterations):
        res = play_game(
            switch=False
        )
        if res == 'win':
            stick_wins += 1
    print(f'stick strategy win rate = {stick_wins / iterations * 100:.3f} %')

    switch_wins = 0
    for i in range(iterations):
        res = play_game(
            switch=True
        )
        if res == 'win':
            switch_wins += 1
    print(f'switch strategy win rate = {switch_wins / iterations * 100:.3f} %')

    end = perf_counter()
    print(f"elapsed time: {end - start:.3f} s")
