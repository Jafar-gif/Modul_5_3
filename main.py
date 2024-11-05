class House:
    def __init__(self,name,nomber_of_floors):
        self.name = name
        self.number_of_floors = nomber_of_floors

    def go_to(self,new_floor):
        if 1 < new_floor < self.number_of_floors:
            for i in range(1,new_floor + 1):
                print(i)
            else:
                print(' Такого этажа не сущетствует')
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название:{self.name}, kол-во этажей:{self.number_of_floors}'
    def __eq__(self, other):
        if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        else:
            return False
    def __lt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors < other.number_of_floors
        else:
            return NotImplemented
    def __le__(self, other):
        if isinstance(other,House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return NotImplemented
    def __gt__(self, other):
        if isinstance(other,House):
            return self.number_of_floors > other.number_of_floors
        else:
            return NotImplemented
    def __ge__(self, other):
        if isinstance(other,House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return NotImplemented
    def __ne__(self, other):
        if isinstance(other,House):
            return self.number_of_floors != other.number_of_floors
        else:
            return True
    def __add__(self, value):
        if isinstance(value,int):
            return House(self.name,self.number_of_floors + value)
        elif isinstance(value,House):
            return House(self.name,self.number_of_floors + value.number_of_floors)
        else:
            return NotImplemented
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)
h1 = House('Жк Эльбрус',10)
h2 = House('Жк Акация',20)

print(h1)
print(h2)

print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
