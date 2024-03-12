from datetime import datetime


class MyStr(str):
    def __new__(cls, value: str, autor: str):
        my_str_new = super().__new__(cls)
        my_str_new.value = value
        my_str_new.autor = autor
        my_str_new.time = datetime.now()
        return my_str_new

    # def __init__(self):
    #     self.value = value
    #     self.autor = autor

    def __str__(self):
        return f'--{self.value}-- autor: {self.autor}, time - {self.time}'

    def __repr__(self):
        return f'{MyStr.__str__(self)}, {self.autor}'


a = MyStr("dddssadfae", "Anton")
print(a)
