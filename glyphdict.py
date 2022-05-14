class Glyphdict:
    def __init__(self) -> None:
        self.consonants = {
            0b0_101000_000000 : "W(wit)",
            0b0_101010_000000 : "T(tunic)",
            0b0_110110_000000 : "S(sit)"
        }

        self.vowels = {
            0b0_000000_000001 : "OW(how)",
            0b0_000000_000010 : "OY(toy)",
            0b0_000000_001110 : "OU(wolf)"
        }