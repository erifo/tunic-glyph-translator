from operator import mod
import pygame

class Controller:
    def __init__(self) -> None:
        pass

    def handle(self, model):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            elif e.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                if (e.button == 1): #Left click
                    for seg in model.segments:
                        if seg.isPointWithinBoundary(mx, my):
                            print("clicked", seg.bin)
                            model.state = model.state ^ seg.bin
                    if model.flipcircle.isPointWithinBoundary(mx,my):
                        print("Clicked circle")
                        model.state = model.state ^ model.flipcircle.bin
                elif (e.button == 3): #Right click
                    model.state = model.state & model.NONE_MASK
