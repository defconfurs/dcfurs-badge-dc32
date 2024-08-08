
import array
import time
from random import random
from is31fl3737 import rgb_value

class chasers:
    def __init__(self, badge):
        self.badge = badge
        self.framebuf = self.badge.disp.clockwise

        self.traces = []
        self.last = time.ticks_ms()
        self.next = self.last + int(random() * 1000)
        self.max_traces = 3
        self.decay = 0.95
        self.brightness = 255
        self.buffer = [rgb_value() for i in range(len(self.framebuf))]
        self.eye_offset = 0.0

    def update(self):
        if time.ticks_ms() > self.next:
            colour = self.badge.pallet[int(1024*random())][0]
            speed = (0.5-((random()-0.5)**2))*1.2*(1 if (random()>0.5) else 0)

            self.traces.append([
                colour,                                     # colour
                speed,                                      # speed
                float(random()*len(self.framebuf)),         # position
                (random()*0.07),                            # life_rate
                1.0,                                        # life
                array.array("f", [0]*len(self.framebuf))]   # record
            )
            self.next = time.ticks_ms() + int(random()*3500)
        
        for trace in self.traces:
            if trace[4] <= 0:
                self.traces.remove(trace)

        for i in range(len(self.framebuf)):
            self.buffer[i].r = 0.0
            self.buffer[i].g = 0.0
            self.buffer[i].b = 0.0

        for trace in self.traces:
            trace[4] -= trace[3]
            if trace[4] < 0:
                trace[4] = 0
            if trace[4] > 0.1:
                end_gain = 1.0
            else:
                end_gain = trace[4] * 10.0
            for i in range(len(self.framebuf)):
                trace[5][i] *= (self.decay * end_gain)
            
            trace[2] += trace[1]
            trace[5][int(trace[2])%len(self.framebuf)] = self.brightness * end_gain

            for i in range(len(self.framebuf)):
                r,g,b = self.buffer[0].hsv(trace[0],1.0,trace[5][i],1.0,ret_value=True)
                self.buffer[i].r += r
                self.buffer[i].g += g
                self.buffer[i].b += b

        for i in range(len(self.framebuf)):
            if self.buffer[i].r > self.brightness: self.buffer[i].r = self.brightness
            if self.buffer[i].g > self.brightness: self.buffer[i].g = self.brightness
            if self.buffer[i].b > self.brightness: self.buffer[i].b = self.brightness
            if self.buffer[i].r < 0: self.buffer[i].r = 0
            if self.buffer[i].g < 0: self.buffer[i].g = 0
            if self.buffer[i].b < 0: self.buffer[i].b = 0
            self.framebuf[i].r = int(self.buffer[i].r)
            self.framebuf[i].g = int(self.buffer[i].g)
            self.framebuf[i].b = int(self.buffer[i].b)
            #print(f"{self.buffer[i].r},{self.buffer[i].g},{self.buffer[i].b}")
            #print(self.framebuf[i])

        self.eye_offset += 0.5
        for i in range(len(self.badge.disp.left_eye)):
            self.badge.disp.left_eye[i].hsv((i+self.eye_offset)/len(self.framebuf), 1.0, self.brightness)
        for i in range(len(self.badge.disp.right_eye)):
            self.badge.disp.right_eye[i].hsv((i+self.eye_offset)/len(self.framebuf), 1.0, self.brightness)
