import threading
import time
import random

def print_random_numbers():
    for _ in range(random.randint(5, 10)):
        number = random.randint(1, 100)
        thread_name = threading.current_thread().name
        print(f"{thread_name} → {number}")
        time.sleep(0.5)

# create 3 threads
threads = []
for i in range(3):
    t = threading.Thread(target=print_random_numbers, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()

# join -wait until all the threads ends
for t in threads:
    t.join()

print("🔚 All 3 threads completed.")



# bonus

import threading
import time
import random

def print_random_numbers():
    for _ in range(random.randint(5, 10)):
        number = random.randint(1, 100)
        thread_name = threading.current_thread().name
        print(f"{thread_name} → {number}")
        time.sleep(0.5)

# random numbers of threads
num_threads = random.randint(5, 10)
threads = []

for i in range(num_threads):
    t = threading.Thread(target=print_random_numbers, name=f"RandomThread-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"🔚 All {num_threads} random threads completed.")
