# multipprocessing not give output when run in jupyter notebook

import multiprocessing
import time

def square():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Square : {i * i}")


def cube():
    for i in range(1, 6):
        time.sleep(1.5)
        print(f"Cube : {i * i * i}")

if __name__ == "__main__":
    t = time.time()
    p1 = multiprocessing.Process(target = square)
    p2 = multiprocessing.Process(target = cube)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    total_time = time.time() - t
    print(f"Finished Time : {total_time}")
