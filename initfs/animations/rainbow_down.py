class rainbow_down:
    def __init__(self, badge):
        self.badge = badge
        self.offset = 0.0
    
    def update(self):
        self.offset -= 0.5
        for i in range(len(self.badge.disp.downward)):
            self.badge.disp.downward[i].hsv(self.badge.pallet[int(1024*(i+self.offset)/100)&0x3FF][0], 1.0, 100)
