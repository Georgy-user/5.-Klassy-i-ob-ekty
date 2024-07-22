class House:
    houses_history = []  # Атрибут класса. Хранит названия созданных объектов.

    def __new__(cls, *args, **kwargs):
        # def add_history(cls, )
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor): # Метод выводит на экран номер этажа, на который надо приехать.
        if new_floor > 0 and new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует.')

    def __len__(self): # Метод возвращает количество этажей дома.
        return self.number_of_floors

    def __str__(self): # Метод возвращает название дома и количество этажей.
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}."

    def __eq__(self, other): # Возвращает True, если количество этажей одинаково.
        return self.number_of_floors == other.number_of_floors

    def __add__(self, dostroika):
        self.number_of_floors = self.number_of_floors + dostroika
        return House(self.name, self.number_of_floors)

    def __radd__(dostroyka, other):
        other.number_of_floors = other.number_of_floors + dostroyka
        return House(other.name, other.number_of_floors)

    def __iadd__(self, dostroika):
        self.number_of_floors += dostroika
        return House(self.name, self.number_of_floors)

    def __gt__(self, other): # Возвращает True, если количество этажей первого дома больше, чем второго.
        return self.number_of_floors > other.number_of_floors

    def __lt__(self, other): # Возвращает True, если количество этажей первого дома меньше, чем второго.
        return self.number_of_floors < other.number_of_floors

    def __ge__(self, other): # Возвращает True, если количество этажей первого дома больше или равно кол-ву этажей второго.
        return self.number_of_floors >= other.number_of_floors

    def __le__(self, other): # Возвращает True, если количество этажей первого дома меньше или равно кол-ву этажей второго.
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other): # Возвращает True, если количество этажей первого дома не равно кол-ву этажей второго.
        return self.number_of_floors != other.number_of_floors

    def __del__(self): # Переопред-е м-да del.
        print(f"{self.name} снесён, но он останется в истории.")



h1 = House('SGR', 4)
print(House.houses_history)
h2 = House('SB', 13)
print(House.houses_history)
h3 = House('PA', 5)
print(House.houses_history)
print()

# Удаление объектов.
del h2
del h3
print(House.houses_history)

