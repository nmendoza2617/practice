"""
DESCRIPTION:
Culver’s is a fast-food restaurant which lets customers build their own
burger. In this program users will build a burger (specifically the
ButterBurger Cheese) and then output the total cost of the burger including
sales tax. Additionally, after the user builds their burger there will be a
trivia game about Culver’s.
"""

# Natalie Mendoza

__author__ = "Natalie Mendoza"


def trivia_game():
    """
    trivia_game() has the trivia game questions about Culver's
    """
    print("-----------------------------------------------------------------")
    print("\nCulver's trivia game!\n")

    # Below are the directions to the trivia game
    print("When selecting your answer choice only input a lower case 'a',"
          " 'b', or 'c'.\n")

    # The structure for trivia_game() is very similar to build_burger(). When
    # the user selects an answer the only valid answers are 'a', 'b', or 'c'.
    # I made question_z_validation = True, and it would become False when a
    # valid answer is entered. If an invalid answer is entered the while
    # loop will keep question_z_validation equal to True, and it will ask the
    # user to try again.

    # QUESTION 1
    question_1_validation = True
    while question_1_validation:
        question_1 = input("1. What year was the first Culver's opened?\n"
                           "a. 1998\n"
                           "b. 1984\n"
                           "c. 2001\n"
                           "your answer: ")
        if question_1 == 'b':
            print("Correct!\n")
            question_1_validation = False  # loop stops if user inputs 'b'
        elif question_1 == 'a':
            print("Incorrect, it was 1984\n")
            question_1_validation = False  # loop stops if user inputs 'a'
        elif question_1 == 'c':
            print("Incorrect, it was 1984\n")
            question_1_validation = False  # loop stops if user inputs 'c'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input lower case 'a', 'b' or 'c'. Try again.\n")
    # QUESTION 2
    question_2_validation = True
    while question_2_validation:
        question_2 = input("2. In which state was the first Culver's opened?\n"
                           "a. Wisconsin\n"
                           "b. Utah\n"
                           "c. Florida\n"
                           "your answer: ")
        if question_2 == 'a':
            print("Correct!\n")
            question_2_validation = False  # loop stops if user inputs 'a'
        elif question_2 == 'b':
            print("Incorrect, it's Wisconsin\n")
            question_2_validation = False  # loop stops if user inputs 'b'
        elif question_2 == 'c':
            print("Incorrect, it's Wisconsin\n")
            question_2_validation = False  # loop stops if user inputs 'c'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input lower case 'a', 'b' or 'c'. Try again.\n")

    # QUESTION 3
    question_3_validation = True
    while question_3_validation:
        question_3 = input("3. How many locations are open in Florida?\n"
                           "a. 70\n"
                           "b. 58\n"
                           "c. 75\n"
                           "your answer: ")
        if question_3 == 'c':
            print("Correct!\n")
            question_3_validation = False  # loop stops if user inputs 'c'
        elif question_3 == 'a':
            print("Incorrect, there are 75 locations in Florida\n")
            question_3_validation = False  # loop stops if user inputs 'a'
        elif question_3 == 'b':
            print("Incorrect, there are 75 locations in Florida\n")
            question_3_validation = False  # loop stops if user inputs 'b'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input lower case 'a', 'b' or 'c'. Try again.\n")

    # QUESTION 4
    question_4_validation = True
    while question_4_validation:
        question_4 = input("4. How many locations are open in the United "
                           "States?\n"
                           "a. 502\n"
                           "b. 850\n"
                           "c. 1205\n"
                           "your answer: ")
        if question_4 == 'b':
            print("Correct!\n")
            question_4_validation = False  # loop stops if user inputs 'b'
        elif question_4 == 'a':
            print("Incorrect, there are 850 locations in the United States\n")
            question_4_validation = False  # loop stops if user inputs 'a'
        elif question_4 == 'c':
            print("Incorrect, there are 850 locations in the United States\n")
            question_4_validation = False  # loop stops if user inputs 'c'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input lower case 'a', 'b' or 'c'. Try again.\n")

    print("Thank you")


