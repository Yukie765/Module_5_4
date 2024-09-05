class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __init__(self, Name, Num_of_floors):
        self.name = Name
        self.num_of_floors = Num_of_floors

    def go_to(self, Floor):
        if Floor < 1 or Floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1,Floor+1):
                print(i)

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.num_of_floors == other.num_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors < other.num_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.num_of_floors <= other.num_of_floors

    def  __gt__(self, other):
        if isinstance(other, House):
            return self.num_of_floors > other.num_of_floors

    def  __ge__(self, other):
        if isinstance(other, House):
            return self.num_of_floors >= other.num_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.num_of_floors != other.num_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
