import a_PlantClass as pc

primrose = pc.Plant("Green")

#sunflower = pc.Flower("Yellow")
#This would give an error because you need the # of petals since you are accessing the subclass

sunflower = pc.Flower("Yellow",20)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


#print(primrose.get_petals())
# This would give an error since primrose is in the superclass and the get_petals
# method is only apart of the subclass 
