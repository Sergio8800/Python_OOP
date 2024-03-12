import math

class Derivative:

    def __init__(self, func):
        self.__func = func

    def __call__(self, x, dx= 0.00001, *args, **kwargs):
        return (self.__func(x+dx) - self.__func(x))/dx

@Derivative
def df_sin(x):
    return math.sin(x)

# df_sin = Derivative(df_sin)
print(df_sin(math.pi/3))
print(df_sin(math.pi/3))
