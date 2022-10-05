#Gillian Bedward
#Restaurant
#Inputs
another_search = 'yes'
while another_search == 'yes':
    vegetarian = False
    vegan = False
    gluten_free = False
    response = input("Is anyone in your party vegetarian? ").lower()
    if response == "Yes" or "yes":
        vegetarian = True
    response = input("Is anyone in your party vegan? ").lower()
    if response == "Yes" or "yes":
        vegan = True
    response = input("Is anyone in your party gluten free? ").lower()
    if response == "Yes" or "yes":
        gluten_free = True
    print("Here are your restaurant choices:")
    if vegetarian == True and vegan == True and gluten_free == True:
        print ("Joe's Gourmet Burgers")
    if vegan == True and gluten_free == True:
        print ("Mama's Fine Italian")
    if vegan == True:
        print ("Main Street Pizza")
        print ("Corner Cafe")
        print ("Chef's Kitchen")
    another_search = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end): ")

