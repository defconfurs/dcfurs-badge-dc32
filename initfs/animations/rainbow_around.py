class rainbow_around:
    def __init__(self, badge):
        self.badge = badge
        self.offset = 0.0
    
    def update(self):
        self.offset += 0.5
        for i in range(len(self.badge.disp.clockwise)):
            self.badge.disp.clockwise[i].hsv(self.badge.pallet[int(1024*((i+self.offset)/60))&0x3FF][0], 1.0, 100)
        for i in range(len(self.badge.disp.left_eye)):
            self.badge.disp.left_eye[i].hsv(self.badge.pallet[int(1024*((i+self.offset)/46))&0x3FF][0], 1.0, 200)
        for i in range(len(self.badge.disp.right_eye)):
            self.badge.disp.right_eye[i].hsv(self.badge.pallet[int(1024*((i+self.offset)/46))&0x3FF][0], 1.0, 200)
