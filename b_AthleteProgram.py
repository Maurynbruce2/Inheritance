
import b_AthleteClass as ac

#Create instance of SuperClass
generic_athlete = ac.Athlete(6,220,0.2)

#Create instance from Football Player subclass 
quarterback = ac.Football_Player(6.2,250,0.15,'quarterback','offense')


print("The height for the generic athlete is:",generic_athlete.get_ht())

#print("The team of the generic athlete is:",generic_athlete.get_team())
    # Gives an error because the SuperClass cannot access attributes in the SubClass
print("The team of the generic athlete is:",quarterback.get_team())

print("The weight for the football player is:",quarterback.get_wt())

print("The position of the football player is:",quarterback.get_position())
