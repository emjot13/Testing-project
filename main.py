# class E_gradebook:
#     def __init__(self):
#         self.students = []
#         self.index = 0

import timeit
def is_prime(num):
    is_prime = True
    for k in range(2, int(num**0.5)):
        if num%k == 0:
            is_prime = False
    return is_prime

def is_prime_no_squrting(num):
    is_prime = True
    for k in range(2, num):
        if num%k == 0:
            is_prime = False
    return is_prime

import time

start = time.time()
is_prime(700544135864171)
end = time.time()
time2 = end - start
print(time2)

start1 = time.time()
is_prime_no_squrting(700544135864171)
end1 = time.time()
time1 = end1 - start1
print(time1)
print(time1/time2)