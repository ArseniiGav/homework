class Animals():
    
    name = ''
    ability_to_fly = False
    ability_to_swim = False
    voice = ''

    def __init__(self, name='нет имени'):
        
        self.name = name
        print('Создано: {}'.format(self.__str__()))

    def get_voice(self):
        
        if not self.voice:
            return
        print('{} издает звук "{}"'.format(self.name, self.voice))

    def __str__(self):
        
        return '{}'.format(self.name)


class Birds(Animals):
    
    ability_to_fly = True


class Mammals(Animals):
    
    ability_to_swim = True

class Ducks(Birds):
    
    ability_to_swim = True
    color = 'white'
    voice = 'кря'


class Gooses(Birds):
    
    ability_to_swim = True
    color = 'white'
    voice = 'га-га'


class Chickens(Birds):
    
    color = 'brown'
    voice = 'кукареку'


class Cows(Mammals):
    
    color = 'brown with white'
    voice = 'му-му'


class Goats(Mammals):
    
    color = 'white'
    voice = 'ме-ме'



class Sheeps(Mammals):
    
    color = 'white'
    voice = 'бее'



class Pigs(Mammals):
    
    color = 'pink'
    voice = 'хрю-хрю'

animal_1 = Ducks('Дейзи')
animal_1.get_voice()
print(type(animal_1))

animal_2 = Gooses('Гога')
animal_2.get_voice()
print(type(animal_2))

animal_3 = Chickens('Цыпа')
animal_3.get_voice()
print(type(animal_3))

animal_4 = Cows('Мурка')
animal_4.get_voice()
print(type(animal_4))

animal_5 = Goats('Капра')
animal_5.get_voice()
print(type(animal_5))

animal_6 = Sheeps('Доли')
animal_6.get_voice()
print(type(animal_6))

animal_7 = Pigs('Пепа')
animal_7.get_voice()
print(type(animal_7))
