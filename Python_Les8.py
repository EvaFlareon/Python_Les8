class Farm:
    def __init__(self, name, size, paws, wings):
        self.name = name
        self.size = size
        self.paws = paws
        self.wings = wings

    def __str__(self):
        return str({
            'name': self.name,
            'size': self.size,
            'paws': self.paws,
            'wings': self.wings,
        })

    @staticmethod
    def feed():
        return 'Вы покормили обитателей фермы'

    @staticmethod
    def drink():
        return 'Вы напоили обитателей фермы'


class Animal(Farm):
    name_animal = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_animal):
        self.name_animal = name_animal
        Farm.__init__(self, name_animal, 'big', 4, 'None')

    @staticmethod
    def stab():
        return 'Вы зарубили животное на мясо'


class Birds(Farm):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        Farm.__init__(self, name_bird, 'small', 2, 'Yes')

    @staticmethod
    def pluck():
        return 'Вы ощипали птицу'


ducks = Birds('Утки')
chickens = Birds('Куры')
geese = Birds('Гуси')

cows = Animal('Коровы')
goats = Animal('Козы')
sheep = Animal('Овцы')
pigs = Animal('Свиньи')

print('Утки: {}'.format(ducks))
print('Коровы: {}'.format(cows))

print(chickens.feed())
print(goats.drink())
print(geese.pluck())
print(sheep.stab())
