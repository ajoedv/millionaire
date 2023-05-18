import random
import questions


def get_player_name():
    try:
        player_name = input("Enter your name: ")
        if len(player_name) == 0 or len(player_name) > 10:
            raise ValueError
        return player_name.capitalize()
    except ValueError:
        print("Invalid input! Please enter"
              "a valid name (up to 10 characters).")
        return get_player_name()
get_player_name()