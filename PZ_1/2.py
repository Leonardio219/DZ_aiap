class List_manager:
    def __init__(self, size):
        self.size = size
        self.list = [0] * size
        self.write_count = 0
        self.read_count = 0

    def output(self):
        print(self.list)

    def get_write_count(self):
        return (self.write_count)

    def get_read_count(self):
        return (self.read_count)

    def __setitem__(self, index, value):
        if not(0 <= index <= self.size-1):
            print(f'{index} такого индекса нет')
            return None
        if not(-100 <= value <= 100):
            print(f'value элемента с индексом {index} выходит за пределы')
            return None
        self.write_count += 1
        self.list[index] = value

    def __getitem__(self, index):
        if not(0 <= index <= self.size-1):
            print(f'{index} такого индекса нет')
            return None
        self.read_count += 1
        return self.list[index]
    def input_item(self, item):
        if not(-100 <= item <= 100):
            print (f'итем {item} выходит за пределы')
            return None
        self.list.append(item)
        self.size += 1

    def sum(self, list_1, list_2):

        if len(list_1) > len(list_2):
            list_3 = [0] * len(list_1)
            for i in range(len(list_2), len(list_1)):
                list_2.append(0)
            for i in range(len(list_1)):
                list_3[i] = list_1[i] + list_2[i]
            return list_3
        else:
            list_3 = [0] * len(list_1)
            for i in range(len(list_1)):
                list_3[i] = list_1[i] + list_2[i]
            return list_3

    def minus(self, list_1, list_2):

        if len(list_1) > len(list_2):
            list_3 = [0] * len(list_1)
            for i in range(len(list_2), len(list_1)):
                list_2.append(0)
            for i in range(len(list_1)):
                list_3[i] = list_1[i] - list_2[i]
            return list_3
        else:
            list_3 = [0] * len(list_1)
            for i in range(len(list_1)):
                list_3[i] = list_1[i] - list_2[i]
            return list_3


    # Дальше идёт проверка всех методов

lm = List_manager(10)
lm[1] = 22
lm[0] = 13
lm[2] = 12
lm[3] = -101
lm[22] = 3
print (lm[2])
print (lm[25])
print(lm.get_read_count())
print(lm.get_write_count())
lm.output()
lm.input_item(75)
lm.output()
print(lm[10])
lm.input_item(-1203)
print(lm.sum([45, 45, 0, 1000, 100, 10, 1, 0, -1000], [1, 2, 3, 4, 5, 6, 7]))
print(lm.sum([45, 45, 0, 1000, 100,], [1, 2, 3, 4, 5, 6, 7]))
print(lm.sum(lm.list, [0, 3, 10]))
lm_1 = List_manager(3)
lm_1[0] = 35
lm_1[1] = -1
lm_1[2] = 2
lm_1.input_item(12)
lm_1.output()
print(lm.sum(lm_1.list, lm.list))

print(lm.minus([45, 45, 0, 1000, 100, 10, 1, 0, -1000], [1, 2, 3, 4, 5, 6, 7]))
print(lm.minus([45, 45, 0, 1000, 100,], [1, 2, 3, 4, 5, 6, 7]))
print(lm.minus(lm.list, [0, 3, 10]))
print(lm.minus(lm_1.list, lm.list))