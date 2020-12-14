import pygame
import os 
import random

pygame.init()
pygame.mixer.init()

#! Colour Code
white_colour = (255,255,255)
red_colour = (255,0,0)
blue_colour = (0,191,155)
black_colour = (0,0,0)

#! Creating Window 
screen_width = 600
screen_height = 500
game_window = pygame.display.set_mode((screen_width,screen_height))

#! Background Image 1
bg_img = pygame.image.load('C:\\Users\\admin\Desktop\\Snake-Game\\start.jpg')
bg_img = pygame.transform.scale(bg_img,
(screen_width,screen_height)).convert_alpha()

#! Background Image 2
bg_img2 = pygame.image.load('C:\\Users\\admin\\Desktop\\Snake-Game\\back.jfif')
bg_img2 = pygame.transform.scale(bg_img2,
(screen_width,screen_height)).convert_alpha()

#! BackGround Image 3
bg_img3 = pygame.image.load('C:\\Users\\admin\\Desktop\\Snake-Game\\gameover.jpg')
bg_img3 = pygame.transform.scale(bg_img3,
(screen_width,screen_height)).convert_alpha()

#! Setting Game Title m
pygame.display.set_caption('Snake Game ')
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial',20)

#! Setting Text Screen
def text_screen(text, colour, x, y) :
    screen_text = font.render(text,True,colour) 
    game_window.blit(screen_text, [x,y])

#! Plotting Snake
def plot_snake(gamewindow, colour, snakelist, snakesize):
    for x,y in snakelist :
        pygame.draw.rect(gamewindow, colour, [x, y, snakesize, snakesize])

#! Welcome Screen
def welcome():
    exit_game = False

    while not exit_game : 
        game_window.fill((233,210,229))
        game_window.blit(bg_img, (0,0))


#! Event ManageMent
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                exit_game = True

            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_SPACE : 
                    pygame.mixer.music.load('onmyway.mp3')
                    pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(60)

#! Main Game
def game_loop() :

#! Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1


#! Creating highscore.txt if not
    if(not os.path.exists("highcore.txt")):
        with open("highcore.txt", "w") as f:
            f.write("0")

    with open('highscore.txt', 'r') as f : 
        highscore = f.read()

    food_x = random.randint(45, screen_width / 2)
    food_y = random.randint(45, screen_height / 2)

    score = 0
    init_velocity  = 3

    snake_size = 15

    while not exit_game : 
        if game_over :
            with open('highscore.txt', 'w') as f :
                f.write(str(highscore))
            game_window.fill(white_colour)
            game_window.blit(bg_img3,(0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_length +=5
                if score>int(highscore):
                    highscore = score

            game_window.fill(white_colour)
            game_window.blit(bg_img2, (0, 0))
            text_screen("Score: " + str(score) + "  HighScore: "+str(highscore), (0, 195, 253), 0, 5)
            pygame.draw.rect(game_window, red_colour, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)


            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('C:\\Users\admin\Desktop\\Snake-Game\\game_over.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('C:\\Users\\admin\Desktop\\Snake-Game\\game_over.mp3')
                pygame.mixer.music.play()
            plot_snake(game_window, black_colour, snake_list, snake_size)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

welcome()