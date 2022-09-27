
class Athlete:
    #SuperClass 

    def __init__(self,ht,wt,bodyfat):
        self.__ht = ht
        self.__wt = wt
        self.__bf = bodyfat

    def get_ht(self):
        return self.__ht

    def get_wt(self):
        return self.__wt

    def get_bf(self):
        return self.__bf



class Football_Player(Athlete):
    # Athlete in () because we are inheriting from SuperClass
    # Use subclass for attributes specific to only Football Players

    def __init__(self,ht,wt,bodyfat,position,team):

        Athlete.__init__(self,ht,wt,bodyfat)

        self.__position = position
        self.__team = team
        #Attributes only required in subclass 

    # Return the attributes 
    
    def get_position(self):
        return self.__position

    def get_team(self):
        return self.__team










    
