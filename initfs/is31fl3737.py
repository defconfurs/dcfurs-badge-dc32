from machine import I2C, Pin
from micropython import const
import math
import array

class rgb_value(object):
    def __init__(self, r=0, g=0, b=0, h=0, s=0, v=0):
        self.value = array.array("B", [0]*3)
        self.hsv_value = array.array("f", [0]*3)
        if h or s or v:
            self.hsv(h,s,v)
        else:
            self.value[0] = r
            self.value[1] = g
            self.value[2] = b
        self.hsv_value[0] = h
        self.hsv_value[1] = s
        self.hsv_value[2] = v
    
    @property 
    def r(self): return self.value[0]
    @property
    def g(self): return self.value[1]
    @property
    def b(self): return self.value[2]
    @r.setter
    def r(self, value):
        self.value[0] = int(value)
    @g.setter
    def g(self, value):
        self.value[1] = int(value)
    @b.setter
    def b(self, value):
        self.value[2] = int(value)

    @property 
    def h(self): return self.hsv_value[0]
    @property 
    def s(self): return self.hsv_value[1]
    @property 
    def v(self): return self.hsv_value[2]
    @h.setter
    def h(self, value):
        self.hsv_value[0] = value
    @s.setter
    def s(self, value):
        self.hsv_value[1] = value
    @v.setter
    def v(self, value):
        self.hsv_value[2] = value

    def __repr__(self):
        return f"<RGB: {self.value[0]}, {self.value[1]}, {self.value[2]}>"

    def set(self, r, g, b):
        self.value[0] = r
        self.value[1] = g
        self.value[2] = b

    def copy(self, other):
        self.value[0] = other.value[0]
        self.value[1] = other.value[1]
        self.value[2] = other.value[2]

    def hsv(self, hue, sat, val, debug=False, ret_value=False):
        self.hsv_value[0] = hue
        self.hsv_value[1] = sat
        self.hsv_value[2] = val
        hue = (int(hue*256)&0xFF)/256
        i = int(((hue) * 6.0) % 6)
        f = ((hue) * 6.0) - i
        v = (val)
        p = (val) * (1.0 - (sat))
        q = (val) * (1.0 - f * (sat))
        t = (val) * (1.0 - (1.0 - f) * (sat))
        i = int(i)
        if   (i == 0): r = v; g = t; b = p
        elif (i == 1): r = q; g = v; b = p
        elif (i == 2): r = p; g = v; b = t
        elif (i == 3): r = p; g = q; b = v
        elif (i == 4): r = t; g = p; b = v
        elif (i == 5): r = v; g = p; b = q
        #if debug: print(f"{hue}/{sat}/{val} - i{i},f{f},v{v},p{p},q{q},t{t} - {r},{g},{b}")
        if ret_value:
            return (int(r), int(g), int(b))
        else:
            self.value[0] = int(r)
            self.value[1] = int(g)
            self.value[2] = int(b)


