# users = [
#     {'username':'admin','password':'admin001'},
#     {'username':'ram','password':'ram001'}
# ]

# username = input("enter your username: ")

# for data in users:
#     data1 = data['username']
#     data2 = data['password']

#     if data1 == username:
#         password = input("enter your password: ")
#         if data2 == password:
#             print("welcome to system")
#         else:
#             print("your password is incorrect")    
#     else:
#         print("Username is incorrect")        
       

# numbers = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

# for num in range(len(numbers[0])):
#     #    for x in num:
#         print(numbers[0][num])

# student = []
# num = int(input("enter a numebr of student: "))
# x=1

# while x<=num:
#     name = input( f"enter a  name of student {x}: ")
#     student.append(name)
#     x +=1

# print(student)

# for i in range(1,11):
#     print("\n")
#     for j in range(1,11):
#         print(f"{i}*{j}= {i * j}")

import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Subway Surfer-like Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Player settings
player_width = 50
player_height = 50
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 10

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5

# Coin settings
coin_radius = 15
coin_speed = 5

# Game variables
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Function to display score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

# Function to draw an obstacle
def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

# Function to draw a coin
def draw_coin(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), coin_radius)

# Main game loop
def game_loop():
    global player_x, score, obstacle_speed, coin_speed

    # Game loop flag
    game_running = True

    # Obstacle settings
    obstacles = []
    coins = []

    while game_running:
        screen.fill(WHITE)  # Fill the screen with white background

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_speed

        # Add new obstacles and coins
        if random.random() < 0.02:  # Random chance to spawn obstacles and coins
            obstacle_x = random.randint(0, width - obstacle_width)
            obstacles.append([obstacle_x, -obstacle_height])  # Add obstacle at random position
        if random.random() < 0.03:  # Random chance to spawn coins
            coin_x = random.randint(0, width - coin_radius)
            coins.append([coin_x, -coin_radius * 2])  # Add coin at random position

        # Move obstacles and coins
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if obstacle[1] > height:
                obstacles.remove(obstacle)  # Remove obstacle if it goes off-screen
            if player_x < obstacle[0] + obstacle_width and player_x + player_width > obstacle[0] and \
               player_y < obstacle[1] + obstacle_height and player_y + player_height > obstacle[1]:
                game_running = False  # Game over if collision happens

        for coin in coins:
            coin[1] += coin_speed
            if coin[1] > height:
                coins.remove(coin)  # Remove coin if it goes off-screen
            if player_x < coin[0] + coin_radius and player_x + player_width > coin[0] and \
               player_y < coin[1] + coin_radius and player_y + player_height > coin[1]:
                score += 1  # Increase score when coin is collected
                coins.remove(coin)  # Remove the collected coin

        # Draw obstacles and coins
        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])
        for coin in coins:
            draw_coin(coin[0], coin[1])

        # Draw player and score
        draw_player(player_x, player_y)
        display_score(score)

        # Increase difficulty (speed) every 10 points
        if score % 10 == 0:
            obstacle_speed = 5 + score // 10
            coin_speed = 5 + score // 20

        # Update the screen
        pygame.display.updsate()

        # Set game speed (frames per second)
        clock.tick(60)

    # Game over screen
    game_over_text = font.render("Game Over! Final Score: " + str(score), True, RED)
    screen.fill(WHITE)
    screen.blit(game_over_text, (width // 4, height // 2))
    pygame.display.update()
    pygame.time.wait(3000)  # Wait for 3 seconds before closing the game
    pygame.quit()

# Run the game
game_loop()
