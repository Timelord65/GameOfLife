
"""
Rules:
Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead

"""



import os
import sys
from copy import deepcopy
from time import sleep

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()
#let the board be of size 50, 50

board = []

for i in range(50):
    thing = []
    for j in range(50):
        
            thing.append(0)

    board.append(thing)

board[1][2] = 1
board[2][3] = 1
board[3][3] = 1
board[3][2] = 1
board[3][1] = 1





class Board:
    def __init__(self, board, width, height):
        self.bo = board
        self.w = width
        self.h = height
        self.size = 50
        self.selected = None
        self.key = None

        pass
    def draw(self, win):
        win.fill([255, 255, 255])
        gap = self.w / 50
        thick = 1
        for i in range(self.size + 1):
            
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.w, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.h), thick)
        
        fnt = pygame.font.SysFont('arial', 10)

        for i in range(50):
            for j in range(50):
                if self.bo[i][j] == 0:
                    continue
                else:
                    txt = fnt.render(str(self.bo[i][j]), 1, (0, 0, 0))
                    win.blit(txt, (j*gap + (gap/2 - txt.get_width()/2), i*gap + (gap/2 - txt.get_height()/2)))


        pass

    def run_step(self):
        stuffy = deepcopy(self.bo)
        dirs = []
                   
        for a in range(-1, 2):
            for b in range(-1, 2):
                if a==0 and b == 0:
                    continue
                else:
                    dirs.append((a, b))

        
        for i in range(50):
            for j in range(50):

                if self.bo[i][j] == 1:
                    count = 0
                    
                    
                    for dir in dirs:
                        x = i
                        y = j
                        x += dir[0]
                        y += dir[1]

                        if x>=0 and x<50 and y>=0 and y<50:
                            if self.bo[x][y] == 1:
                                count += 1
                            else:
                                continue

                    if not (count == 2 or count == 3):
                        stuffy[i][j] = 0

                else:
                    count = 0
                   
                    for dir in dirs:
                        x, y = i, j
                        x += dir[0]
                        y += dir[1]

                        if x>=0 and x<50 and y>=0 and y<50:
                            if self.bo[x][y] == 1:
                                count += 1
                    if count == 3:
                        stuffy[i][j] = 1
        self.bo = deepcopy(stuffy)


                    

    def clicked(self):
        pass
    def selected(self):
        pass



def main():
    print("Main Test")
    width = 600
    height = 600
    screen = pygame.display.set_mode((width, height))
    screen.fill([255, 255, 255])
    A = Board(board, width, height)
    
    running = True
    
    while running:
        
        A.run_step()

        A.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        sleep(0.1)
 
main()

def stuff():
    thingy = pygame.font.get_fonts()
    print(thingy)

#stuff()




