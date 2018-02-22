class animals:

    flight_altitude = 0
    position = 0
    ability_to_breath = None
    color = None
    size = 0  # meters**3
    ability_to_swim = None
    ability_to_fly = None
    hoof = None

    def voice(self, voice):
        return voice

    def fly(self, flight_altitude):
        flight_altitude += 2  # meters
        return flight_altitude

    def run(self, position):
        position += 3  # meters
        return position


class mammals(animals):

    number_of_hoof = 0
    position = 0

    def run(self, position):
        position += 3  # meters
        return position

    def milk_a_goat(self, goats_milk):
        goats_milk += 3  # litres

        return goats_milk

    def milk_a_cow(self, cows_milk):
        cows_milk += 5  # litres
        return cows_milk

    def slaughter_a_pig(self, meat):
        meat += 20  # kg
        return meat

    def shave_sheep(self, wool):
        wool += 5  # kg
        return wool


class birds(animals):

    beak = None
    number_of_wings = 0
    feathers = None

    def get_eggs(self, eggs):
        eggs += 3
        return eggs
