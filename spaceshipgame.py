
import pygame
import random
import sys

pygame.init()
HEIGHT=800
WIDTH=600
GREEN=(255,0,0)
BLUE=(0,0,255)
#GREEN=(0,255,200)
#GREEN=(50,50,50)
RED=(255,0,0)

YELLOW=(255,255,0)

SPEED=10




pygame.mixer.music.load('jazz.mp3')
pygame.mixer.music.play(-1)

clock=pygame.time.Clock()
sky=pygame.image.load('sky.jpg')
sky = pygame.transform.scale(sky, (HEIGHT, WIDTH))
redSquare = pygame.image.load("n.jpg")
redSquare = pygame.transform.scale(redSquare,(50,50))

enemy=pygame.image.load('x.jpg')
enemy = pygame.transform.scale(enemy,(85,85))


enemy1=pygame.image.load('x1.jpg')
enemy1 = pygame.transform.scale(enemy1,(75,75))


imageX= 500; # x coordnate of image
imageY= 500; # y coordinate of image



myFont = pygame.font.SysFont("monospace", 50)

myFont1 = pygame.font.SysFont("monospace", 50)





player_pos=[370,501]
player_size=50

enemy_size=50
enemy_pos=[random.randint(0,WIDTH),0]
enemy_list=[enemy_pos]

screen = pygame.display.set_mode((HEIGHT,WIDTH))
gameover = False


score=0


def drop_enemies(enemy_list):
    delay= random.random()
    if len(enemy_list)<5+(score/25) :
        x_pos=random.randint(0,WIDTH-enemy_size)
        y_pos=0
        enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
          screen.blit(enemy,(random.randint(enemy_pos[0],enemy_pos[0]+1),random.randint(enemy_pos[1],enemy_pos[1]+1)))
          
    



def collision_check(enemy_list,player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False




def update_enemy_positions(enemy_list,score):
    for enemy_pos in enemy_list:
        if enemy_pos[1]>=0 and enemy_pos[1]<HEIGHT:
            enemy_pos[1] += SPEED
        else:
            score+=1
            
            enemy_pos[0]=random.randint(0,HEIGHT-enemy_size)
            enemy_pos[1]=0
    return score





def detect_collision(player_pos,enemy_pos):
    p_x=player_pos[0]
    p_y=player_pos[1]

    e_x=enemy_pos[0]
    e_y=enemy_pos[1]

    if (e_x>p_x+20 and e_x<(p_x+player_size)) or (e_x<p_x and p_x<(e_x+enemy_size)):
        if(e_y>p_y and e_y<(p_y+player_size)) or (p_y>e_y and p_y<(e_y+enemy_size)):
            return True
            #screen.fill(YELLOW)
    return False




while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
         
            x=player_pos[0]
            y=player_pos[1]
            if event.key == pygame.K_LEFT:
                if x>0+player_size :
                    x-=player_size
                else:
                    continue
                
            elif event.key == pygame.K_RIGHT:
                if x<HEIGHT-player_size:
    
                    x+=player_size
                else:
                    continue

            
            elif event.key == pygame.K_UP:
                if y>0:
                    y-=player_size
                else:
                    continue

            
            elif event.key == pygame.K_DOWN:
                if y<WIDTH-player_size:
                    y+=player_size
                else:
                    continue

            elif event.key == pygame.K_SPACE:
                gameover=True
                break


    
                
            
                
            player_pos = [x,y]



    
    drop_enemies(enemy_list)
    screen.fill((YELLOW))
    
    screen.blit(sky,(0,0))

    #screen.blit(enemy,(300,300))
    



    score = update_enemy_positions(enemy_list,score)
    text = "Score:"+ str(score)
    
    lad = myFont.render(text, 1, (GREEN))
    screen.blit(lad, (545,545))


    txt1= "Press SPACE BAR to exit"
    lad1=myFont1.render(txt1,1,(GREEN))
    screen.blit(lad1,(25,85))
    


    if collision_check(enemy_list,player_pos):
        gameover=True
        
        break
  
    draw_enemies(enemy_list)
    

    screen.blit(redSquare , (random.randint(player_pos[0],player_pos[0]+1), random.randint(player_pos[1],player_pos[1]+1)) ) # paint to screen

    
    #pygame.draw.rect(screen,(225,0,0),(300,300,30,30))

    
   
    clock.tick(30)
    pygame.display.update()

pygame.mixer.music.stop()
        
pygame.quit()
