if __name__ == "__main__":

    # VARIABLES ASSIGNED TO WORDS IN STRING FORMAT

    player_choice = "rock"
    print(player_choice)

    computer_choice = "paper"
    print(computer_choice)


    # FUNCTIONS
    def get_choices():
        player_choice = "kohli"
        computer_choice = "dhoni"

        return computer_choice


    choices = get_choices()
    print(choices)

    # DIRECTIONARY -> KEY VALUE PAIR

    dict = {"name": "parag", "country": "India"}


    # INPUT FUNCTION
    def get_choices():
        player_choice = input("kohli or dhoni : ")
        computer_choice = "dhoni"
        choices = {"player": player_choice, "computer": computer_choice}
        return choices


    choices = get_choices()
    print(choices)

    # LIBRARY

    import random

    # LISTS

    food = ["pizza", "sandwich", "burger"]
    menu = random.choices(food)
    print(menu)


    # FUNCTIONS ARGUMENTS

    def check_win(player, computer):
        return [player, computer]


    # IF STATEMENTS

    a = 3
    b = 5
    if a >= b:
        print("yes")


    def check_win(player, computer):
        if player == computer:
            return "It's a tie!"


    # CONCATENATE STRINGS -> combination of strings

    def check_win(player, computer):
        print("You choose " + player + ", computer choose " + computer)
        if player == computer:
            return "It's a tie!"


    # F-strings
    def check_win(player, computer):
        print(f"You choose {player}, computer choose {computer}")
        if player == computer:
            return "It's a tie!"


    check_win("rock", "paper")

    # Else and if statements

    age = 28

    if age > 18:
        print("You are an adult.")
    elif age > 12:
        print("You are an teenager.")
    elif age > 1:
        print("You are an child.")
    else:
        print("You are an baby.")

    # REFRACTORING AND NESTED IF-> process of restructing code while keeping the original functionality to make it \
    # simple and more understandable.

    def check_winn(player, computer):
        print(f"You choose {player}, computer choose {computer}.")
        if player == computer:
            print("It's a tie.")
        elif player == "rock":
            if computer == "scissors":
                return "Rock smashes scissors! You win!"
            else:
                return "paper covers rock! You lose!"
        elif player == "paper":
            if computer == "rock":
                return "Paper covers rock! You win!"
            else:
                return "scissors cuts paper! You lose!"
        elif player == "scissors":
            if computer == "paper":
                return "scissors cuts paper! You win!"
            else:
                return "rock smashes scissors! You lose!"

    check_winn("rock", "rock")

    # ACCESSING DICTIONARY VALUE

    choices = {"player": "parag", "computer": "gunjal"}
    p_choices = choices["player"]
    p_choices = choices["computer"]

    # VARIABLES -> you can't use keywords as variable name e.g "if"

    name = "parag"

    # VALID VARIABLES

    # name1
    # HEIGHT
    # my_name
    # _name

    # INVALID VARIABLES

    # 123
    # test!
    # test%

    # EXPRESSIONS AND STATEMENT

    name = "parag"
    print(name)

    name = "parag"; print(name)

    # COMMENTS

    name = "parag" # this is inline comment
    # everything written within hash is ignored

    # DATA TYPES

    name = "parag"                          #STRING
    print(type(name))
    print(type(name) == str)
    print(isinstance(name, str))

    age = 11
    print(isinstance(age, int))
    print(isinstance(age, float))

    # DATA TYPE CONVERSION

    age = float(11)
    print(isinstance(age, float))

    # OPERATORS

    age = 11            # assignment operator
    age += 11

    # ARITHEMATIC OPERTORS

    1 + 1
    2 - 1
    2 * 2
    4 / 2
    4 % 2
    4 // 2

    # COMPARISON OPERATORS

    a == b
    a != b
    a > b
    a <= b

    # BOOLEAN DATA TYPE -> TRUE/FALSE

    # BOOLEAN OPERATORS -> not/or/and

    print(0 or 1)               #1
    print(False or 'hey')       #hey
    print("hi" or "hey")        #hi
    print([] or False)          #False
    print(False or [])          #[]

    print(0 and 1)              #0
    print(1 and 0)              #0
    print(False and 'hey')      #False
    print('hi' and 'hey')       #hey
    print([] and False)         #[]
    print(False and [])         #False

    # BITWISE OPERATORS

    # & performs binary AND
    # | performs binary OR
    # ~ performs a binary NOT operation
    # << shift left operation
    # >> shift right operation

    #TERNARY OPERATOR -> if else statement all in a single line

    def is_adult(age):
        return True if age> 18 else False

    #STRINGS -> "" ''

    name = 'parag'
    phrase = name + " is my name" #concatenated string
    name += " is my name"
    age = str(10)
    print("""
    parag is 
    my 
    name
    """)                            #multiline string

    # STRING METHODS

    print("parag".upper())
    print("PArag".lower())
    print("parag gunjal".title())

    # isalpha() -> contains only character and is not empty
    # isalnum() -> contains characters or digits and is not empty
    # isdecimal() -> contains digit and not empty
    # lower() -> lowercase version
    # islower() -> to check string is lowercase
    # upper() -> uppercase version
    # isupper() -> to check string is uppercase
    # title() -> capitalize version
    # startswith() -> string starts with specific substring
    # endswith() -> string ends with specific substring
    # replace() -> replace part of a string
    # spilt() -> spilt string
    # strip() -> to trim whitespace
    # join() -> to append new letters
    # find() -> to find the position

    # \ -> escaping characters
    # \n -> new line

    # STRING CHARACTERS AND SLICING

    name = "parag"
    print(name[0])                  #p
    print(name[::])                 #parag
    print(name[1:3])                #ar
    print(name[2:])                 #rag

    # BOOLEANS -> True/False

    done = True

    if done:
        print("yes")
    else:
        print("no")

    done = False

    if done:
        print("yes")
    else:
        print("no")

    ingrediants_purchased = True
    meal_cooked = False

    ready_to_serve = any([ingrediants_purchased, meal_cooked])                #True
    print(ready_to_serve)
    ready_to_serve = all([ingrediants_purchased, meal_cooked])                #False
    print(ready_to_serve)