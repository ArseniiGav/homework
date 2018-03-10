class Animals():

    def __init__(self, kind, animal_class, animal_type, family, color):
        self.kind = kind
        self.animal_class = animal_class
        self.animal_type = animal_type
        self.family = family
        self.color = color


class Birds(Animals):

    def __init__(self, kind, animal_class,
                 animal_type, family, wings, paws, color):
        self.wings = wings
        self.paws = paws
        super().__init__(kind, animal_class, animal_type, family, color)


class Mammals(Animals):

    def __init__(self, kind, animal_class, animal_type,
                 family, horns, hoofs, color):
        self.hoofs = hoofs
        self.horns = horns
        super().__init__(kind, animal_class, animal_type, family, color)


class Ducks(Birds):

    def __str__(self):
        return str('Вид животного: {}; \nКласс: {}; \nТип: {};\
                   \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}\
                   \nЦвет: {}'.format(self.kind, self.animal_class,
                   self.animal_type, self.family, self.wings, self.paws,
                   self.color))

    def give_feathers(self, feathers):
        print('Эта {} даёт в среднем {} гр пуха.'
              .format(self.kind, feathers))


class Gooses(Birds):

    def __str__(self):
        return str('Вид животного: {}; \nКласс: {}; \nТип: {};\
                   \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}\
                   \nЦвет: {}'.format(self.kind, self.animal_class,
                   self.animal_type, self.family, self.wings, self.paws,
                   self.color))

    def give_feathers(self, feathers):
        print('Эта {} даёт в среднем {} гр пуха'
              .format(self.kind, feathers))


class Chickens(Birds):

    def __str__(self):
        return str('Вид животного: {}; \nКласс: {}; \nТип: {};\
                   \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}\
                   \nЦвет: {}'.format(self.kind, self.animal_class,
                   self.animal_type, self.family, self.wings, self.paws,
                   self.color))

    def give_feathers(self, feathers):
        print('Эта {} даёт в среднем {} гр пуха.'
              .format(self.kind, feathers))

    def give_eggs_to_day(self, eggs):
        if eggs > 0:
            print('Это курица дает яйца в количестве: {} штук в день'
                  .format(eggs))
        else:
            print('Эта курица еще не дает яиц')


class Cows(Mammals):

    def __str__(self):
        return str('Вид животного: {}; \nКласс: {}; \nТип: {};\
                   \nСемейство: {}; \nКол-во рогов: {}; \nКол-во копыт: {}.\
                   \nЦвет: {}'.format(self.kind, self.animal_class,
                   self.animal_type, self.family, self.horns, self.hoofs,
                   self.color))

    def give_milk(self, milk):
        if milk is False:
            print('{} не даёт молока.'.format(self.kind, milk))
        else:
            print('{} даёт в среднем {} литров молока в месяц.'
                  .format(self.kind, milk))


class Goats(Mammals):

    def __str__(self):
        return str('Вид животного: {}; \nКласс: {}; \nТип: {};\
                   \nСемейство: {}; \nКол-во рогов: {}; \nКол-во копыт: {}.\
                   \nЦвет: {}'.format(self.kind, self.animal_class,
                   self.animal_type, self.family, self.horns, self.hoofs,
                   self.color))

    def give_milk(self, milk):
        if milk is False:
            print('{} не даёт молока.'.format(kind, milk))
        else:
            print('{} даёт в среднем {} литров молока в месяц.'
                  .format(self.kind, milk))

    def give_wool(self, wool):
        print('{} дает {} гр шерсти в год.'
              .format(self.kind, wool))


class Sheeps(Mammals):

    def __str__(self):
        return str('Вид животного: {}; \nКласс: {}; \nТип: {};\
                   \nСемейство: {}; \nКол-во рогов: {}; \nКол-во копыт: {}.\
                   \nЦвет: {}'.format(self.kind, self.animal_class,
                   self.animal_type, self.family, self.horns, self.hoofs,
                   self.color))

    def give_milk(self, milk):
        if milk is False:
            print('{} не даёт молока.'.format(self.kind, milk))
        else:
            print('{} даёт в среднем {} литров молока в месяц.'
                  .format(self.kind, milk))


class Pigs(Mammals):

    def __str__(self):
        return str('Вид животного: {}; \nКласс: {}; \nТип: {};\
                   \nСемейство: {}; \nКол-во рогов: {}; \nКол-во копыт: {}.\
                   \nЦвет: {}'.format(self.kind, self.animal_class,
                   self.animal_type, self.family, self.horns, self.hoofs,
                   self.color))

    def give_milk(self, milk):
        if milk is False:
            print('{} не даёт молока.'.format(self.kind, milk))
        else:
            print('{} даёт в среднем {} литров молока в месяц.'
                  .format(self.kind, milk))


duck = Ducks('Утка', 'Птицы', 'Хордовые', 'Утинных',
             2, 'Перепончатые', 'Белый')
print(duck)

goose = Gooses('Гусь', 'Птицы', 'Хордовые', 'Утинных гусеобразных',
               2, 'Перепончатые', 'Белый')
print('\n', goose)

chicken = Chickens('Курица', 'Птицы', 'Хордовые',
                   'Фазановых', 2, 'Без перепонок', 'Белый')
print('\n', chicken)

cow = Cows('Корова', 'Млекопитающие', 'Хордовые', 'Жвачные парнокопытные',
           2, 4, 'Пятнистый белый с коричневым')
print('\n', cow)

goat = Goats('Коза', 'Млекопитающие', 'Хордовые', 'Полорогие',
             2, 4, 'Коричневый')
print('\n', goat)

sheep = Sheeps('Овца', 'Млекопитающие', 'Хордовые', 'Полорогие', 2, 4, 'Белый')
print('\n', sheep)

pig = Pigs('Свинья', 'Млекопитающие', 'Хордовые',
           'Нежвачные парнокопытные', 0, 4, 'Серый')
print('\n', pig)
