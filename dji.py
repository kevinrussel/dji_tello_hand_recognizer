from djitellopy import Tello

import queue
global_queue = queue.Queue()

class DJI:
    
    def __init__(self):
        self.counter = 0
        self.right_counter = 0
        self.left_counter = 0
        self.tello = Tello()
        self.tello.connect()


    def worker(self):
        while True:
            item = global_queue.get()
            if item == "liftoff":
                self.liftoff()  
            elif item == "right":
                self.move_right(20)
            elif item == "left":
                self.move_left(20)
            elif item == "land":
                self.land()


    def land_drone(self):
        global_queue.put("land")

    def move(self, direction):
        if direction == "right":
            self.right_counter += 1
            if(self.right_counter % 10 == 0):
                global_queue.put(direction)
                self.right_counter = 0
        else:
            self.left_counter += 1
            if(self.left_counter % 10 == 0):
                global_queue.put(direction)
                self.left_counter = 0

    def liftoff(self):
        self.tello.takeoff()
        self.tello.land()

    def takeoff_initiation(self): 
        self.counter +=1
        if (self.counter % 50 == 0):
            self.counter = 0
            global_queue.put("liftoff")
        return self.counter