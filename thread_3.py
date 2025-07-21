import threading
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    print(threading.current_thread().name, f"working on {n}")

# resource pool
with ThreadPoolExecutor(max_workers=3) as executor:
    numbers = [1, 2, 3, 4, 5]
    executor.map(task, numbers)

print("All tasks completed!")