class is31fl3737(object):
    I2C_ADDR = 80

    REF_CONF      = const(0)
    REG_PAGE_SEL  = const(0xFD)
    REG_PAGE_LOCK = const(0xFE)
    REG_INT_MASK  = const(0xF0)
    REG_INT_STAT  = const(0xF1)

    # Page 0
    REG_LEDONOFF = const(0x0000) # ON or OFF state control for each LED. Write only.
    REG_LEDOPEN  = const(0x0018) # Open state for each LED. Read only.
    REG_LEDSHORT = const(0x0030) # Short state for each LED. Read only.

    # Registers in Page 1.
    REG_LEDPWM = const(0x0100) # PWM duty for each LED. Write only.

    # Registers in Page 2.
    REG_LEDABM = const(0x0200) # Auto breath mode for each LED. Write only.

    # Registers in Page 3.
    REG_CR    = const(0x0300) # Configuration Register. Write only.
    REG_GCC   = const(0x0301) # Global Current Control register. Write only.
    REG_ABM1  = const(0x0302) # Auto breath control register for ABM-1. Write only.
    REG_ABM2  = const(0x0306) # Auto breath control register for ABM-2. Write only.
    REG_ABM3  = const(0x030A) # Auto breath control register for ABM-3. Write only.
    REG_TUR   = const(0x030E) # Time update register. Write only.
    REG_SWPUR = const(0x030F) # SWy Pull-Up Resistor selection register. Write only.
    REG_CSPDR = const(0x0310) # CSx Pull-Down Resistor selection register. Write only.
    REG_RESET = const(0x0311) # Reset register. Read only.

    leds        = [rgb_value() for i in range(49)]
    left_ear    = [leds[12],leds[11],leds[10],leds[9],leds[8],leds[7]]
    right_ear   = [leds[6],leds[5],leds[4],leds[3],leds[2],leds[1]]
    left_tuft   = [leds[23],leds[24],leds[21],leds[22],leds[20]]
    right_tuft  = [leds[37],leds[38],leds[40],leds[39],leds[41]]
    left_cheek  = [leds[16],leds[15],leds[14],leds[13]]
    right_cheek = [leds[45],leds[46],leds[47],leds[48]]
    cheeks      = left_cheek + right_cheek
    nose        = [leds[36],leds[25],leds[35],leds[26],leds[34],leds[27],leds[33],leds[28],leds[32],leds[29],leds[31],leds[30]]
    left_eye    = [leds[18],leds[19],leds[17]]
    right_eye   = [leds[43],leds[42],leds[44]]

    clockwise   = right_ear + right_tuft + right_cheek + [leds[30],leds[31]] +  [i for i in reversed(left_cheek + left_tuft + left_ear)]
    downward = [leds[12],leds[6],leds[11],leds[5],leds[10],leds[4],leds[9],leds[3],leds[8],leds[2],leds[7],leds[1],
                leds[23],leds[37],leds[24],leds[38],leds[18],leds[43],leds[17],leds[44],leds[21],leds[40],leds[22],leds[39],leds[19],leds[42],leds[20],leds[41],
                leds[36],leds[25],leds[35],leds[26],leds[34],leds[27],leds[16],leds[45],leds[15],leds[46],leds[14],leds[47],leds[13],leds[48],leds[33],leds[28],
                leds[32],leds[29],leds[31],leds[30]]

    def __init__(self):
        self.i2c = I2C(0, scl=Pin(1), sda=Pin(0))
        self.sdb = Pin(3, Pin.OUT)
        self.leds_raw = bytearray(256)
        self.brightness = 256
        
        self.power_on()
        self.init()

    def power_on(self):
        self.sdb(1)
    def power_off(self):
        self.sdb(0)

    def set_page(self, page_num:int):
        self.i2c.writeto_mem(self.I2C_ADDR, self.REG_PAGE_LOCK, b"\xC5")
        self.i2c.writeto_mem(self.I2C_ADDR, self.REG_PAGE_SEL, bytes([page_num & 0x3]))
    
    def read_paged_reg(self, addr):
        self.set_page(addr>>8)
        return self.i2c.readfrom_mem(self.I2C_ADDR, addr&0xFF, 1)
    
    def write_paged_reg(self, addr, value):
        self.set_page(addr>>8)
        self.i2c.writeto_mem(self.I2C_ADDR, addr&0xFF, bytes([value & 0xFF]))

    def init(self):
        # Read reset register to reset device.
        self.read_paged_reg(self.REG_RESET)
        # Clear software reset in configuration register.
        self.write_paged_reg(self.REG_CR, 0x01) # SSD bit
        # Clear state of all LEDs in internal buffer and sync buffer to device.
        self.set_page(0)
        self.i2c.writeto_mem(self.I2C_ADDR, 0, bytes([0xFF]*0x18)) # turn on all the LEDs
        self.set_page(2)
        self.i2c.writeto_mem(self.I2C_ADDR, 0, bytes([0x00]*0xBF)) # turn off auto breath mode

        for i in range(256):
            self.leds_raw[i] = 0
        self.update()
        self.set_page(3)
        self.i2c.writeto_mem(self.I2C_ADDR, 0, bytes([1]))
        self.i2c.writeto_mem(self.I2C_ADDR, 1, bytes([50]))

    def update(self):
        for i in range(48):
            self.set_led_raw(i, self.leds[i+1]) # change from last year - D<x> = led<x> and there's no D0
        self.set_page(1)
        self.i2c.writeto_mem(self.I2C_ADDR,   0, self.leds_raw[  0:127])
        self.i2c.writeto_mem(self.I2C_ADDR, 128, self.leds_raw[128:255])

    def set_led_raw(self, led_num, led):
        addr = int(led_num % 12)
        if addr > 5: addr += 2
        addr += (led_num // 12)*0x30
        self.leds_raw[(addr+0x00)&0xFF] = led.value[2]*self.brightness//256
        self.leds_raw[(addr+0x10)&0xFF] = led.value[1]*self.brightness//256
        self.leds_raw[(addr+0x20)&0xFF] = led.value[0]*self.brightness//256


    def clear(self):
        for i in range(49):
            self.leds[i].set(0, 0, 0)
        self.update()
    
