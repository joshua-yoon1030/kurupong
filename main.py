import pygame
import block
import ball

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN, #presses a key down
    QUIT, #presses the x button on pygame window
)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# define a main function
def main():
     
    pygame.init()
    pygame.display.set_caption("KuruPong")

    #clock
    clock = pygame.time.Clock()

    #object generation
    player1 = block.Block(SCREEN_WIDTH, SCREEN_HEIGHT)
    player2 = block.Block(SCREEN_WIDTH, SCREEN_HEIGHT, False)

    myBall = ball.Ball(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    #sprite game generation
    all_sprites = pygame.sprite.Group()
    players = pygame.sprite.Group()

    all_sprites.add(player1)
    all_sprites.add(player2)
    players.add(player1)
    players.add(player2)

    all_sprites.add(myBall)

    #screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg = pygame.image.load("img/bg.png")

    #events
    MUSIC_STOP = pygame.USEREVENT + 1

    #music
    pygame.mixer.init()
    pygame.mixer.music.set_endevent(MUSIC_STOP)

    # define a variable to control the main loop
    running = True
    outer = True
    
    while outer:
        pygame.mixer.music.load("sfx/startMusic.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.queue("sfx/bgm.ogg", loops = -1)

        screen.fill((0,0,0))
        myBall.reset()
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        pygame.display.flip()

        running = True
        wait = True
        while(wait):
            for event in pygame.event.get():
                if event.type == MUSIC_STOP:
                    wait = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        wait = False
                        outer = False
                elif event.type == QUIT:
                    running = False
                    wait = False
                    outer = False

        # main loop
        while running:
            for event in pygame.event.get():
            
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        outer = False
                elif event.type == QUIT:
                    running = False
                    outer = False
                
            pressed_keys = pygame.key.get_pressed()
            player1.update(pressed_keys)
            player2.update(pressed_keys)
            result = myBall.update()
            if result > 0 or result < 0:
                running = False

            if pygame.sprite.spritecollideany(myBall, players):
                myBall.vx = -myBall.vx
                myBall.makeNoise()
                myBall.speedUp()


            screen.fill((0,0,0))
            screen.blit(bg, (0,0))

            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
                
            pygame.display.flip()
            clock.tick(30)

     
if __name__=="__main__":
    # call the main function
    main()