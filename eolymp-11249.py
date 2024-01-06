import time, timeit


# def foo(var):
#     if var == 0:
#         return a
#     else:
#         return foo(var - 1) + b * var + c
#
#
# a, b, c, n = map(int, input().split())
#
# start_time = time.time()
# print(foo(n))
# print(time.time() - start_time)

def test1():
    d = [x for x in range(100000) if x % 2 == 0]


print(timeit.timeit(stmt=test1, number=10))
