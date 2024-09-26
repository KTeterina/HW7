birds = ["dove", "owl", "eagle"]
type(birds)

birds.append("wolf") #add a new element
print(birds)

for bird in birds:
    if bird == "dove":
        print("there is a dove")
    if bird == "wolf":
        print("wolf isn't a bird, remove it")

birds.remove("wolf")
print(birds)