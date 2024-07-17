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






h1 = House('SGR', 4)
h2 = House('SB', 13)

h1.go_to(3)
h1.go_to(5)
print()
h2.go_to(6)
h2.go_to(-1)