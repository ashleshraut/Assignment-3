import threading

shared_counter = 0
ITERATIONS = 100000

def unsynchronized_worker():
    global shared_counter
    for _ in range(ITERATIONS):
        # Read and write explicitly separated to induce race condition
        val = shared_counter
        val += 1
        shared_counter = val

def synchronized_worker(lock):
    global shared_counter
    for _ in range(ITERATIONS):
        with lock:
            val = shared_counter
            val += 1
            shared_counter = val

def run_demo():
    global shared_counter
    
    # 1. Unsynchronized Run
    shared_counter = 0
    t1 = threading.Thread(target=unsynchronized_worker)
    t2 = threading.Thread(target=unsynchronized_worker)
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"Unsynchronized Final Counter: {shared_counter} (Expected: {2 * ITERATIONS})")
    
    # 2. Synchronized Run
    shared_counter = 0
    lock = threading.Lock()
    t3 = threading.Thread(target=synchronized_worker, args=(lock,))
    t4 = threading.Thread(target=synchronized_worker, args=(lock,))
    t3.start(); t4.start()
    t3.join(); t4.join()
    print(f"Synchronized Final Counter:   {shared_counter} (Expected: {2 * ITERATIONS})")

if __name__ == "__main__":
    run_demo()
