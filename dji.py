from djitellopy import Tello
from djitellopy.tello import TelloException
import queue, threading, time

class DJI:
    def __init__(self):
        self.tello = Tello()
        self.tello.connect()
        self.stop_event = threading.Event()

    def worker(self, q: queue.Queue):
        while not self.stop_event.is_set():
            try:
                item = q.get(timeout=0.2)
            except queue.Empty:
                continue

            try:
                if item == "liftoff":
                    self.liftoff()
                elif item == "right":
                    self.tello.move_right(20)
                elif item == "left":
                    self.tello.move_left(20)
                elif item == "land":
                    self.tello.land()
                elif item == "STOP":
                    self.stop_event.set()

            except TelloException as e:
                print(f"[DRONE CMD FAILED] {item} -> {e}")
                # keep worker alive

            finally:
                q.task_done()
