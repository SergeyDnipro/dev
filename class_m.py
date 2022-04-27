class myclassmethod(object):

    def __init__(self, f):
        self.f = f

    def __get__(self, object, cls=None):
        if cls is None:
            cls = type(object)

        def new_f(*args):
            return self.f(cls, *args)
        return new_f


class A:

    def __init__(self, x):
        self.x = x

    @classmethod
    def b(cls, y):
        return cls(y)

    @myclassmethod
    def c(cls, z):
        return cls(z)


class B(A):
    pass


x_1 = B(2)

print(type(B.c(1)))
print(type(B.b(1)))
print(type(x_1))
