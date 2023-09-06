import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Choices
choices = ["rock", "paper", "scissors"]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'rock') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    clock = pygame.time.Clock()
    player_choice = None
    computer_choice = None
    result = None
    player_turn = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and player_turn:
                if event.key == pygame.K_r:
                    player_choice = "rock"
                    player_turn = False
                elif event.key == pygame.K_p:
                    player_choice = "paper"
                    player_turn = False
                elif event.key == pygame.K_s:
                    player_choice = "scissors"
                    player_turn = False

        if not player_turn and not computer_choice:
            computer_choice = get_computer_choice()
            result = determine_winner(player_choice, computer_choice)

        # Clear the screen
        screen.fill(WHITE)

        # Display choices and result
        if player_turn:
            player_text = FONT.render("Player's turn", True, (0, 0, 0))
        else:
            player_text = FONT.render(f"Player chose: {player_choice}", True, (0, 0, 0))
            computer_text = FONT.render(f"Computer chose: {computer_choice}", True, (0, 0, 0))
            result_text = FONT.render(result, True, (0, 0, 0))

        screen.blit(player_text, (20, 20))
        if not player_turn:
            screen.blit(computer_text, (20, 60))
            screen.blit(result_text, (20, 100))

        pygame.display.update()

        if not player_turn and result:
            pygame.time.delay(2000)  # Pause for a moment to display the result
            player_choice = None
            computer_choice = None
            result = None
            player_turn = True

        clock.tick(30)

if __name__ == "__main__":
    main()
