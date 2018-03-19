class Animals():
    
    type = 'animal'
    name = ''
    ability_to_fly = False
    ability_to_swim = False
    voice = ''

    def __init__(self, name):
        
        self.name = name
        print('Создано: {}'.format(self.__str__()))

    def get_voice(self):
        
        if not self.voice:
            return
        print('{} издает звук "{}"'.format(self.name, self.voice))

    def __str__(self):
        
        return '{}: {}'.format(self.type, self.name)


class Birds(Animals):
    
    type = 'bird'
    ability_to_fly = True


class Mammals(Animals):
    
    type = 'mammal'


class Ducks(Birds):
    
    type = 'duck'
    ability_to_swim = True
    color = 'white'
    voice = 'кря'


class Gooses(Birds):
    
    type = 'goose'
    ability_to_swim = True
    color = 'white'
    voice = 'га-га'


class Chickens(Birds):
    
    type = 'chicken'
    color = 'brown'
    voice = 'кукареку'


class Cows(Mammals):
    
    type = 'cow'
    color = 'brown with white'
    voice = 'му-му'


class Goats(Mammals):
    
    type = 'goat'
    color = 'white'
    voice = 'ме-ме'



class Sheeps(Mammals):
    
    type = 'sheep'
    color = 'white'
    voice = 'бее'



class Pigs(Mammals):
    
    type = 'pig'
    color = 'pink'
    voice = 'хрю-хрю'
