import threading
import time

def print_numbers(n):
    for i in range(n):
        print(f"Thread {threading.current_thread().name}: {i}")
        time.sleep(0.5)

# Creating multiple threads with arguments
thread1 = threading.Thread(target=print_numbers, args=(5,))
thread2 = threading.Thread(target=print_numbers, args=(3,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads completed!")

# tagril-
# run 3 threads from 1-random(5-10), print the numbers + the thread-name
#   each time sleep(0.5)
#   join to wait for all threads
#   *bonus: create random threads 5-10 (list) and do the same + join