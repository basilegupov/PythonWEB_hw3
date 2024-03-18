import time
from multiprocessing import Pool, cpu_count


def factorize(num):
    factors = [i for i in range(1, num+1) if num % i == 0]
    return factors


def factorize_sync(numbers):
    return [factorize(num) for num in numbers]


def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize, numbers)


a, b, c, d = factorize(128), factorize(255), factorize(99999), factorize(10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
             1521580, 2130212, 2662765, 5325530, 10651060]

start_time = time.time()
result_sync = factorize_sync([128, 255, 99999, 10651060])
print("Час виконання синхронної версії:", time.time() - start_time)

start_time = time.time()
result_parallel = factorize_parallel([128, 255, 99999, 10651060])
print("Час виконання паралельної версії:", time.time() - start_time)
