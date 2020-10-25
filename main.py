def P1_B_R():
    global AngleR
    for index in range(50):
        AngleR += 1
        pins.servo_write_pin(AnalogPin.P1, AngleR)
        basic.pause(Temp)
def P13_B_R():
    global AngleR
    for index2 in range(50):
        AngleR += 1
        pins.servo_write_pin(AnalogPin.P13, AngleR)
        basic.pause(Temp)
def P12_H_R():
    global AngleR
    for index3 in range(50):
        AngleR += -1
        pins.servo_write_pin(AnalogPin.P12, AngleR)
        basic.pause(Temp)
def _2VMH():
    pins.servo_write_pin(AnalogPin.P0, 90)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 98)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 107)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 116)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 125)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 134)
    basic.pause(40)
def P1_AV():
    P0_H_V()
    P1_H_R()
    P0_B_V()
    P1_B_R()
    P1_B_R()
    P0_H_V()
    P1_H_R()
    P0_B_V()
def _2RM1():
    pins.servo_write_pin(AnalogPin.P1, 90)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 80)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 70)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 60)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 50)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 45)
    basic.pause(40)
def P2_B_R():
    global AngleR
    for index4 in range(50):
        AngleR += 1
        pins.servo_write_pin(AnalogPin.P2, AngleR)
        basic.pause(Temp)
def _2():
    _2VMH()
    _2RM1()
    _2VHM()
    _2VMB()
    _2R1M()
    _2RM2()
    _2VBM()
    _2VMH()
    _2R2M()
    _2VHM()

def on_button_pressed_a():
    P1_AV()
    P1_AR()
input.on_button_pressed(Button.A, on_button_pressed_a)

def P13_H_R():
    global AngleR
    for index5 in range(50):
        AngleR += -1
        pins.servo_write_pin(AnalogPin.P13, AngleR)
        basic.pause(AngleR)
def _2RM2():
    pins.servo_write_pin(AnalogPin.P1, 90)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 100)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 110)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 120)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 130)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 140)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 145)
    basic.pause(40)
def P1_H_R():
    global AngleR
    for index6 in range(50):
        AngleR += -1
        pins.servo_write_pin(AnalogPin.P1, AngleR)
        basic.pause(Temp)
def P13_AR():
    P0_H_V()
    P1_B_R()
    P0_B_V()
    P1_H_R()
    P1_H_R()
    P0_H_V()
    P1_B_R()
    P0_B_V()
def _2VHM():
    pins.servo_write_pin(AnalogPin.P0, 134)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 125)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 116)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 107)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 98)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 90)
    basic.pause(40)
def P1_AR():
    P0_H_V()
    P1_B_R()
    P0_B_V()
    P1_H_R()
    P1_H_R()
    P0_H_V()
    P1_B_R()
    P0_B_V()
def P8_H_V():
    global AngleV
    for index7 in range(50):
        AngleV += -1
        pins.servo_write_pin(AnalogPin.P8, AngleV)
        basic.pause(Temp)
def P0_H_V():
    global AngleV
    for index8 in range(50):
        AngleV += -1
        pins.servo_write_pin(AnalogPin.P0, AngleV)
        basic.pause(Temp)
def P0_B_V():
    global AngleV
    for index9 in range(50):
        AngleV += 1
        pins.servo_write_pin(AnalogPin.P0, AngleV)
        basic.pause(Temp)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def _2R2M():
    pins.servo_write_pin(AnalogPin.P1, 145)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 140)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 130)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 120)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 110)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 100)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 90)
    basic.pause(40)
def _2VMB():
    pins.servo_write_pin(AnalogPin.P0, 90)
    basic.pause(50)
    pins.servo_write_pin(AnalogPin.P0, 81)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 72)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 64)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 55)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 47)
    basic.pause(40)
def _2VBM():
    pins.servo_write_pin(AnalogPin.P0, 47)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 55)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 64)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 72)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 81)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P0, 90)
    basic.pause(40)
def P8_B_V():
    global AngleV
    for index10 in range(50):
        AngleV += 1
        pins.servo_write_pin(AnalogPin.P8, AngleV)
        basic.pause(Temp)
def P2_H_R():
    global AngleR
    for index11 in range(50):
        AngleR += -1
        pins.servo_write_pin(AnalogPin.P2, AngleR)
        basic.pause(Temp)
def _2R1M():
    pins.servo_write_pin(AnalogPin.P1, 45)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 50)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 60)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 70)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 80)
    basic.pause(40)
    pins.servo_write_pin(AnalogPin.P1, 90)
    basic.pause(40)
def P12_B_R():
    global AngleR
    for index12 in range(50):
        AngleR += 1
        pins.servo_write_pin(AnalogPin.P12, AngleR)
        basic.pause(Temp)
Temp = 0
AngleR = 0
AngleV = 0
pins.servo_write_pin(AnalogPin.P0, 90)
basic.pause(100)
pins.servo_write_pin(AnalogPin.P1, 90)
basic.pause(100)
pins.servo_write_pin(AnalogPin.P2, 90)
basic.pause(100)
pins.servo_write_pin(AnalogPin.P8, 90)
basic.pause(100)
pins.servo_write_pin(AnalogPin.P12, 90)
basic.pause(100)
pins.servo_write_pin(AnalogPin.P13, 90)
basic.pause(100)
AngleV = 90
AngleR = 90
Temp = 20

def on_forever():
    basic.show_string("" + str((AngleR)))
basic.forever(on_forever)
