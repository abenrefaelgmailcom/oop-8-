# tagril-
# run 3 threads from 1-random(5-10), print the numbers + the thread-name
#   each time sleep(0.5)
#   join to wait for all threads
#   *bonus: create random threads 5-10 (list) and do the same + join


import threading
import time
import random

def print_random_numbers():
    for _ in range(random.randint(5, 10)):
        number = random.randint(1, 100)
        thread_name = threading.current_thread().name
        print(f"{thread_name} → {number}")
        time.sleep(0.5)

# מספר רנדומלי של חוטים
num_threads = random.randint(5, 10)
threads = []

for i in range(num_threads):
    t = threading.Thread(target=print_random_numbers, name=f"RandomThread-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"🔚 All {num_threads} random threads completed.")
