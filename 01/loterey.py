class LotteryGame:
    def __init__(self, list1: list, list2: list):
        self.list1 = list1
        self.list2 = list2
    def compare_lists(self):
        res = list(set(list1) & set(list2))
        sum_res = len(res)
        return f'Совпадающие числа: {res}\nКоличество совпадающих чисел: {sum_res}'


    def compare_lists2(self):
        res = []
        for i in list1:
            if i in list2:
                res.append(i)
        return print(sorted(res))



list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
print(sorted(list1))
print(sorted(list2))

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
matching_numbersf2 = game.compare_lists2()
print(matching_numbers)


