#Q1) Kate’s cat, Roary, loves catching moths. Write a program 
#that determines whether or not it is time for Roary catch moths.

moths_in_house = True
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not(moths_in_house) and not(mitch_is_home):
    print("No threats detected.")
elif moths_in_house and not(mitch_is_home):
    print("Meooooooooooooow! Hissssss!")
elif not(moths_in_house) and mitch_is_home:
    print("Climb on Mitch.")

moths_in_house = False
mitch_is_home = False

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not(moths_in_house) and not(mitch_is_home):
    print("No threats detected.")
elif moths_in_house and not(mitch_is_home):
    print("Meooooooooooooow! Hissssss!")
elif not(moths_in_house) and mitch_is_home:
    print("Climb on Mitch.")

moths_in_house = True
mitch_is_home = False

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not(moths_in_house) and not(mitch_is_home):
    print("No threats detected.")
elif moths_in_house and not(mitch_is_home):
    print("Meooooooooooooow! Hissssss!")
elif not(moths_in_house) and mitch_is_home:
    print("Climb on Mitch.")

moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not(moths_in_house) and not(mitch_is_home):
    print("No threats detected.")
elif moths_in_house and not(mitch_is_home):
    print("Meooooooooooooow! Hissssss!")
elif not(moths_in_house) and mitch_is_home:
    print("Climb on Mitch.")