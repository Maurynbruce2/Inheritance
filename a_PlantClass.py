
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant):
    #Flower is subclass to Plant 
    def __init__(self,color, petals):
        Plant.__init__(self,color)
        #1st thing we do is call init method of superclass

        self.__petals = petals

    def get_petals(self):
        return self.__petals
        #Petals is an attribute that only belongs to the Flowers subclass 
        #Petals only apply to Flower
