import random
import questions


# Get player name function:
def get_player_name():
    try:
        player_name = input("Enter your name: ")
        if len(player_name) == 0 or len(player_name) > 10:
            raise ValueError
        if not player_name.isalpha():
            print("Invalid input! Please enter a valid name (letters only).")
        else:
            return player_name.capitalize()
    except ValueError:
        print("Invalid input! Please enter"
              "a valid name (up to 10 characters).")
        return get_player_name()


# wellcoming and ask the player to write his name:
print("---------------------------------------------------")
print("Welcome to Who Wants to Be a Millionaire!")
print("---------------------------------------------------")
player_name = get_player_name()

# Game rules
print("---------------------------------------------------")
print("Game Rules:")
print("1. You will be asked a series of multiple-choice questions.")
print("2. Choose the correct answer by"
      "entering the corresponding letter (a, b, c, d).")
print("3. If you answer a question correctly,"
      "you will win the corresponding amount of money.")
print("4. If you answer a question incorrectly,"
      "the game is over.")
print("5. If you reach the $1,000,000 question"
      "and answer it correctly, you will become a millionaire!")
print("---------------------------------------------------")
input("Press Enter to start the game.")

# The game loop
def game_loop():
    # Initialize variables
    total_questions = len(questions.questions)
    current_question = 0
    money = 0

    # Shuffle the questions
    random.shuffle(questions.questions)

    # money increment pattern
    money_increments = [100, 200, 300, 500, 1000, 2000, 4000, 8000,16000, 32000, 64000, 125000, 250000, 500000, 1000000]

    # Function for checking the answer
    def check_answer(question, user_answer):


    # Function for getting user's answer
    def get_user_answer():
            user_answer = input("Enter your answer (a, b, c, d): ")
            return user_answer.lower()


    # Function for handling a single question
    def ask_question(question):
        print("---------------------------------------------------")
        print(player_name, ":", question["question"])
        print("---------------------------------------------------")
        for option in question["options"]:
            print(option)
        

        # Get user's answer


        # Check if the answer is correct
    

    # Game loop


        # Check if the player becomes a millionaire


    # Game ended


    # Ask if the player wants to play again


game_loop()