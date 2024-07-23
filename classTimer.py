import time
from typing import List
from abc import ABC, abstractmethod

class Timer(ABC):
    def __init__(self):
        self.Continue = False
        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.days = 0
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def end(self,save:bool=False):
        pass

class timerT1(Timer):
    def start(self):
        while True :
            if self.Continue == False:
                timerT1.end()
                break
            time.sleep(0.001)
            self.milliseconds += 1
            if self.milliseconds == 1000:
                if self.seconds == 60:
                    self.minutes += 1
                    if self.minutes == 60:
                        self.hours += 1
                        if self.hours == 24:
                            self.days += 1
                            self.hours = 0
                        self.minutes = 0
                    self.seconds = 0
                self.milliseconds = 0
    def stop(self):
        self.Continue = False
    def continuing(self):
        self.Continue = True
    def end(self,save:bool=False):
        if save == True:
            with open(f'recordsT1.txt', 'w+') as f:
                lines = f.readlines()
                lines.append(f'{self.days}days and {self.hours}hours {self.minutes}minutes {self.seconds}seconds {self.milliseconds}milliseconds')
                f.writelines(lines)

