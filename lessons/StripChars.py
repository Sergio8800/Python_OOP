class StripChars:
    def __init__(self, chars):
        self.__couter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("it is must be string!!!!")
        return args[0].strip(self.__chars)#удаляет в конце символы прописаные в значениях

k = StripChars("k:.,!")
t = "Hello,,!! k Workd! kks!,"
result = k(t)
print(t)
print(result)