import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()
screen = pygame.display.set_mode((400,400), 0, 32)
pygame.display.set_caption("The 15 Puzzle!")
screen.fill((255,255,255))
clock = pygame.time.Clock()

num_imgs = []
num = []
hole = (3,3)
prev_hole = (-1,-1)
ran = sample(range(0,15),15)
animation_speed = 0.002

def check(ran = []):
    ans = 0
    for i in range(0,14):
        for j in range(i+1,15):
            if ran[j] < ran[i]:
                ans += 1
    return ans%2 == 0

while not check(ran):
    ran = sample(range(0,15),15)
ran.append(15)

for i in range(1,16):
    num_imgs.append(pygame.image.load(str(i)+'.png'))
num_imgs.append(0)

for i in range(0,16):
    num.append(((i%4),(i//4)))

def move(x,y,num_imgs = []):
    global hole, prev_hole
    absx = abs(hole[0] - x)
    absy = abs(hole[1] - y)
    if (absx == 0 or absx == 1) and (absy == 0 or absy == 1) and (absx != absy):
        num_imgs[ran[hole[1]*4+hole[0]]] = num_imgs[ran[y*4+x]]
        num_imgs[ran[y*4+x]] = 0
        prev_hole = hole
        hole = (x,y)
    return num_imgs

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            x -= 72
            y -= 72
            num_imgs = move(x//64,y//64,num_imgs)
    u, v = hole
    pygame.draw.rect(screen,(255,0,0),(64,64,272,272),4)
    for i in range(0,16):
        if num_imgs[ran[i]] and i != prev_hole[1]*4+prev_hole[0]:
            screen.blit(num_imgs[ran[i]],(72+64*num[i][0],72+64*num[i][1]))

        elif prev_hole[0] == hole[0]:
            c = 0
            if prev_hole[1] > hole[1]:
                while c <= 1:
                    if c:
                        screen.fill((255,255,255),(72+64*u,72+64*(v+c-animation_speed),65,65))
                    screen.blit(num_imgs[ran[prev_hole[1]*4+prev_hole[0]]],(72+64*u,72+64*(v + c)))
                    for j in range(0,16):
                        if j != prev_hole[1]*4+prev_hole[0] and num_imgs[ran[j]]:
                             screen.blit(num_imgs[ran[j]],(72+64*num[j][0],72+64*num[j][1]))
                    c += animation_speed
                    pygame.display.update()
                prev_hole = (-1,-1)
            else:
                while c >= -1:
                    if c:
                        screen.fill((255,255,255),(72+64*u,72+64*(v+c+animation_speed),65,65))
                    screen.blit(num_imgs[ran[prev_hole[1]*4+prev_hole[0]]],(72+64*u,72+64*(v + c)))
                    for j in range(0,16):
                        if j != prev_hole[1]*4+prev_hole[0] and num_imgs[ran[j]]:
                             screen.blit(num_imgs[ran[j]],(72+64*num[j][0],72+64*num[j][1]))
                    c -= animation_speed
                    pygame.display.update()
                prev_hole = (-1,-1)

        elif prev_hole[1] == hole[1]:
            c = 0
            if prev_hole[0] > hole[0]:
                while c <= 1:
                    if c:
                        screen.fill((255,255,255),(72+64*(u+c-animation_speed),72+64*v,65,65))
                    screen.blit(num_imgs[ran[prev_hole[1]*4+prev_hole[0]]],(72+64*(u + c),72+64*v))
                    for j in range(0,16):
                        if j != prev_hole[1]*4+prev_hole[0] and num_imgs[ran[j]]:
                             screen.blit(num_imgs[ran[j]],(72+64*num[j][0],72+64*num[j][1]))
                    c += animation_speed
                    pygame.display.update()
                prev_hole = (-1,-1)

            else:
                while c >= -1:
                    if c:
                        screen.fill((255,255,255),(72+64*(u+c+animation_speed),72+64*v,65,65))
                    screen.blit(num_imgs[ran[prev_hole[1]*4+prev_hole[0]]],(72+64*(u + c),72+64*v))
                    for j in range(0,16):
                        if j != prev_hole[1]*4+prev_hole[0] and num_imgs[ran[j]]:
                             screen.blit(num_imgs[ran[j]],(72+64*num[j][0],72+64*num[j][1]))
                    c -= animation_speed
                    pygame.display.update()
                prev_hole = (-1,-1)

    pygame.display.update()
