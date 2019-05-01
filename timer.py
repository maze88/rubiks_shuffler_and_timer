#!/usr/bin/python3
"""This is the main module for the Rubik's shuffler and timer project. It calls directly or indirectly all other modules."""

import time
import sys
from shuffle import *

def ascii_cube():
    """Prints ascii art of a Rubik's cube."""
    with open('cube.ascii', 'r') as f:
        ascii_cube = f.readlines()
        for line in ascii_cube:
            print(line, end = '')

def inspection_time(inspection_seconds):
    """Lets the user start a countdown for cube inspection time."""
    _ = input('\nInspection time: {} seconds. Press ENTER to start inspection (or `q` to quit)!'.format(inspection_seconds))
    if _ == 'q':
        exit()
    while inspection_seconds:
        print(inspection_seconds)
        inspection_seconds -= 1
        time.sleep(1)
    print('Inspection time over.')

def time_solve(inspection_seconds):
    """Lets the user start a timer for cube solving."""
    if inspection_seconds:
        inspection_time(inspection_seconds)
    _ = input('\nPress ENTER to start timer and solve (or `q` to quit)...')
    start_time = time.time()
    if _ == 'q':
        exit()
    input('Started!\nTiming... Press ENTER to stop!')
    end_time = time.time()
    print('Stopped.\n\n')
    solve_time = round(end_time - start_time, 4)
    return solve_time

def save_solve_to_session(session, solve_time):
    """Stores solve to session array as a tuple containing date/time and `solve_time`."""
    solve = (time.ctime(), solve_time)
    session.append(solve)

def display_session_solves(session_solves):
    """Prints the sessions solve times and average, tagging the best, worst and latest ones."""
    if session_solves:
        all_times = [solve[1] for solve in session_solves]
        best = min(all_times)
        worst = max(all_times)
        total = 0
        print('Session results')
        print('---------------')
        for i, solve in enumerate(session_solves):
            index = '  '
            tag = ''
            if len(session_solves) > 1:
                index = str(i + 1) + '.'
                if solve[1] == best:
                    tag += ' <- Best'
                if solve[1] == worst:
                    tag += ' <- Worst'
                if i == len(session_solves) - 1:
                    tag += ' (Last solve)'
            print('{} {}\t{} seconds{}'.format(index, solve[0], solve[1], tag))
            total += solve[1]
        if len(session_solves) > 1:
            average = round(total/len(all_times), 4)
            print('Average solve: {}'.format(average))
    else:
        print('\nLets cube!')

def display_last_5_running_average(session_solves):
    """Prints the running average (not including best & worst) for the last 5 solves."""
    if len(session_solves) >= 5:
        last_5 = [solve[1] for solve in session_solves[-5:]]
        last_5.remove(min(last_5))
        last_5.remove(max(last_5))
        running_average = round(sum(last_5)/len(last_5), 4)
        print('Running average (not including best & worst) for last 5 solves: {}'.format(running_average))

def solve_cycle_unit(session_solves, inspection_seconds, shuffle_move_count, shuffle_move_spacing):
    """Displays current session results and cube shuffling instructions, then times a solve."""
    ascii_cube()
    display_session_solves(session_solves)
    display_last_5_running_average(session_solves)
    shuffle(shuffle_move_count, shuffle_move_spacing)
    solve_time = time_solve(inspection_seconds)
    save_solve_to_session(session_solves, solve_time)


def main(inspection_seconds, shuffle_move_count, shuffle_move_spacing):
    """Starts an eternal loop session for cube solvings."""
    session_solves = []
    while True:
        solve_cycle_unit(session_solves, inspection_seconds, shuffle_move_count, shuffle_move_spacing)

if __name__ == '__main__':
    INSPECTION_SECONDS = 0
    SHUFFLE_MOVES = 32
    SHUFFLE_MOVE_SPACE_FREQ = 4
    try:
        if len(sys.argv) > 1:
            INSPECTION_SECONDS = abs(int(sys.argv[1]))
            if len(sys.argv) > 2:
                SHUFFLE_MOVES = abs(int(sys.argv[2]))
                if len(sys.argv) > 3:
                    SHUFFLE_MOVE_SPACE_FREQ = abs(int(sys.argv[3]))
    except:
        ascii_cube()
        print('Usage: $./timer.py [seconds for inspection] [amount of shuffle moves] [shuffle move space frequency]')
        exit()
    main(INSPECTION_SECONDS, SHUFFLE_MOVES, SHUFFLE_MOVE_SPACE_FREQ)
