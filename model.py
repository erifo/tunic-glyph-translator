from glyphsegment import Glyphsegment
from glyphcircle import Glyphcircle
from glyphdict import Glyphdict

class Model:
    def __init__(self, width, height) -> None:
        self.WIDTH = width
        self.HEIGHT = height
        self.FLIP_MASK = 0b1_000000_000000
        self.CONSONANT_MASK = 0b0_111111_000000
        self.VOWEL_MASK = 0b0_000000_111111
        self.state = 0b1_111111_111111
        self.glyphdict = Glyphdict()
        self.flipcircle = None
        self.segments = []
        self.segmentSetup()

    def segmentSetup(self):
        # Establish width and height units.
        wu = self.WIDTH//8
        hu = self.HEIGHT//12
        padding = 10

        # Circle used for order flipping
        self.flipcircle = Glyphcircle(0b1_000000_000000, wu*4, hu//2*24, 20, padding)
        
        # Baseline
        self.segments.append(Glyphsegment(0b0_000000_000000, wu*1, hu*6, wu*7, hu*6, -5))

        # Upside filler
        self.segments.append(Glyphsegment(0b0_001000_000000, wu*4, hu*6, wu*4, hu*5, -5))
        self.segments.append(Glyphsegment(0b0_010000_000000, wu*4, hu*6, wu*4, hu*5, -5))
        self.segments.append(Glyphsegment(0b0_100000_000000, wu*4, hu*6, wu*4, hu*5, -5))

        # Consonants
        self.segments.append(Glyphsegment(0b0_000001_000000, wu*4, hu*7, wu*7, hu*9, -padding))
        self.segments.append(Glyphsegment(0b0_000010_000000, wu*4, hu*7, wu*4, hu*11, padding))
        self.segments.append(Glyphsegment(0b0_000100_000000, wu*4, hu*7, wu*1, hu*9, -padding))
        # ---
        self.segments.append(Glyphsegment(0b0_001000_000000, wu*4, hu*5, wu*1, hu*3, -padding))
        self.segments.append(Glyphsegment(0b0_010000_000000, wu*4, hu*5, wu*4, hu*1, padding))
        self.segments.append(Glyphsegment(0b0_100000_000000, wu*4, hu*5, wu*7, hu*3, -padding))

        # Vowels
        self.segments.append(Glyphsegment(0b0_000000_000001, wu*7, hu*9, wu*4, hu*11, -padding))
        self.segments.append(Glyphsegment(0b0_000000_000010, wu*4, hu*11, wu*1, hu*9, -padding))
        self.segments.append(Glyphsegment(0b0_000000_000100, wu*1, hu*9, wu*1, hu*7, padding))
        # ---
        self.segments.append(Glyphsegment(0b0_000000_001000, wu*1, hu*6, wu*1, hu*3, padding))
        self.segments.append(Glyphsegment(0b0_000000_010000, wu*1, hu*3, wu*4, hu*1, -padding))
        self.segments.append(Glyphsegment(0b0_000000_100000, wu*4, hu*1, wu*7, hu*3, -padding))
    

    def isFlipped(self):
        return self.state & self.FLIP_MASK == self.FLIP_MASK

    def getWord(self):
        if (self.isFlipped()):
            return self.getVowel() + " " + self.getConsonant()
        return self.getConsonant() + " " + self.getVowel()

    def getConsonant(self):
        bin = self.CONSONANT_MASK & self.state
        if bin not in self.glyphdict.consonants:
            return "---"
        return self.glyphdict.consonants[bin]

    def getVowel(self):
        bin = self.VOWEL_MASK & self.state
        if bin not in self.glyphdict.vowels:
            return "---"
        return self.glyphdict.vowels[bin]
