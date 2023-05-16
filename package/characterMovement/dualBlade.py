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

    def script(self):
        time.sleep(2)
        self.frenzy_Totem()
        time.sleep(1)
        for i in range(50):
            time.sleep(0.8)
            print('---------------第' + str(i + 1) + '輪---------------')
            for i in range(3):
                self.blade_Fury()

                keyboard.press('left')
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                keyboard.send('space')
                time.sleep(0.2)

                keyboard.send('space + v')
                keyboard.release('left')
                time.sleep(0.6)
                
            self.blades_Of_destiny()
            self.rope_Lift()

            for i in range(4):
                self.blade_Fury()

                keyboard.press('right')
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                keyboard.send('space')
                time.sleep(0.2)

                if i == 0:
                    self.erda_Shower()
                elif i == 1:
                    self.blade_Tornado()
                elif i == 2:
                    self.sudden_Raid()
                
                keyboard.send('space + v')
                keyboard.release('right')
                time.sleep(0.6)
    
    def script2(self):
        time.sleep(2)
        self.frenzy_Totem()
        time.sleep(1.5)
        for i in range(50):
            time.sleep(0.5)
            print('---------------第' + str(i + 1) + '輪---------------')
            if i % 3 == 0:
                self.final_Cut()
            for i in range(3):
                self.blade_Fury()

                keyboard.press('left')
                keyboard.send('space')
                time.sleep(0.05)
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                time.sleep(0.2)

                if i == 0:
                    self.true_Arachnid_reflection()
                if i == 1:
                    self.erda_Shower()
                elif i == 2:
                    self.blades_Of_destiny()
                keyboard.send('space + v')
                keyboard.release('left')
                time.sleep(0.6)
            
            keyboard.press('right')
            time.sleep(0.4)
            keyboard.release('right')

            self.rope_Lift()

            for i in range(3):
                self.blade_Fury()

                keyboard.press('right')
                keyboard.send('space')
                time.sleep(0.05)
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                time.sleep(0.2)
                keyboard.send('space')
                time.sleep(0.2)
                
                if i == 0:
                    self.blade_Tornado()
                elif i == 1:
                    self.solar_Crest()
                elif i == 2:
                    time.sleep(0.7)
                    self.sudden_Raid()

                keyboard.send('space + v')
                keyboard.release('right')
                if i == 2:
                    time.sleep(0.1)
                else:
                    time.sleep(0.6)
    
    def script3(self):
        time.sleep(2)
        self.frenzy_Totem()
        time.sleep(1.5)
        for i in range(50):
            print('---------------第' + str(i + 1) + '輪---------------')
            for i in range(3):
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
                #self.blade_Fury()
                time.sleep(0.3)

            self.rope_Lift()

            for i in range(3):
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
                    self.solar_Crest()
                elif i == 2:
                    time.sleep(0.3)
                    self.sudden_Raid()

                keyboard.release('left')
                #self.blade_Fury()
                time.sleep(0.3)