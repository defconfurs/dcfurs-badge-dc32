class test_pattern:
    def __init__(self, badge):
        self.badge = badge
        self.offset = 0.0
        self.test_pattern = [4288554444, 4201042, 2195458, 3426361, 161, 148228, 4235264, 69632]

    def update(self):
        self.offset += 0.1
        if self.offset > 32.0: self.offset = 0.0
        for i in range(len(self.badge.disp.downward)):
            self.badge.disp.downward[i].r = 0.0
            self.badge.disp.downward[i].g = 0.0
            self.badge.disp.downward[i].b = 0.0
        if (self.test_pattern[0] >> int(self.offset)) & 1: self.badge.disp.downward[44].value[2] = 1.0
        if (self.test_pattern[1] >> int(self.offset)) & 1: self.badge.disp.downward[42].value[2] = 1.0
        if (self.test_pattern[2] >> int(self.offset)) & 1: self.badge.disp.downward[30].value[2] = 1.0
        if (self.test_pattern[3] >> int(self.offset)) & 1: self.badge.disp.downward[28].value[2] = 1.0
        if (self.test_pattern[4] >> int(self.offset)) & 1: self.badge.disp.downward[29].value[2] = 1.0
        if (self.test_pattern[5] >> int(self.offset)) & 1: self.badge.disp.downward[31].value[2] = 1.0
        if (self.test_pattern[6] >> int(self.offset)) & 1: self.badge.disp.downward[43].value[2] = 1.0
        if (self.test_pattern[7] >> int(self.offset)) & 1: self.badge.disp.downward[45].value[2] = 1.0
