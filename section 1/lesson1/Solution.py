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

    # NUMBER DATA TYPES - COMPLEX TYPE

    num1 = 2+3j
    num2 = complex(2, 3)

    print(num2.real, num2.imag)         # 2.0 3.0
    print(abs(-111))                    # 111
    print(round(5.6))                   # 6
    print(round(5.4))                   # 5

    # ENUMERATE

    from enum import Enum

    class State(Enum):
        INACTIVE = 0
        ACTIVE = 1

    print(State.INACTIVE)       # State.Inactive
    print(State.INACTIVE.value)     # 0
    print(list(State))              # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
    print(State(1))                 # State.ACTIVE

    #  USER INPUT FUNCTION

    age = input("What is your age? ")
    print("your age is " + age)

    # CONTROL STATEMENTS

    condition = True
    name = "parag"

    if condition == True:
        print("yes")
    elif name == "parag1":
        print("woho")
    else:
        print("quit")

    # LISTS

    dogs = ["roger", 1, "syd", True]

    print("roger" in dogs)          # True
    print("rog" in dogs)            # False

    print(dogs[0])          # roger
    print(dogs[2])          # syd

    dogs[2] = "coopie"

    print(dogs[2])          # coopie
    print(dogs)             # ['roger', 1, 'coopie', True]

    print(dogs[1:3])        # slicing -> [1, 'coopie']
    print(len(dogs))        # 4

    dogs.append("max")           #
    dogs.extend(["ray", 5])
    dogs += ["ray", 5]
    print(dogs)             # ['roger', 1, 'coopie', True, 'max', 'ray', 5, 'ray', 5]

    dogs.pop()              # 5
    print(dogs)             # ['roger', 1, 'coopie', True, 'max', 'ray', 5, 'ray']

    dogs.insert(2, "aa")
    print(dogs)             # ['roger', 1, 'aa', 'coopie', True, 'max', 'ray', 5, 'ray']

    dogs[1:1] = ["bb", "cc"]        #inserting multiple items
    print(dogs)             # ['roger', 'bb', 'cc', 1, 'aa', 'coopie', True, 'max', 'ray', 5, 'ray']

    items = ["Roger", "bob", "Brew", "Quincy"]
    items.sort()
    print(items)                    # ['Brew', 'Quincy', 'Roger', 'bob']
    items.sort(key=str.lower)
    print(items)                    # ['bob', 'Brew', 'Quincy', 'Roger']

    print(sorted(items, key=str.lower))     # ['bob', 'Brew', 'Quincy', 'Roger']

    # TUPLES -> no changes

    names = ('parag', 'pg', 'parry')
    names[0]
    names[0:2]
    len(names)
    print("parag" in names)
    print(sorted(names))
    newtuples = names + ("gg", "pmg")
    print(newtuples)                        # ('parag', 'pg', 'parry', 'gg', 'pmg')

    # DICTIONARIES  -> key-value pair

    dog = {"name": "Roger", "age": 10}

    print(dog["name"])                      # Roger

    dog["name"] = "coopie"

    print(dog)                              # {'name': 'coopie', 'age': 10}
    print(dog.get("name"))                  # coopie

    print(dog.get("color", "white"))        # white
    print(dog)                              # {'name': 'coopie', 'age': 10}
    print(dog.get("color", "red"))          # red

    print(dog.pop("name"))                  # coopie
    print(dog)                              # {'age': 10}

    #print(dog.popitem())    ->             # removes last item in dictionary

    dog = {"name": "coopie", "age": 1, "color": "white"}
    print(dog.keys())                       # dict_keys(['name', 'age', 'color'])
    print(list(dog.keys()))                 # ['name', 'age', 'color']
    print(dog.values())                     # dict_values(['coopie', 1, 'white'])
    print(list(dog.values()))               # ['coopie', 1, 'white']

    dog["favourite food"] = "meat"
    print(dog)                              # {'name': 'coopie', 'age': 1, 'color': 'white', 'favourite food': 'meat'}

    del dog["color"]

    # SETS  -> one of each in one set

    set1 = {"Rogers", "syd"}
    set2 = {"Rogers"}

    intersect = set1 & set2
    print(intersect)                     # {'Rogers'}

    modification = set1 | set2
    print(modification)                  # {'Rogers', 'syd'}

    difference = set1 - set2
    print(difference)                    # {'syd'}

    mod = set1 > set2
    print(mod)                           # True

    mod = set1 < set2
    print(mod)                           # False

    # FUNCTIONS

    def hello():
        print("parag")

    hello()                             # parag


    def hello(name):
        print("Hello " + name)

    hello("parag")                      # Hello parag


    def hello(name = "Parag"):
        print("Hello" + name)

    hello()                             # HelloParag

    def hello(name, age):
        print("Hello " + name + ", you are " + str(age) + " years old!")

    hello("Parag", 28)                  # Hello Parag, you are 28 years old!

    def hello(name):
        if not name:
            return
        print("Hello " + name + "!")

    hello(False)                        #
    hello("parag")                      # Hello parag!

    def hello(name):
        print("Hello" + name + "!")
        return name, "Gunjal", 20

    print(hello("parag"))              # Helloparag!
                                       # ('parag', 'Gunjal', 20)


    # VARIABLE SCOPES

    age = 8                             # Global variable

    def test():
        print(age)

    print(age)                          # 8
    test()                              # 8


    # def test():
    #     age = 8                         # inside function
    #     print(age)
    #
    # print(age)
    # test()

    #
