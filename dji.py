class DJI:
    
    
    
    
    
    def __init__(self):
        self.counter = 0

    def increase_counter(self):
        self.counter +=1

        if (self.counter % 50 == 0):
            print("lift off")
            self.counter = 0
        return self.counter