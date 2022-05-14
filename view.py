from pygame import display, font, draw


class View:
    def __init__(self, width, height) -> None:
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = (255,200,50)
        display.set_caption('TUNIC Glyph Translator')
        self.screen = display.set_mode((self.WIDTH, self.HEIGHT))
        self.segments = []

    def render(self, model):
        # Background
        self.screen.fill((0,0,0))

        # Flipcircle
        c = model.flipcircle
        if (model.state & c.bin == c.bin):
            draw.circle(self.screen, self.COLOR, (c.x1, c.y1), c.radius, width=5)

        # Line Segments
        for seg in model.segments:
            if (model.state & seg.bin != seg.bin):
                continue
            start = (seg.x1, seg.y1)
            end = (seg.x2, seg.y2)
            draw.line(self.screen, self.COLOR, start, end, width=14)
            draw.circle(self.screen, self.COLOR, (seg.x1+1, seg.y1+1), 7)
            draw.circle(self.screen, self.COLOR, (seg.x2+1, seg.y2+1), 7)
        
        # Translated Text
        myfont = font.Font('freesansbold.ttf', 32)
        text = myfont.render(str(model.getWord()), True, self.COLOR, (50,50,50))
        textRect = text.get_rect()
        textRect.center = (self.WIDTH//2, self.HEIGHT-25)
        self.screen.blit(text, textRect)


        display.flip()