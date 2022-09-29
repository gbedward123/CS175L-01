#Gillian Bedward
#Restaurant
#Inputs
vegetarian = False
vegan = False
gluten_free = False
response = input("Is anyone in your party vegetarian? ").lower()
if response == "Yes" or response == "yes":
    vegetarian = True
response = input("Is anyone in your party vegan? ").lower()
if response == "Yes" or response == "yes":
    vegan = True
response = input("Is anyone in your party gluten free? ").lower()
if response == "Yes" or response == "yes":
    gluten_free = True
input("Here are your restaurant choices:")
if response == "(NOT vegetarian) AND (NOT vegan) AND (NOT gluten_free)":
    print ("Joe's Gourmet Burgers")
if response == "(NOT vegan) AND (NOT gluten_free)":
    print ("Mama's Fine Italian")
if response == "(NOT vegan)":
    print ("Main Street Pizza")
    print ("Corner Cafe")
    print ("Chef's Kitchen")
