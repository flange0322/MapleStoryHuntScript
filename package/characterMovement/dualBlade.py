import keyboard
from . import characterPrototype as cp
import time

class dual_Blade(cp.common_Skills):
    def __init__(self):
        pass
    def blade_Fury(self):
        keyboard.send('v')
        time.sleep(0.4)
        print('短刀護佑')

    def sudden_Raid(self):
        keyboard.send('s')
        time.sleep(0.4)
        print('穢土轉生')

    def blades_Of_destiny(self):
        keyboard.send('shift')
        time.sleep(0.4)
        print('炎獄修羅斬')

    def blade_Tornado(self):
        keyboard.send('d')
        time.sleep(0.4)
        print('疾刃颶風')
    
    def final_Cut(self):
        keyboard.send('a')
        time.sleep(0.4)
        print('絕殺刃')
    
    def script(self):
        self.frenzy_Totem()
        time.sleep(2)
        for i in range(50):
            print('-------------------第'+str(i)+'輪-------------------')
            r_str = 'right'
            l_str = 'left'
            switch = False
            for i in range(10):
                if i == 5:
                    switch = True
                    self.rope_Lift()

                if not switch and i == 0:
                    keyboard.press(r_str)
                    time.sleep(0.05)
                    keyboard.release(r_str)
                elif switch and i == 5:
                    keyboard.press(l_str)
                    time.sleep(0.05)
                    keyboard.release(l_str)

                keyboard.press("space")
                time.sleep(0.02)
                keyboard.release("space")

                keyboard.press("space")
                time.sleep(0.02)
                keyboard.release("space")

                keyboard.press("space")
                time.sleep(0.02)

                if i % 5 == 0:
                    if not switch:
                        self.blade_Fury()
                    else:
                        self.erda_Shower()
                elif i % 5 == 1:
                    if not switch:
                        self.blades_Of_destiny()
                    else:
                        self.sudden_Raid()
                        self.blade_Fury()
                elif i % 5 == 2:
                    if not switch:
                        self.blade_Tornado()
                    else:
                        self.blade_Fury()
                elif i % 5 == 3:
                    if not switch:
                        self.blade_Fury()
                    else:
                        self.blade_Fury()
                elif i % 5 == 4:
                    if not switch:
                        self.blade_Fury()
                    else:
                        self.blade_Fury()

                keyboard.release("space")

                time.sleep(0.5)
            time.sleep(0.3)