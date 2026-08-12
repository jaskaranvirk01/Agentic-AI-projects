import threading
import time


class RateLimiter:
    def __init__(self, requests_per_second: float):
        self.interval = 1.0 / requests_per_second
        self.lock = threading.Lock()
        self.last_request_time = 0.0

    def acquire(self):
        with self.lock:
            now = time.monotonic()
            elapsed = now - self.last_request_time

            if elapsed < self.interval:
                wiat_time = self.interval - elapsed
                time.sleep(wiat_time)

            self.last_request_time = time.monotonic()
