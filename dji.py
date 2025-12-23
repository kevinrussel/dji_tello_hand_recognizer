from djitellopy import Tello
from djitellopy.tello import TelloException
import queue, threading

class DJI:
    def __init__(self):
        self.tello = Tello()
        self.tello.connect()

        self.stop_event = threading.Event()
        self.q = queue.Queue(maxsize=3)  

    def enqueue(self, item: str):
        """Non-blocking: drop if queue is full."""
        try:
            self.q.put_nowait(item)
        except queue.Full:
            pass

    def worker(self):
        while not self.stop_event.is_set():
            try:
                item = self.q.get(timeout=0.2)
            except queue.Empty:
                continue

            try:
                if item in ("takeoff"):
                    self.tello.takeoff()
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

            finally:
                self.q.task_done()
