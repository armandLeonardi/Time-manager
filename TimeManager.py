# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:47:25 2019

@author: Armand
"""
from winsound import Beep
from time import time,sleep
import json
import getopt
import sys
from os import system

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

class Timer:
    
    def __init__(self,title,time):
        self.__version__ = "1.1.0"
        self.title = title
        self.time = time * 60 # in seconds
        self.default_step = 10 # seconds spreads between updating

        self.freq = 700 # frequence of beep 
        self.duration = 500 # miliseconds
        self.timePause = 1.5 # seconds
        
    def __call__ (self):
        T0 = time()
        delta = time() - T0
        lenght = 50
        while delta < self.time:
            printProgressBar(delta,self.time,round((self.time - delta)/60,0),length = lenght)
            delta = time() - T0
            sleep(self.default_step)

        printProgressBar(self.time,self.time,0,length = lenght)

        for _ in range(3):

            for _ in range(3):
                Beep(self.freq,self.duration)

            sleep(self.timePause)

        return "Timer finish"


class TimeManager:
    
    def __init__ (self):
        self.__version__ = "1.0.0"
        self.timers = {"default":5}
        self.download()
        
    def upload(self):
        f = open("timers.json",'w')
        f.write(json.dumps(self.timers))
        #f.write("\""+str(self.timers)+"\"")
        f.close()
        
    def download(self):
        f = open("timers.json",'r')
        self.timers = json.load(f)
        f.close()
    
        
    def create(self,title,time):
        self.timers[title] = time
        
    def delete(self,title):
        self.timers.pop(title)
    
    def __call__(self,title="default"):
        time = self.timers[title]
        timer = Timer(title,time)
        print(timer())
        
           
if __name__ == "__main__":
    
    print("##### TIME MANAGER ####")
    
    tm = TimeManager()
    action = ""
    
    actions = ["quit","timers","new","delete","upload","download"]

    while action != "quit":
        action = input("-> ")
        
        if action not in actions and  action not in tm.timers.keys():
            print("Input command is false : %s\nIt may be like %s"%(action,actions))
            continue
        
        if action == "timers":
            
            print(tm.timers)
            continue
        
        if action in tm.timers.keys():
            system('cls')
            tm(action)
            continue
            
        if action == "new":
            _title = input("timer title : ")
            _time = int(input("time :"))
            tm.create(_title,_time)
            tm.upload()
            continue
            
        if action == "delete":
            _title = input("timer title : ")
            tm.delete(_title)
            tm.upload()
            continue
        
        if action == "upload":
            tm.upload()
            continue
        
        if action == "download":
            tm.download()
            continue
        
    print("##### CLOSE TIME MANAGER ####")
    exit(0)

