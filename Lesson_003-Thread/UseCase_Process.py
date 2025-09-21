# Real World Implementatio using multi - Processing

import multiprocessing
import sys                        # sys to adjust system parameters or limit to find large no. factorial.
import math 
import time
from concurrent.futures import ProcessPoolExecutor

sys.set_int_max_str_digits(100000)

def compute_factorial(number):
    result = math.factorial(number)
    return (f"Factorial of {number} is : {result}")

if __name__ == "__main__":
    numbers = [6000, 7000, 8000]

    t = time.time()

    with ProcessPoolExecutor(max_workers=16) as executor:
        results = executor.map(compute_factorial, numbers)

    for result in results:
        print(result)

    print(f"Time taken: {time.time() - t} seconds")



'''
we can also use

with multiprocessing.Pool() as pool:            # By default, multiprocessing.Pool() sets processes = os.cpu_count() or number of logical CPU cores on your machine.
    results = pool.map(compute_factorial, numbers)     


'''