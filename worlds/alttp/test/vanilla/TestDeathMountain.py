from .TestVanilla import TestVanilla


class TestDeathMountain(TestVanilla):

    def testWestDeathMountain(self):
        self.run_location_tests([
            ["Ether Tablet", False, []],
            ["Ether Tablet", False, [], ['Progressive Glove', 'Flute']],
            ["Ether Tablet", False, [], ['Lamp', 'Flute']],
            ["Ether Tablet", False, [], ['Magic Mirror', 'Hookshot']],
            ["Ether Tablet", False, [], ['Magic Mirror', 'Hammer']],
            ["Ether Tablet", False, ['Progressive Sword'], ['Progressive Sword']],
            ["Ether Tablet", False, [], ['Book of Mudora']],
            ["Ether Tablet", True, ['Flute', 'Magic Mirror', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Flute', 'Hammer', 'Hookshot', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Progressive Glove', 'Lamp', 'Hammer', 'Hookshot', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],

            ["Old Man", False, []],
            ["Old Man", False, [], ['Progressive Glove', 'Flute']],
            ["Old Man", False, [], ['Lamp']],
            ["Old Man", True, ['Flute', 'Lamp']],
            ["Old Man", True, ['Progressive Glove', 'Lamp']],

            ["Spectacle Rock Cave", False, []],
            ["Spectacle Rock Cave", False, [], ['Progressive Glove', 'Flute']],
            ["Spectacle Rock Cave", False, [], ['Lamp', 'Flute']],
            ["Spectacle Rock Cave", True, ['Flute']],
            ["Spectacle Rock Cave", True, ['Progressive Glove', 'Lamp']],

            ["Spectacle Rock", False, []],
            ["Spectacle Rock", False, [], ['Progressive Glove', 'Flute']],
            ["Spectacle Rock", False, [], ['Lamp', 'Flute']],
            ["Spectacle Rock", False, [], ['Magic Mirror']],
            ["Spectacle Rock", True, ['Flute', 'Magic Mirror']],
            ["Spectacle Rock", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
        ])
        
    def testEastDeathMountain(self):
        self.run_location_tests([
            ["Mimic Cave", False, []],
            ["Mimic Cave", False, [], ['Quake']],
            ["Mimic Cave", False, [], ['Progressive Sword']],
            ["Mimic Cave", False, ['Progressive Glove'], ['Progressive Glove']],
            ["Mimic Cave", False, [], ['Hammer']],
            ["Mimic Cave", False, [], ['Magic Mirror']],
            ["Mimic Cave", False, [], ['Moon Pearl']],
            ["Mimic Cave", False, [], ['Cane of Somaria']],
            ["Mimic Cave", False, ['Small Key (Turtle Rock)'], ['Small Key (Turtle Rock)']],
            ["Mimic Cave", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Mimic Cave", True, ['Bomb Upgrade (+5)', 'Quake', 'Progressive Sword', 'Flute', 'Progressive Glove', 'Progressive Glove', 'Hammer', 'Moon Pearl', 'Cane of Somaria', 'Magic Mirror', 'Small Key (Turtle Rock)', 'Small Key (Turtle Rock)']],
            
            ["Spiral Cave", False, []],
            ["Spiral Cave", False, [], ['Progressive Glove', 'Flute']],
            ["Spiral Cave", False, [], ['Magic Mirror', 'Hammer', 'Hookshot']],
            ["Spiral Cave", False, [], ['Magic Mirror', 'Hookshot']],
            ["Spiral Cave", False, [], ['Hammer', 'Hookshot']],
            ["Spiral Cave", False, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Spiral Cave", False, ['Progressive Glove', 'Hookshot']],
            ["Spiral Cave", False, ['Flute', 'Magic Mirror']],
            ["Spiral Cave", False, ['Flute', 'Hammer']],
            ["Spiral Cave", True, ['Flute', 'Hookshot']],
            ["Spiral Cave", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Spiral Cave", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Hammer']],
            ["Spiral Cave", True, ['Flute', 'Magic Mirror', 'Hammer']],

            ["Paradox Cave Lower - Far Left", False, []],
            ["Paradox Cave Lower - Far Left", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Far Left", False, [], ['Magic Mirror', 'Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", False, [], ['Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", False, [], ['Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", False, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Far Left", False, ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", False, ['Flute', 'Magic Mirror']],
            ["Paradox Cave Lower - Far Left", False, ['Flute', 'Hammer']],
            ["Paradox Cave Lower - Far Left", True, ['Flute', 'Hookshot', 'Cane of Somaria']],
            ["Paradox Cave Lower - Far Left", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Bomb Upgrade (+5)']],
            ["Paradox Cave Lower - Far Left", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Hammer', 'Progressive Sword', 'Progressive Sword']],
            ["Paradox Cave Lower - Far Left", True, ['Flute', 'Magic Mirror', 'Hammer', 'Fire Rod']],

            ["Paradox Cave Lower - Left", False, []],
            ["Paradox Cave Lower - Left", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Left", False, [], ['Magic Mirror', 'Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Left", False, [], ['Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Left", False, [], ['Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Left", False, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Left", False, ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Left", False, ['Flute', 'Magic Mirror']],
            ["Paradox Cave Lower - Left", False, ['Flute', 'Hammer']],
            ["Paradox Cave Lower - Left", True, ['Flute', 'Hookshot', 'Cane of Somaria']],
            ["Paradox Cave Lower - Left", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Bomb Upgrade (+5)']],
            ["Paradox Cave Lower - Left", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Hammer', 'Progressive Sword', 'Progressive Sword']],
            ["Paradox Cave Lower - Left", True, ['Flute', 'Magic Mirror', 'Hammer', 'Fire Rod']],

            ["Paradox Cave Lower - Middle", False, []],
            ["Paradox Cave Lower - Middle", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Middle", False, [], ['Magic Mirror', 'Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Middle", False, [], ['Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Middle", False, [], ['Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Middle", False, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Middle", False, ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Middle", False, ['Flute', 'Magic Mirror']],
            ["Paradox Cave Lower - Middle", False, ['Flute', 'Hammer']],
            ["Paradox Cave Lower - Middle", True, ['Flute', 'Hookshot', 'Cane of Somaria']],
            ["Paradox Cave Lower - Middle", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Bomb Upgrade (+5)']],
            ["Paradox Cave Lower - Middle", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Hammer', 'Progressive Sword', 'Progressive Sword']],
            ["Paradox Cave Lower - Middle", True, ['Flute', 'Magic Mirror', 'Hammer', 'Fire Rod']],

            ["Paradox Cave Lower - Right", False, []],
            ["Paradox Cave Lower - Right", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Right", False, [], ['Magic Mirror', 'Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Right", False, [], ['Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Right", False, [], ['Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Right", False, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Right", False, ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Right", False, ['Flute', 'Magic Mirror']],
            ["Paradox Cave Lower - Right", False, ['Flute', 'Hammer']],
            ["Paradox Cave Lower - Right", True, ['Flute', 'Hookshot', 'Cane of Somaria']],
            ["Paradox Cave Lower - Right", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Bomb Upgrade (+5)']],
            ["Paradox Cave Lower - Right", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Hammer', 'Progressive Sword', 'Progressive Sword']],
            ["Paradox Cave Lower - Right", True, ['Flute', 'Magic Mirror', 'Hammer', 'Fire Rod']],

            ["Paradox Cave Lower - Far Right", False, []],
            ["Paradox Cave Lower - Far Right", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Far Right", False, [], ['Magic Mirror', 'Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", False, [], ['Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", False, [], ['Hammer', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", False, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Far Right", False, ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", False, ['Flute', 'Magic Mirror']],
            ["Paradox Cave Lower - Far Right", False, ['Flute', 'Hammer']],
            ["Paradox Cave Lower - Far Right", True, ['Flute', 'Hookshot', 'Cane of Somaria']],
            ["Paradox Cave Lower - Far Right", True, ['Progressive Glove', 'Lamp', 'Hookshot', 'Bomb Upgrade (+5)']],
            ["Paradox Cave Lower - Far Right", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Hammer', 'Progressive Sword', 'Progressive Sword']],
            ["Paradox Cave Lower - Far Right", True, ['Flute', 'Magic Mirror', 'Hammer', 'Fire Rod']],

            ["Paradox Cave Upper - Left", False, []],
            ["Paradox Cave Upper - Left", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Upper - Left", False, [], ['Magic Mirror', 'Hammer', 'Hookshot']],
            ["Paradox Cave Upper - Left", False, [], ['Magic Mirror', 'Hookshot']],
            ["Paradox Cave Upper - Left", False, [], ['Hammer', 'Hookshot']],
            ["Paradox Cave Upper - Left", False, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Upper - Left", False, ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Upper - Left", False, ['Flute', 'Magic Mirror']],
            ["Paradox Cave Upper - Left", False, ['Flute', 'Hammer']],
            ["Paradox Cave Upper - Left", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Flute', 'Hookshot']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Lamp', 'Magic Mirror', 'Hammer']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror', 'Hammer']],

            ["Paradox Cave Upper - Right", False, []],
            ["Paradox Cave Upper - Right", False, [], ['Progressive Glove', 'Flute']],
            ["Paradox Cave Upper - Right", False, [], ['Magic Mirror', 'Hammer', 'Hookshot']],
            ["Paradox Cave Upper - Right", False, [], ['Magic Mirror', 'Hookshot']],
            ["Paradox Cave Upper - Right", False, [], ['Hammer', 'Hookshot']],
            ["Paradox Cave Upper - Right", False, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Upper - Right", False, ['Progressive Glove', 'Hookshot']],
            ["Paradox Cave Upper - Right", False, ['Flute', 'Magic Mirror']],
            ["Paradox Cave Upper - Right", False, ['Flute', 'Hammer']],
            ["Paradox Cave Upper - Right", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Flute', 'Hookshot']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Lamp', 'Magic Mirror', 'Hammer']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror', 'Hammer']],
        ])

    def testWestDarkWorldDeathMountain(self):
        self.run_location_tests([
            ["Spike Cave", False, []],
            ["Spike Cave", False, [], ['Progressive Glove']],
            ["Spike Cave", False, [], ['Moon Pearl']],
            ["Spike Cave", False, [], ['Hammer']],
            ["Spike Cave", False, [], ['Cape', 'Cane of Byrna']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cape']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],
        ])

    def testEastDarkWorldDeathMountain(self):
        self.run_location_tests([
            ["Superbunny Cave - Top", False, []],
            ["Superbunny Cave - Top", False, [], ['Progressive Glove']],
            ["Superbunny Cave - Top", False, [], ['Moon Pearl']],
            ["Superbunny Cave - Top", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Superbunny Cave - Top", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Flute']],
            ["Superbunny Cave - Top", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
            ["Superbunny Cave - Top", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Lamp']],

            ["Superbunny Cave - Bottom", False, []],
            ["Superbunny Cave - Bottom", False, [], ['Progressive Glove']],
            ["Superbunny Cave - Bottom", False, [], ['Moon Pearl']],
            ["Superbunny Cave - Bottom", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Superbunny Cave - Bottom", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Flute']],
            ["Superbunny Cave - Bottom", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
            ["Superbunny Cave - Bottom", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Lamp']],

            ["Hookshot Cave - Bottom Right", False, []],
            ["Hookshot Cave - Bottom Right", False, [], ['Progressive Glove']],
            ["Hookshot Cave - Bottom Right", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Flute', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Magic Mirror', 'Hammer', 'Lamp', 'Pegasus Boots']],

            ["Hookshot Cave - Bottom Left", False, []],
            ["Hookshot Cave - Bottom Left", False, [], ['Progressive Glove']],
            ["Hookshot Cave - Bottom Left", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Bottom Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Hookshot Cave - Bottom Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],

            ["Hookshot Cave - Top Left", False, []],
            ["Hookshot Cave - Top Left", False, [], ['Progressive Glove']],
            ["Hookshot Cave - Top Left", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Top Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Hookshot Cave - Top Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],

            ["Hookshot Cave - Top Right", False, []],
            ["Hookshot Cave - Top Right", False, [], ['Progressive Glove']],
            ["Hookshot Cave - Top Right", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Top Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Hookshot Cave - Top Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
        ])
