import pygame
from model import Model
from view import View
from controller import Controller

def main():
    pygame.init()

    w = 300
    h = 450
    m = Model(w, h)
    v = View(w, h+75)
    c = Controller()

    while True:
        c.handle(m)
        v.render(m)

if __name__ == "__main__":
    main()