class test_pattern:
    def __init__(self, badge):
        self.badge = badge
        self.offset = 0.0
        self.test_pattern = [4288554444, 4201042, 2195458, 3426361, 161, 148228, 4235264, 69632]

    def update(self):
        self.offset += 0.1
        if self.offset > 32.0: self.offset = 0.0
        for i in range(len(self.badge.disp.downward)):
            self.badge.disp.downward[i].set(0, 0, 0)

        mask = 1 << int(self.offset)
        if self.test_pattern[0] & mask: self.badge.disp.downward[44].b = 255
        if self.test_pattern[1] & mask: self.badge.disp.downward[42].b = 255
        if self.test_pattern[2] & mask: self.badge.disp.downward[30].b = 255
        if self.test_pattern[3] & mask: self.badge.disp.downward[28].b = 255
        if self.test_pattern[4] & mask: self.badge.disp.downward[29].b = 255
        if self.test_pattern[5] & mask: self.badge.disp.downward[31].b = 255
        if self.test_pattern[6] & mask: self.badge.disp.downward[43].b = 255
        if self.test_pattern[7] & mask: self.badge.disp.downward[45].b = 255



[4288554444,  4201042,  2195458,  3426361,  161,  148228, 4235264, 69632]
[0xFF9E25CC, 0x401A52, 0x218002, 0x344839, 0xA1, 0x24304, 0x40A000, 0x11000]