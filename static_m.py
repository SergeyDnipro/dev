class mystaticmethod(object):

    def __init__(self, x):
        self.x = x

    def __get__(self, obj, ob=None):
        return self.x


class MyClass:
    num = 0

    def __init__(self):
        MyClass.num += 1

    def out(self):
        print(MyClass.num)

    @staticmethod
    def out_1():
        print(MyClass.num)

    @mystaticmethod
    def out_2():
        print(MyClass.num)


a = MyClass()


try:
    MyClass.out()
except TypeError:
    print('Type Error')

try:
    MyClass.out_1()
except TypeError:
    print('Type Error')

try:
    MyClass.out_2()
except TypeError:
    print('Type Error')
