#!/usr/bin/python3
import time

def timeSolve(inspectionTime = 0):
  if inspectionTime:
    inspect(inspectionTime)
  _ = input('\nPress ENTER to start solve timer (or `q` to exit)...')
  start_time = time.time()
  if _ == 'q':
    exit()
  input('Started!\nTiming... Press ENTER to stop!')
  end_time = time.time()
  print('Stopped.\n')
  solveTime = round(end_time - start_time, 4)
  return solveTime

def displaySessionSolves(sessionSolves):
  if len(sessionSolves):
    times = [solve[1] for solve in sessionSolves]
    best = min(times)
    worst = max(times)
    total = 0
    print('Session results')
    print('---------------')
    for i, solve in enumerate(sessionSolves):
      tag = ''
      if len(sessionSolves) > 1:
        if solve[1] == best:
          tag += ' <- Best'
        if solve[1] == worst:
          tag += ' <- Worst'
        if i + 1 == len(sessionSolves):
          tag += ' <- Latest'
      print('  {}: {} seconds{}'.format(solve[0], solve[1], tag))
      total += solve[1]
    if len(sessionSolves) > 1:
      average = round(total/len(times), 4)
      print('Average solve: {}'.format(average))
      print('------------------\n')
  else:
    print('\nNo solves yet in session. Why not have a go?')

def saveSolveToSession(solve):
  sessionSolves.append((time.ctime(), solve))

def inspect(seconds):
  input('\nInspection time: {} seconds. Press ENTER to start inspection!'.format(seconds))
  while seconds:
    print(seconds)
    seconds -= 1

sessionSolves = []

def main():
  while True:
    displaySessionSolves(sessionSolves)
    solveTime = timeSolve()
    saveSolveToSession(solveTime)

if __name__ == '__main__':
  main()
