class animals(object):
    mood = 50 # %
    health = 100 # %
    satiety = 50 # %
    ability_to_breath = True
    color = None
    years_of_life = 0
    size = 0 # meters**3
    ability_to_swim = True
    ability_to_fly = True
    number_of_legs = 0
    number_of_animals_on_ferm = 0
    def pat(self, mood):
        mood += 5
        if mood > 100:
            mood = 100
        return mood
    def feed(self, mood, satiety):
        mood += 5
        if mood > 100:
            mood = 100
        satiety += 3
        if satiety > 100:
            satiety = 100
        return mood, satiety 
    def kick(self, mood, health):
        mood -= 10
        if mood < 0:
            mood = 0
        health -= 8
        if health < 0:
            health = 0
        return mood, health

class cows(animals):
    def milk_a_cow(self, milk):
        milk += 5 # litres
        return milk
    def voice(self):
        return "Мууу"
    

class goats(animals):
    def milk_a_goat(self, milk):
        milk += 3 # litres
        return milk

class sheeps(animals):
    def shave_sheep(self, wool):
        wool += 5 # kg
        return wool

class pigs(animals):
    def slaughter(self, meat):
        meat += 20 #kg
        return meat
    
class ducks(animals):
     def slaughter(self, meat):
        meat += 2 #kg
        return meat

class chicken(animals):
    def get_eggs(self, egg):
        egg += 1 
        return egg

class gooses(animals):
    def slaughter(self, meat):
        meat += 3 #kg
        return meat