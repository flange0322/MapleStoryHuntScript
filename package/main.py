import time
from characterMovement import dualBlade as db

def counter():
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)

start = db.dual_Blade()
counter()
while True:
    start.script4()