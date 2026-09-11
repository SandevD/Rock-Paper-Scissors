# Author: Sandev Dullewa

import random

# The below function is used to display a welcome screen with instructions in colourful text.
def welcome_screen():
    cyan = "\033[96m"
    green = "\033[92m"
    red = "\033[91m"
    yellow = "\033[93m"
    reset = "\033[0m"

    border = f"{cyan}{'=' * 42}{reset}"
    title = "ROCK, PAPER, SCISSORS".center(42)

    print(f"\n{border}")
    print(f"{yellow}{title}{reset}")
    print(border)
    print(f"{green}Welcome! Choose rock, paper, or scissors.{reset}")
    print(f"{red}Enter q if you want to quit.{reset}")
    print(f"{border}\n")

# The blow function is used to retrieve the player's choice, also checking if the choice is valid as well.
def retrieve_player_choice(choices):
    red = "\033[91m"
    reset = "\033[0m"

    while True:
        player_choice = input("Your choice: ").strip().lower()

        if player_choice == "q" or player_choice in choices:
            return player_choice

        print(f"{red}Invalid choice. Please enter rock, paper, or scissors.{reset}\n")

# The below function is used to find or decide the winner of the game, based on the choices made by both the player and the computer.
def find_winner(player, computer):
    if player == computer:
        return "draw"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"

# The below function is used to display the result of each round in a colourful manner.
def round_result_screen(winner, player_score, computer_score, draw_score):
    cyan = "\033[96m"
    green = "\033[92m"
    red = "\033[91m"
    yellow = "\033[93m"
    reset = "\033[0m"

    if winner == "player":
        result_message = f"{green}You win this round!{reset}"
    elif winner == "computer":
        result_message = f"{red}Computer wins this round!{reset}"
    else:
        result_message = f"{yellow}It is a draw!{reset}"

    border = f"{cyan}{'-' * 42}{reset}"
    print(border)
    print(f"{cyan}              ROUND RESULT{reset}")
    print(result_message)
    print(
        f"{green}You: {player_score}{reset}   |   "
        f"{yellow}Draws: {draw_score}{reset}   |   "
        f"{red}Computer: {computer_score}{reset}"
    )
    print(f"{border}\n")

# The below function is used to display the final scores of the game.
def final_results_screen(player_score, computer_score, draw_score):
    cyan = "\033[96m"
    green = "\033[92m"
    red = "\033[91m"
    yellow = "\033[93m"
    reset = "\033[0m"

    if player_score > computer_score:
        result_message = f"{green}Congrats, you have won the game!{reset}"
    elif computer_score > player_score:
        result_message = f"{red}The computer has won the game. Better luck next time!{reset}"
    else:
        result_message = f"{yellow}The game has ended in a draw!{reset}"

    border = f"{cyan}{'=' * 42}{reset}"
    print(f"\n{border}")
    print(f"{yellow}               FINAL SCORE{reset}")
    print(border)
    print(
        f"{green}You: {player_score}{reset}   |   "
        f"{yellow}Draws: {draw_score}{reset}   |   "
        f"{red}Computer: {computer_score}{reset}"
    )
    print(result_message)
    print(border)
    print("\nThanks for playing!\n")


def main():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    draw_score = 0

    welcome_screen()

    while True:
        player_choice = retrieve_player_choice(choices)

        if player_choice == "q":
            break

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        winner = find_winner(player_choice, computer_choice)

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        else:
            draw_score += 1

        round_result_screen(winner, player_score, computer_score, draw_score)

    final_results_screen(player_score, computer_score, draw_score)


if __name__ == "__main__":
    main()
