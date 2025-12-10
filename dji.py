from djitellopy import Tello

import time
import asyncio

class DJI:
    
    def __init__(self):
        self.counter = 0
        self.tello = Tello()
        self.tello.connect()


    async def liftoff(self):
        self.tello.takeoff()
        await asyncio.sleep(5)
        self.tello.land()

    def increase_counter(self): 
        
        self.counter +=1

        if (self.counter % 25 == 0):
            self.liftoff()
            self.counter = 0
        return self.counter