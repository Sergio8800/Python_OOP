class Validator:
    # def __init__(self, min_value, max_value):
    #     self.min_value = min_value
    #     self.max_value = max_value
    @classmethod
    def validator(cls, val):
        if type(val) !=int:
            raise TypeError("It is must be INTENGER")

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{value} меньше, чем {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} больше, чем {self.max_value}')
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        print("!")