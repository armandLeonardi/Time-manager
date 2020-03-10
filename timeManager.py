# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:47:25 2019

@author: Armand
"""

from time import time
from progressbar import printProgressBar
import json


class Timer:
    
    def __init__(self,title,time):
        self.title = title
        self.time = time * 60 # in seconds
        
    def __call__ (self):
        T0 = time()
        delta = time() - T0
        lenght = 50
        while delta < self.time:
            printProgressBar(delta,self.time,round((self.time - delta)/60,0),length = lenght)
            delta = time() - T0


class TimeManager:
    
    def __init__ (self):
        self.version = "1.0"
        self.timers = {"default":5}
        
    def uploadTimers(self):
        f = open("timers.json",'w')
        f.write(json.dumps(self.timers))
        #f.write("\""+str(self.timers)+"\"")
        f.close()
        
    def downloadTimers(self):
        f = open("timers.json",'r')
        self.timers = json.load(f)
        f.close()

        
    def create(self,title,time):
        self.timers[title] = time
        
    def __call__(self,title):
        time = self.timers[title]
        timer = Timer(title,time)
        timer()
        
           
if __name__ == "__main__":
    
    tm = TimeManager()
 
    tm.create("work",1)

    tm.uploadTimers()
        
    tm = None

    tm = TimeManager()

    tm.downloadTimers()
    
    tm("work")