from concurrent.futures import ProcessPoolExecutor
import time

def print_num(num):
    time.sleep(2)
    return num

t = time.time()
num = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers = 5) as executor:
        results = executor.map(print_num, num)

    for result in results:
        print(result)

    print("Finished Time : ", time.time() - t)