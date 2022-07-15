import time


def fibonachi_recursion(n):  # Рекуррентное решение, используя метод Фибоначчи, заранее известно решение для лестницы из трех ступеней
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n <= 2:
        return n
    return fibonachi_recursion(n - 1) + fibonachi_recursion(n - 2) + fibonachi_recursion(n - 3)


# Самое быстрое решение, создается список, значения в котором являются суммой трех предыдущих значений
def fibonachi_list(n):
    lst = [0 for x in range(n + 1)]
    lst[0] = 1
    lst[1] = 2
    lst[2] = 4
    for i in range(3, n):
        lst[i] = lst[i-1] + lst[i-2] + lst[i-3]
    return lst[n-1]


# Рекурсивное решение для каждого шага (1, 2 или 3)
def count_stairs(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 0
    for i in range(1, 4):
        result += count_stairs(n-i)
    return result


# Создал список, в котором прописываются решения для каждой ступени. Дубликаты не просчитываються заново.
def count_stairs_optimized(n, solution_list):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if solution_list[n] == 0:
        for i in range(1, number_of_steps + 1):
            solution_list[n] += count_stairs_optimized(n - i, solution_list)
    return solution_list[n]


number_of_steps = 3
number_of_stairs = 25
solution_list = [0 for x in range(number_of_stairs + 1)]

t1 = time.monotonic()
print(fibonachi_recursion(25))
print(time.monotonic() - t1)

t2 = time.monotonic()
print(fibonachi_list(25))
print(time.monotonic() - t2)

t3 = time.monotonic()
print(count_stairs(25))
print(time.monotonic() - t3)

t4 = time.monotonic()
print(count_stairs_optimized(number_of_stairs, solution_list))
print(time.monotonic() - t4)