def build_burger():
    """
    build_burger() contains all the ingredients the user can select from to
    build their burger. After the user is finished building their burger
    their total cost will be printed.
    """

    # INTRODUCTION
    # This is informing the user that they will be building a burger.
    print("\nBuild a burger!\nPlease follow the directions when selecting the"
          " meat, bun, cheese, and toppings.\nNote: This is specifically for"
          " the ButterBurger Cheese.\n")

    # "cost" is an accumulator, the default cost is 00.00 and will increase
    # or decrease depending on what ingredients the user selects.
    cost = 0.00

    # When the users select their ingredients they will need to input certain
    # answers like '1', '2', '3', 'y', or 'n' depending on the ingredient.
    # I used a while loop to continue to ask the user for a valid answer if
    # they input an invalid answer. I did this by making z_validation = True
    # (z varies in names throughout the program). z_validation will stay True
    # if an invalid answer is inputted and while it's True the program will
    # ask the user for a valid answer until an appropriate answer in entered.
    # When a valid answer is entered z_validation will become False stopping
    # the loop and continuing through the program.

    # MEAT
    # Here the user will select their meat however they can only select '1' or
    # '2'. While the user does not input '1' or '2' they will be informed
    # that they have inputted an invalid answer and will be asked again
    # until they input a '1' or '2'.
    # meat_validation is set to True and will continue to stay True until the
    # user inputs either '1' or '2'
    meat_validation = True
    while meat_validation:
        print("Select single or double meat by inputting '1' or '2': ")
        meat = input("1. single meat\n2. double meat\nchoice: ")
        # if the user inputs '1' meat_validation will become False stopping the
        # loop, adding 3.99 to the accumulator "cost", and moving onto the next
        # ingredient
        if meat == '1':
            cost += 3.99
            meat_validation = False
        # if the user inputs '2' meat_validation will become False stopping the
        # loop and moving onto the next ingredient, the same as if the user
        # inputs '1' but a different about will be added to the accumulator
        # "cost"
        elif meat == '2':
            cost += 6.19
            meat_validation = False
        # however, if the user does not input either '1' or '2' the user will
        # be informed they have inputted an invalid answer and the loop will
        # ask the user to try again until they input '1' or '2'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input '1' or '2'. Try again.\n")

    # BUN
    # The user will select the type of bun they want and the only valid
    # answers are '1', '2', or '3'. If an invalid answer is inputted the user
    # will be asked to try again.
    bun_validation = True
    while bun_validation:
        print("\nSelect your bun by inputting '1', '2', or '3': ")
        bun = input("1. regular bun\n2. gluten free bun\n3. no bun\nchoice: ")
        if bun == "1":
            cost += 0.00  # no additional cost is added to "cost"
            bun_validation = False  # while loop stops if user inputs '1'
        elif bun == "2":
            cost += 2.00  # $2.00 is added to "cost"
            bun_validation = False  # while loop stops if user inputs '2'
        elif bun == "3":
            cost -= 0.30  # $0.30 is subtracted to "cost"
            bun_validation = False  # while loop stops if user inputs '3'
        # if user enters an invalid answer they will be asked to try again
        # (bun_validation will stay True repeating the loop)
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input '1', '2', or '3'. Try again.\n")

    # For the cheese and toppings I used the same idea with the while loop.
    # This will only accept certain inputs and will ask the user to try again
    # if an invalid answer is entered

    # CHEESE
    # This is where the user will select the type of cheese they want with the
    # only appropriate answers being '1', '2', or '3'. Also, there is no
    # additional cost for cheese so nothing will be added to the accumulator.
    cheese_validation = True
    while cheese_validation:
        print("\nSelect a cheese by inputting '1', '2', or '3': ")
        cheese = input("1. American\n2. Cheddar\n3. Swiss\nchoice: ")
        if cheese == '1':
            cheese_validation = False  # while loop stops if user inputs '1'
        elif cheese == '2':
            cheese_validation = False  # while loop stops if user inputs '2'
        elif cheese == '3':
            cheese_validation = False  # while loop stops if user inputs '3'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input '1', '2', or '3'. Try again.\n")

    # TOPPINGS
    # The users will select which toppings they want by entering a lower case
    # 'y' for yes or 'n' for no.
    print("\nTo select your toppings input 'y' for yes and 'n' for no.\n"
          "Note: only input lower case 'y' or 'n'\n")

    ketchup_validation = True
    while ketchup_validation:
        ketchup = input("ketchup: ")
        if ketchup == 'y':
            ketchup_validation = False  # while loop stops if user inputs 'y'
        elif ketchup == 'n':
            ketchup_validation = False  # while loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    mustard_validation = True
    while mustard_validation:
        mustard = input("mustard: ")
        if mustard == 'y':
            mustard_validation = False  # while loop stops if user inputs 'y'
        elif mustard == 'n':
            mustard_validation = False  # while loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    pickles_validation = True
    while pickles_validation:
        pickles = input("pickles: ")
        if pickles == 'y':
            pickles_validation = False  # while loop stops if user inputs 'y'
        elif pickles == 'n':
            pickles_validation = False  # while loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    raw_onions_validation = True
    while raw_onions_validation:
        raw_onions = input("raw onions: ")
        if raw_onions == 'y':
            raw_onions_validation = False  # loop stops if user inputs 'y'
        elif raw_onions == 'n':
            raw_onions_validation = False  # loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    grilled_onions_validation = True
    while grilled_onions_validation:
        grilled_onions = input("grilled onions: ")
        if grilled_onions == 'y':
            grilled_onions_validation = False  # loop stops if user inputs 'y'
        elif grilled_onions == 'n':
            grilled_onions_validation = False  # loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    lettuce_validation = True
    while lettuce_validation:
        lettuce = input("lettuce: ")
        if lettuce == 'y':
            lettuce_validation = False  # while loop stops if user inputs 'y'
        elif lettuce == 'n':
            lettuce_validation = False  # while loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    mayo_validation = True
    while mayo_validation:
        mayo = input("mayo: ")
        if mayo == 'y':
            mayo_validation = False  # while loop stops if user inputs 'y'
        elif mayo == 'n':
            mayo_validation = False  # while loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    bacon_validation = True
    while bacon_validation:
        bacon = input("bacon: ")
        if bacon == "y":
            cost += 0.80
            bacon_validation = False  # while loop stops if user inputs 'y'
        elif bacon == 'n':
            bacon_validation = False  # while loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    tomato_validation = True
    while tomato_validation:
        tomato = input("tomato: ")
        if tomato == "y":
            cost += 0.30
            tomato_validation = False  # while loop stops if user inputs 'y'
        elif tomato == 'n':
            tomato_validation = False  # while loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    mushrooms_validation = True
    while mushrooms_validation:
        mushrooms = input("mushrooms: ")
        if mushrooms == "y":
            cost += 0.50
            mushrooms_validation = False  # loop stops if user inputs 'y'
        elif mushrooms == 'n':
            mushrooms_validation = False  # loop stops if user inputs 'n'
        else:
            print("\nSorry, you inputted an invalid answer. Please only "
                  "input a lower case 'y' for yes or 'n' for no. Try again.\n")

    # The total cost is calculated by first obtaining the tax that will
    # be added to the amount in accumulator "cost". The tax amount is found by
    # multiplying 0.065 (sales tax) to the amount in the accumulator "cost"
    # and rounding to the hundredths place. Then the tax amount and the amount
    # in the accumulator "cost" is added and rounded to get the total cost.
    tax = round(cost * 0.065, 2)
    total_cost = cost + tax
    print("\nYour total cost is: $", format(total_cost, "0.2f"))

    # Call trivia_game()
    trivia_game()


def main():
    """
    main() contains the introduction to the program and calls build_burger()
    """

    # Here the print function contains an introduction to the program
    print("Welcome! In this program you will build a burger from Culver's and"
          " play a Culver's trivia game!")

    # Call build_burger()
    build_burger()


main()
# Call main(), main() then calls build_burger(), and lastly build_burger calls
# trivia_game
