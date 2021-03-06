class Glyphdict:
    def __init__(self) -> None:
        self.consonants = {
            0b0_010001_000000 : "B(baby)",
            0b0_001010_000000 : "CH(chat)",
            0b0_010101_000000 : "D(dog)",
            0b0_100110_000000 : "F(fox)",
            0b0_100011_000000 : "G(gun)",
            0b0_010011_000000 : "H(hop)",
            0b0_010100_000000 : "J(jam)",
            0b0_110001_000000 : "K(kart)",
            0b0_010010_000000 : "L(live)",
            0b0_000101_000000 : "M(move)",
            0b0_001101_000000 : "N(net)",
            0b0_111111_000000 : "NG(ring)",
            0b0_100010_000000 : "P(pot)",
            0b0_110010_000000 : "R(run)",
            0b0_110110_000000 : "S(sit)",
            0b0_101111_000000 : "SH(shut)",
            0b0_101010_000000 : "T(tunic)",
            0b0_111010_000000 : "TH(thick)",
            0b0_010111_000000 : "TH(this)",
            0b0_011001_000000 : "V(vine)",
            0b0_101000_000000 : "W(wit)",
            0b0_011010_000000 : "Y(you)",
            0b0_011011_000000 : "Z(zit)",
            0b0_111101_000000 : "ZH(azure)",
        }

        self.vowels = {
            0b0_000000_111100 : "A(glass)",
            0b0_000000_110011 : "AR(arm)",
            0b0_000000_011100 : "AH(swan)",
            0b0_000000_010000 : "AY(bay)",
            0b0_000000_001111 : "E(end)",
            0b0_000000_011111 : "EE(bee)",
            0b0_000000_011101 : "EER(beer)",
            0b0_000000_110000 : "EH(the)",
            0b0_000000_001101 : "ERE(air)",
            0b0_000000_000011 : "I(bit)",
            0b0_000000_100000 : "IE(guy)",
            0b0_000000_101111 : "IR(bird)",
            0b0_000000_111111 : "OH(toe)",
            0b0_000000_000010 : "OI(toy)",
            0b0_000000_111110 : "OO(too)",
            0b0_000000_001110 : "OU(wolf)",
            0b0_000000_000001 : "OW(how)",
            0b0_000000_111101 : "ORE(your)"
        }