import time
import sys

print(' ')
print('Countdown Timer')
print(' ')
print('Input time to countdown from.')
print(' ')

c=':'

hourz=input('Hours: ')
minz=input('Minutes: ')
secz=input('Seconds: ')
print(' ')

hour=int(hourz)
min=int(minz)
sec=int(secz)

while hour > -1:
    while min > -1:
        while sec > 0:
            sec=sec-1
            time.sleep(1)
            sec1 = ('%02.f' % sec)  # format
            min1 = ('%02.f' % min)
            hour1 = ('%02.f' % hour)
            sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))

        min=min-1
        sec=60
    hour=hour-1
    min=59

print('\nCountdown Complete.')