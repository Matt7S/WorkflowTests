from cake import Cake

class SpecialCake(Cake):
    def __init__(self, name, kind, taste, additives, filling, glutenFree, text, occasion, shape, ornaments):
        super().__init__(name, kind, taste, additives, filling, glutenFree, text)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments

    def show_info(self):
        super().show_info()
        print("Ocassion:\t{}".format(self.occasion))
        print("Shape:\t\t{}".format(self.shape))
        print("Ornaments:\t{}".format(self.ornaments))

    def add_additives(self, additives):
        return super().add_additives(additives)
    
    def __iadd__(self, other):
        if type(other) is list:
            self.additives.extend(other)
            return self
        if type(other) is str:
            self.additives.append(other)
            return self
        else:
            raise Exception('Adding type {} to Cake is not implemented'.format(type(other)))
        


if __name__ == "__main__":
    birthday_cake = SpecialCake('Vanilla Cake','cake', 'vanilla', ['chocolate', 'nuts'], 'cream', 'free', 'loveYou', 'birthday', 'square', '')

    birthday_cake.show_info()

    birthday_cake.save_to_file('/special_birthday_cake.bakery')

    print(Cake.get_bakery_files(''))
    