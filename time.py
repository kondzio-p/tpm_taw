import time

def measure_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution Time: ", execution_time)

def some_function():
    for _ in range (100000):
        pass

measure_time(some_function)

print("Siema chłopie, ")
time.sleep(3)
print("wstałeś już?")