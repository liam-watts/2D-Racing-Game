#https://stackoverflow.com/questions/35001207/how-to-detect-collision-between-objects-in-pygame

import pygame 
pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Mons Liam Car') #funky name
WHITE = (255, 255, 255)

#loading the car
car = pygame.image.load('2dcar.png')
car = pygame.transform.scale(car,(40, 40))

#initial conditions
car_x = 10
car_y = 10
dx, dy = 20, 20

#second car
car2 = pygame.image.load('2dcar.png')
car2rect = car2.get_rect()
car2rect.topleft=(0,0)

while True: # the main game loop
    for event in pygame.event.get(): #add some events to the game
        DISPLAYSURF.fill(WHITE)
        if event.type == pygame.QUIT:
            pygame.quit()
            

        if event.type == pygame.KEYDOWN: #moving directions with keys
                if event.key == pygame.K_LEFT:
                    car_x += -dx
                elif event.key == pygame.K_RIGHT:
                    car_x += dx
                elif event.key == pygame.K_DOWN:
                    car_y += dy
                elif event.key == pygame.K_UP:
                    car_y += -dy

        DISPLAYSURF.blit(car, (car_x, car_y)) #display the cat if an "event" happens
    pygame.display.update()