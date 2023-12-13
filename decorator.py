# def f1():
#     def f2(data_1):
#         return str(data_1)
#     return f2
#
#
# func = f1()
# print(func)
# func(1)
# print(type(func(1)))
#
# func = f1()('120')
# print(func)

def convert_to_str(func):
    quantity = 10

    def convert(*args, **kwargs):
        if isinstance(func(*args, **kwargs), int):
            print(*kwargs.values())
            return str(func(*args, **kwargs))
        return '0'
    return convert


@convert_to_str
def int_val(value1: int, value2: int) -> int:
    return value1 * value2


res = int_val(value1=15, value2=3)
print(res)
print(type(res))
