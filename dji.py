from djitellopy import Tello

import time
import asyncio
import queue
global_queue = queue.Queue()

class DJI:
    
    def __init__(self):
        self.counter = 0
        self.tello = Tello()
        self.tello.connect()


    def worker(self):
        while True:
            item = global_queue.get()
            self.liftoff()


    def liftoff(self):
        self.tello.takeoff()
        self.tello.land()

    def increase_counter(self): 
        self.counter +=1
        if (self.counter % 25 == 0):
            self.counter = 0
            global_queue.put("liftoff")
        return self.counter