from random import choice
import random

doors = ['A', 'B', 'C']
change_win = 0
notChange_win = 0
n =10000

for i in range(n):
    true_door = choice(doors)
    c = choice(doors)
    print('your choise is', c)

    notChoiseDoor = doors.copy()
    notChoiseDoor.remove(c)


    if true_door == c:
        opened = choice(notChoiseDoor)
        print('The presenter opened the door', opened)
        notChange_win += 1

    else:
        notChoiseDoor.remove(true_door)
        print('The presenter opened the door', notChoiseDoor)
        change_win += 1

print(change_win/n, notChange_win/n)

