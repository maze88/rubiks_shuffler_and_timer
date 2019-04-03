#!/usr/bin/python3
import time
import sys
#from shuffle import *  # TODO uncomment when shuffle.py is in repo.

def inspectionTime(inspectionSeconds):
  """Lets the user start a countdown for cube inspection time."""
  _ = input('\nInspection time: {} seconds. Press ENTER to start inspection (or `q` to quit)!'.format(inspectionSeconds))
  if _ == 'q':
    exit()
  while inspectionSeconds:
    print(inspectionSeconds)
    inspectionSeconds -= 1
    time.sleep(1)
  print('Inspection time over.')

def timeSolve(inspectionSeconds):
  """Lets the user start a timer for cube solving."""
  if inspectionSeconds:
    inspectionTime(inspectionSeconds)
  _ = input('\nPress ENTER to start timer and solve (or `q` to quit)...')
  start_time = time.time()
  if _ == 'q':
    exit()
  input('Started!\nTiming... Press ENTER to stop!')
  end_time = time.time()
  print('Stopped.\n')
  solveTime = round(end_time - start_time, 4)
  return solveTime

def saveSolveToSession(session, solveTime):
  """Stores solve to session array as a tuple containing date/time and `solveTime`."""
  solve = (time.ctime(), solveTime)
  session.append(solve)

def displaySessionSolves(sessionSolves):
  """Prints the sessions solve times and average, tagging the best, worst and latest ones."""
  if len(sessionSolves):
    all_times = [solve[1] for solve in sessionSolves]
    best = min(all_times)
    worst = max(all_times)
    total = 0
    print('Session results')
    print('---------------')
    for i, solve in enumerate(sessionSolves):
      index = '  '
      tag = ''
      if len(sessionSolves) > 1:
        index = str(i + 1) + '.'
        if solve[1] == best:
          tag += ' <- Best'
        if solve[1] == worst:
          tag += ' <- Worst'
        if i == len(sessionSolves) - 1:
          tag += ' (Last solve)'
      print('{} {}\t{} seconds{}'.format(index, solve[0], solve[1], tag))
      total += solve[1]
    if len(sessionSolves) > 1:
      average = round(total/len(all_times), 4)
      print('Average solve: {}'.format(average))
      print('------------------\n')
  else:
    print('\nLets cube!')

def oneSessionSolve(sessionSolves, inspectionSeconds):
  displaySessionSolves(sessionSolves)
  solve_time = timeSolve(inspectionSeconds)
  saveSolveToSession(sessionSolves, solve_time)


"""Main"""
def main(inspectionSeconds):
  """Starts an eternal loop session for cube solvings."""
  session_solves = []
  while True:
    aSolveForSession(session_solves, inspectionSeconds)
    #shuffle(randMoves)  # TODO rename to main shuffle method from shuffle.py.

if __name__ == '__main__':
  inspection_seconds = 0
  if len(sys.argv) > 1:
    inspection_seconds = abs(int(sys.argv[1]))
  main(inspection_seconds)
