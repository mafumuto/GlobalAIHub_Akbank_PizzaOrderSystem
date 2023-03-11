"""
from main import *


class PizzaFactory:
    __pizza = None
    __extra = None


    def __init__(self, *args):
        print("İşlem devam ediyor")

    def get_cost(self):
        if self.__extra is None:
            return print(self.__pizza.get_cost())
        else:
            return print(self.__pizza.get_cost() + self.__extra.get_cost())

    @classmethod
    def get_only_pizza(cls, onlypizza: Pizza):
        cls.__pizza = onlypizza
        return cls(cls.__pizza)

    @classmethod
    def get_pizza(cls, basepizza: Pizza, extras: Ingredient):
        cls.pizza = basepizza
        cls.extra = extras
        return cls(cls.__pizza, cls.__extra)


asd = PizzaFactory.get_only_pizza(Classic())
asd.get_cost()
PizzaFactory(2)



class Choicee:

    @classmethod
    def pizza_choice(cls):
        cls.pizza_choice = None
        while True:
            try:
                choice = int(input("Lütfen seçmek istediğniz pizzanın numarasını giriniz. \n"))
                if choice in Pizzas.keys():
                    cls.pizza = PizzaFactory(Pizzas[choice])
                    return cls.pizza
                else:
                    print("Seçiminiz listede yoktur. Lütfen listede olan pizzanın numarasını tamsayı olarak giriniz.\n")
            except ValueError:
                print("Lütfen tamsayı bir değer(örneğin 1 gibi) giriniz. \n")

    @classmethod
    def extra_choice(cls):
        cls.extra_choices = []
        while True:
            try:
                cls.extra_choice = int(input("Lütfen seçmek istediğiniz sosun(ekstra malzeme) numarasını giriniz. İşlemi sonlandırmak için 0'ı girebilirsiniz.\n"))
                if cls.extra_choice == 0:
                    break
                elif cls.extra_choice in cls.extra_choices:
                    print("bu seçimi zaten yapmıştınız")
                elif cls.extra_choice in Ingredients.keys():
                    cls.extra_choices.append(cls.extra_choice)
                else:
                    print("Seçiminiz listede yoktur. Lütfen listede olan sosun numarasını tamsayı olarak giriniz.\n")

            except ValueError:
                print("Lütfen tamsayı bir değer(örneğin 1 gibi) giriniz. \n")
        return cls.extra_choices



    def pizza_choice():
        while True:
            try:
                choice = int(input("Lütfen seçmek istediğniz pizzanın numarasını giriniz. \n"))
                if choice in Pizzas.keys():
                    pizza = PizzaFactory(Pizzas[choice])
                    return pizza
                else:
                    print("Seçiminiz listede yoktur. Lütfen listede olan pizzanın numarasını tamsayı olarak giriniz.\n")
            except ValueError:
                print("Lütfen tamsayı bir değer(örneğin 1 gibi) giriniz. \n")


    def extra_choice():
        extra_choices = []
        while True:
            try:
                extra_choice = int(input("Lütfen seçmek istediğiniz sosun(ekstra malzeme) numarasını giriniz. İşlemi sonlandırmak için 0'ı girebilirsiniz.\n"))
                if extra_choice == 0:
                    break
                elif extra_choice in extra_choices:
                    print("bu seçimi zaten yapmıştınız")
                elif extra_choice in Ingredients.keys():
                    extra_choices.append(Ingredients[extra_choice])
                else:
                    print("Seçiminiz listede yoktur. Lütfen listede olan sosun numarasını tamsayı olarak giriniz.\n")

            except ValueError:
                print("Lütfen tamsayı bir değer(örneğin 1 gibi) giriniz. \n")
        return extra_choices


"""
