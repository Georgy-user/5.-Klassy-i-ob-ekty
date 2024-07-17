class House:
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
        nm = self.name
        nf = self.number_of_floors
        return f"Название: {nm}, кол-во этажей: {nf}."


h1 = House('SGR', 4)
h2 = House('SB', 13)

print(str(h1))
print(str(h2))
print()
print(h1)
print(h2)
print()
print(len(h1))
print(len(h2))