from __future__ import annotations
import pickle
import glob


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    number_of_cakes = 0
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, glutenFree, text):
        self.name = name

        # if element is on the list with known kinds
        if kind in Cake.known_types:
            self.kind = kind
        else:   # if not the kind is signed as other
            self.kind = 'other'

        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__glutenFree = glutenFree

        # Jeżeli element jest tortem to możemy na nim zrobic napis
        if self.kind == 'cake':
            self.__text = text
        else:
            self.__text = ''

        Cake.number_of_cakes += 1
        self.bakery_offer.append(self)

    def show_info(self):
        print("----- {} -----".format(self.name.upper()))
        print("Kind:\t\t{}".format(self.kind))
        print("Taste:\t\t{}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t* {}".format(a))
        if len(self.filling) > 0:
            print("Filling:\t{}".format(self.filling))
        print('Is gluten free: {}'.format(self.__glutenFree))
        if len(self.__text) > 0:
            print('Text:\t\t{}'.format(self.__text))

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __iadd__(self, other):
        if type(other) is list:
            for ele in other:
                if ele not in self.additives:
                    self.additives.append(other)
            return self

        if type(other) is str:
            if other in self.additives:
                self.additives.append(other)
            return self
        else:
            raise Exception('Adding type {} to Cake is not implemented'.format(type(other)))

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

    def save_to_file(self, path):
        with open(path, 'bw') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'br') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        print(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(path + '/*.bakery')


class NoDuplicates:
    def __init__(self, function):
        self.function = function

    def __call__(self, cake: Cake, additives):
        no_duplicate_list = [a for a in additives if a not in cake.additives]
        # function call finds arguments for which it will be working
        self.function(cake, no_duplicate_list)


@ NoDuplicates
def add_extra_additives(cake: Cake, additives):
    cake.add_additives(additives)


if __name__ == "__main__":
    birthday_cake = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', 'free', 'loveYou')
    birthday_cake += 'milk'
    birthday_cake += 'milk'
    add_extra_additives(birthday_cake, ['chocolate', 'apple'])

    birthday_cake.show_info()

#birthday_cake.save_to_file('./birthday_cake.bakery')
#print(Cake.get_bakery_files('./'))
