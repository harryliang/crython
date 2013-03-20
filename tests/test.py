#encoding=utf8

from crython import crython
import time

# @crython.job(expr='@minutely')
@crython.job(expr='0 * * * * * *')
def task1():
    print 'task1 will be called every minitus'

@crython.job(expr='0 0 * * *')
def task2():
    print 'task2 will be called every hour'

crython.tab.start()

while True:
    time.sleep(10000)