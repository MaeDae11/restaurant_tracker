# You'll write a program to help you track which restaurants near ATV you have gone to for lunch.

 

# Basic features:

# -##### Show a menu of three restaurants (for example: 1. chipotle, 2. farm burger, and 3. ru san's)
# -#### Keep track of the user's choice and print out a message that tells them what they chose.

# - Prompt the user to choose one (for example by typing the number 1 for chipotle).


# Intermediate features:

# # -##### Keep prompting them until they choose 0, or until they've finished 5 rounds.
# # -##### Keep track of the number of times they choose each restaurant.

# # - If they choose a single restuarant more than 3 times, make them choose another.



x = 0
y = 0
z = 0

def menu():
    menu_input = int(raw_input("\nWhat would you like to do today?" + "\n\t1. Main Menu" + "\n\t2. My Restaurant Spots" + "\n\t3. Quit\n"))
    if menu_input == 1:
        print "You are at the menu options.\n"
        menu()
    elif menu_input == 2:    
        print "You are going to My Restaurant Spots.\n"
        adding_restaurants_menu()
    elif menu_input == 3:
        print "You are about to quit the program. Are you sure?"
        quit_y_n = str.capitalize(raw_input("Y" + " " + "/" + " " + "N\n"))
        if quit_y_n == "Y":
            print "Quit"
        elif quit_y_n == "N":
            menu()

def choose_lunch():
    restaurant1 = "Chipotle"
    restaurant2 = "Farm Burger"
    restaurant3 = "Ru San's"
    return str.capitalize(raw_input("Today, did you have:\n%s\n%s\n%s?\n" % (restaurant1, restaurant2, restaurant3)))

  





def counter_chipotle(num):
    return num + 1   

def total_chipotle():
    number  = counter_chipotle()
    

def adding_restaurants_menu():
    answer = choose_lunch()
    chipotle_visits = 0
    if answer == "Chipotle":
        if chipotle_visits < 3:
            chipotle_visits = counter_chipotle(chipotle_visits)
            print "Today you chose %s." % answer
            print "You have eaten at %s %d times this week.\n " % (answer, chipotle_visits)
            # restaurants_menu()
        elif chipotle_visits == 3:
            counter_chipotle(chipotle_visits)
            print "You have eaten at %s %d times this week.\n " % (answer, chipotle_visits)
            print "You should really eat somewhere else.\n"
            # restaurants_menu()
        elif chipotle_visits == 4:
            print "Choose a different restaurant tomorrow.\n"
        elif chipotle_visits > 4:
            print "%s is no longer an option. " % answer


    # choose Farm Burger 
    elif answer == restaurant2:
        if y < 3:
            y = y + 1
            print "Today you chose %s." % restaurant2
            print "You have eaten at %s %d times this week. " % (restaurant2, y)
        elif y == 3: 
            y = y + 1
            print "You have eaten at %s %d times this week. " % (restaurant2, y)
            print "You should really eat somewhere else."
        elif y == 4:
            print "%s is no longer an option. " % restaurant2
    

    #  choose Ru San's  
    elif answer == restaurant3:
        if z < 3:
            z = z + 1
            print "Today you chose %s." % restaurant3
            print "You have eaten %s %d times this week. " % (restaurant3, z)
        elif z == 3:
            z = z + 1
            print "You have eaten %s %d times this week. " % (restaurant3, z)
            print "You should really eat somewhere else."
        elif z == 4:
            print "%s is no longer an option. " % restaurant3

menu()



          















# This is original addition of menu items that works
# def adding_restaurants_menu():  
#     while x <= 5 and y <= 5 and z <= 5:
#         answer = choose_lunch()
        
#         # Choose Chipotle
#         if answer == restaurant1:
#             if x < 3:
#                 x = x + 1
#                 print "Today you chose %s." % restaurant1
#                 print "You have eaten at %s %d times this week.\n " % (restaurant1, x)
#                 menu()
#             elif x == 3:
#                 x = x + 1
#                 print "You have eaten at %s %d times this week.\n " % (restaurant1, x)
#                 print "You should really eat somewhere else.\n"
#                 menu()
#             elif x == 4:
#                 print "Choose a different restaurant tomorrow.\n"
#             elif x > 4:
#                 print "%s is no longer an option. " % restaurant1


#         # choose Farm Burger 
#         elif answer == restaurant2:
#             if y < 3:
#                 y = y + 1
#                 print "Today you chose %s." % restaurant2
#                 print "You have eaten at %s %d times this week. " % (restaurant2, y)
#             elif y == 3: 
#                 y = y + 1
#                 print "You have eaten at %s %d times this week. " % (restaurant2, y)
#                 print "You should really eat somewhere else."
#             elif y == 4:
#                 print "%s is no longer an option. " % restaurant2
        

#         #  choose Ru San's  
#         elif answer == restaurant3:
#             if z < 3:
#                 z = z + 1
#                 print "Today you chose %s." % restaurant3
#                 print "You have eaten %s %d times this week. " % (restaurant3, z)
#             elif z == 3:
#                 z = z + 1
#                 print "You have eaten %s %d times this week. " % (restaurant3, z)
#                 print "You should really eat somewhere else."
#             elif z == 4:
#                 print "%s is no longer an option. " % restaurant3

# menu()



# # choose_lunch()

# if x == 5 or y == 5 or z == 5:            
    # print "\nYou should start making lunch at home.\n"




# def keep_track_of_restaurant_count():
#     i = i + 1
#     if i < 3:
#         print "Today you chose %s." % restaurant_name
#         print "You have eaten at %s %d times this week.\n " % (restaurant_name, i)
#         i = i + 1
#     elif i == 3:
#         print "You have eaten at %s %d times this week.\n " % restaurant_name
#         print "You should really eat somewhere else.\n"
#         i = i + 1
#     elif i == 4:
#         print "Choose a different restaurant tomorrow.\n"





#### extra menu that wasn't needed
# restaurant1, 2, 3 / answer / x, y, z
# def restaurants_menu():
#     print "You are in the Restaurants Menu.\n"
#     menu_input = int(raw_input("\nPlase choose an option:" + "\n1. Main Menu" + "\n2. Add Today's Lunch Spot" + "\n3. Quit\n"))
#     if menu_input == 1:
#         print "You are going back to the menu options.\n"
#         menu()
#     elif menu_input == 2:    
#         print "You are going to My Restaurant Spots.\n"
#         adding_restaurants_menu()
#     elif menu_input == 3:
#         print "You are about to quit the program. Are you sure?"
#         quit_y_n = str.capitalize(raw_input("Y" + " " + "/" + " " + "N\n"))
#         if quit_y_n == "Y":
#             print "Quit"
#         elif quit_y_n == "N":
#             menu()