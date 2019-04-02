#!/usr/bin/python3
import time

x = input('Press enter to start timer...')
startTime = time.time()
print('Timing...')
x = input('Press enter to stop timer!...')
print('Stopped.')
endTime = time.time()

result = round(endTime - startTime, 4)
print('Result: Timed {} seconds.'.format(result))
