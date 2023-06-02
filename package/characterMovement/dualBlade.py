import keyboard
from . import characterPrototype as cp
import time

class dual_Blade(cp.common_Skills):
    def __init__(self):
        pass
    def blade_Fury(self):
        keyboard.send('v')
        time.sleep(0.55)
        print('短刀護佑')

    def sudden_Raid(self):
        keyboard.send('s')
        time.sleep(0.5)
        print('穢土轉生')

    def blades_Of_destiny(self):
        keyboard.send('shift')
        time.sleep(0.3)
        print('炎獄修羅斬')

    def blade_Tornado(self):
        keyboard.send('d')
        time.sleep(0.3)
        print('疾刃颶風')
    
    def final_Cut(self):
        keyboard.send('a')
        time.sleep(0.3)
        print('絕殺刃')
    
    def script4(self):
        time.sleep(2)
        self.frenzy_Totem()
        time.sleep(1.5)
        for i in range(50):
            print('---------------第' + str(i + 1) + '輪---------------')
            for i in range(5):
                self.blade_Fury()

                keyboard.press('right')
                keyboard.send('space')
                time.sleep(0.05)
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                time.sleep(0.4)

                
                if i == 0:
                    self.blades_Of_destiny()
                if i == 1:
                    self.erda_Shower()
                elif i == 2:
                    self.blade_Tornado()

                keyboard.release('right')
                time.sleep(0.3)

            self.rope_Lift()

            for i in range(5):
                self.blade_Fury()

                keyboard.press('left')
                keyboard.send('space')
                time.sleep(0.05)
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                time.sleep(0.4)

                if i == 0:
                    self.true_Arachnid_reflection()
                elif i == 1:
                    self.blades_Of_destiny()
                elif i == 2:
                    self.blade_Tornado()
                elif i == 3:
                    self.solar_Crest()
                elif i == 4:
                    self.sudden_Raid()

                keyboard.release('left')
                time.sleep(0.5)