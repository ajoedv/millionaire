import random
import questions


def get_player_name():
        player_name = input("Enter your name: ")
        print(player_name)
        return get_player_name()
get_player_name()