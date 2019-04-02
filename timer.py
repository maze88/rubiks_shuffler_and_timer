#!/usr/bin/python3
import time

def timeSolve(inspectionTime = 0):
  if inspectionTime:
    inspect(inspectionTime)
  input('\nPress ENTER to start solve timer...')
  start_time = time.time()
  input('Started!\nTiming... Press ENTER to stop!')
  end_time = time.time()
  print('Stopped.\n')
  solveTime = round(end_time - start_time, 4)
  return solveTime

def displaySessionTimes(sessionTimes):
  if len(sessionTimes):
    print('Session results')
    print('---------------')
    for solveDate, solveTime in sessionTimes.items():
      print('  {}: {}s'.format(solveDate, solveTime))
    if len(sessionTimes) > 1:
      average = round(sum(sessionTimes.values())/len(sessionTimes), 4)
      best = min(sessionTimes.values())
      print('Best solve: {}'.format(best))
      print('Average solve: {}'.format(average))
      print('---------------------\n')
  else:
    print('\nNo solves yet in session. Why not have a go?')

def saveSolveToSession(solve):
  sessionTimes[time.ctime()] = solve

def inspect(seconds):
  input('\nInspection time: {} seconds. Press ENTER to start!'.format(seconds))
  while seconds:
    print(seconds)
    seconds -= 1

sessionTimes = {}

def main():
  while True:
    displaySessionTimes(sessionTimes)
    solveTime = timeSolve()
    #print('Result: {} seconds.'.format(solveTime))
    saveSolveToSession(solveTime)

if __name__ == '__main__':
  main()
