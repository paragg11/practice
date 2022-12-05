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





