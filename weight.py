weight = int(input("Enter your weight: ")) # user will input there weight
unit = input("(L)bs or (k)g: ") # the user will choose if they input their weight in kg or lbs

if unit.upper() == "L": # if the users input L it will convert weight into kg
   total = weight * 0.45
   print(f"your are {total} in kilo!")
elif unit.upper() == "K": # if the input K it will convert weight into lbs
    total = weight / 0.45
    print(f"your are {total} in pounds!")
    
     