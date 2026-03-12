pet_species = "dog"

age = 10

if pet_species == "dog":
    if age < 2:
        food = "puppy food"
    else:
        food = "senior food"

if pet_species == "cat":
    if age <5:
        food = "kitty food"
    else:
        food = "senior cat food"


print (food, "is recommanded")