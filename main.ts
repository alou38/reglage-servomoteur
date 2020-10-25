function droite90 () {
    RepeterV += 15
    Repeter += 8
    P0_H_V()
    P13_hor_R()
    P1_hor_R()
    P0_B_V()
    basic.pause(20)
    P0_B_V()
    P2_hor_R()
    P12_hor_R()
    P13_antihor_R()
    P1_antihor_R()
    P8_B_V()
    basic.pause(20)
    P8_B_V()
    P12_anti_R()
    P2_antihor_R()
    P8_H_V()
    basic.pause(20)
    pins.servoWritePin(AnalogPin.P0, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P13, 90)
    pins.servoWritePin(AnalogPin.P12, 90)
    pins.servoWritePin(AnalogPin.P8, 90)
}
function P12_hor_R () {
    for (let index = 0; index < Repeter; index++) {
        AngleR3 += -1
        pins.servoWritePin(AnalogPin.P12, AngleR3)
        basic.pause(Temp)
    }
}
function AV () {
    P8_H_V()
    P2_hor_R()
    P12_anti_R()
    P8_B_V()
    P8_B_V()
    P2_antihor_R()
    P2_antihor_R()
    P12_hor_R()
    P12_hor_R()
    P8_H_V()
    P8_H_V()
    P2_hor_R()
    P12_anti_R()
    P8_B_V()
    P0_H_V()
    P1_hor_R()
    P13_antihor_R()
    P0_B_V()
    P0_B_V()
    P1_antihor_R()
    P1_antihor_R()
    P13_hor_R()
    P13_hor_R()
    P0_H_V()
    P0_H_V()
    P1_hor_R()
    P13_antihor_R()
    P0_B_V()
    pins.servoWritePin(AnalogPin.P0, 90)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P13, 90)
    pins.servoWritePin(AnalogPin.P12, 90)
    pins.servoWritePin(AnalogPin.P8, 90)
}
function P2_hor_R () {
    for (let index = 0; index < Repeter; index++) {
        AngleR2 += -1
        pins.servoWritePin(AnalogPin.P2, AngleR2)
        basic.pause(Temp)
    }
}
function P13_hor_R () {
    for (let index = 0; index < Repeter; index++) {
        AngleR4 += -1
        pins.servoWritePin(AnalogPin.P13, AngleR4)
        basic.pause(Temp)
    }
}
function gauche90 () {
    RepeterV += 15
    Repeter += 8
    P0_H_V()
    P13_antihor_R()
    P1_antihor_R()
    P0_B_V()
    basic.pause(20)
    P0_B_V()
    P2_antihor_R()
    P12_anti_R()
    P13_hor_R()
    P1_hor_R()
    P8_B_V()
    basic.pause(20)
    P8_B_V()
    P12_hor_R()
    P2_hor_R()
    P8_H_V()
    basic.pause(20)
    pins.servoWritePin(AnalogPin.P0, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P13, 90)
    pins.servoWritePin(AnalogPin.P12, 90)
    pins.servoWritePin(AnalogPin.P8, 90)
}
function P12_anti_R () {
    for (let index = 0; index < Repeter; index++) {
        AngleR3 += 1
        pins.servoWritePin(AnalogPin.P12, AngleR3)
        basic.pause(Temp)
    }
}
function P8_H_V () {
    for (let index = 0; index < RepeterV; index++) {
        AngleV += 1
        pins.servoWritePin(AnalogPin.P8, AngleV)
        basic.pause(Temp)
    }
}
function P0_H_V () {
    for (let index = 0; index < RepeterV; index++) {
        AngleV += -1
        pins.servoWritePin(AnalogPin.P0, AngleV)
        basic.pause(Temp)
    }
}
function P1_hor_R () {
    for (let index = 0; index < Repeter; index++) {
        AngleR1 += -1
        pins.servoWritePin(AnalogPin.P1, AngleR1)
        basic.pause(Temp)
    }
}
function P0_B_V () {
    for (let index = 0; index < RepeterV; index++) {
        AngleV += 1
        pins.servoWritePin(AnalogPin.P0, AngleV)
        basic.pause(Temp)
    }
}
function P13_antihor_R () {
    for (let index = 0; index < Repeter; index++) {
        AngleR4 += 1
        pins.servoWritePin(AnalogPin.P13, AngleR4)
        basic.pause(Temp)
    }
}
function P8_B_V () {
    for (let index = 0; index < RepeterV; index++) {
        AngleV += -1
        pins.servoWritePin(AnalogPin.P8, AngleV)
        basic.pause(Temp)
    }
}
function P2_antihor_R () {
    for (let index = 0; index < Repeter; index++) {
        AngleR2 += 1
        pins.servoWritePin(AnalogPin.P2, AngleR2)
        basic.pause(Temp)
    }
}
function P1_antihor_R () {
    for (let index = 0; index < Repeter; index++) {
        AngleR1 += 1
        pins.servoWritePin(AnalogPin.P1, AngleR1)
        basic.pause(Temp)
    }
}
function AR () {
    P0_B_V()
    P13_antihor_R()
    P1_hor_R()
    P0_H_V()
    P0_H_V()
    P13_hor_R()
    P13_hor_R()
    P1_antihor_R()
    P1_antihor_R()
    P0_B_V()
    P0_B_V()
    P13_antihor_R()
    P1_hor_R()
    P0_H_V()
    P8_B_V()
    P12_anti_R()
    P2_hor_R()
    P8_H_V()
    P8_H_V()
    P12_hor_R()
    P12_hor_R()
    P2_antihor_R()
    P2_antihor_R()
    P8_B_V()
    P8_B_V()
    P12_anti_R()
    P2_hor_R()
    P8_H_V()
    pins.servoWritePin(AnalogPin.P0, 90)
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P13, 90)
    pins.servoWritePin(AnalogPin.P12, 90)
    pins.servoWritePin(AnalogPin.P8, 90)
}
let Temp = 0
let AngleR4 = 0
let AngleR3 = 0
let AngleR2 = 0
let AngleR1 = 0
let AngleV = 0
let RepeterV = 0
let Repeter = 0
pins.servoWritePin(AnalogPin.P0, 90)
basic.pause(100)
pins.servoWritePin(AnalogPin.P1, 90)
basic.pause(100)
pins.servoWritePin(AnalogPin.P2, 90)
basic.pause(100)
pins.servoWritePin(AnalogPin.P8, 90)
basic.pause(100)
pins.servoWritePin(AnalogPin.P12, 90)
basic.pause(100)
pins.servoWritePin(AnalogPin.P13, 90)
basic.pause(100)
Repeter = 40
RepeterV += 15
AngleV = 90
AngleR1 = 90
AngleR2 = 90
AngleR3 = 90
AngleR4 = 90
Temp = 5
basic.forever(function () {
    while (input.buttonIsPressed(Button.A)) {
        for (let index = 0; index < 1; index++) {
            droite90()
            basic.pause(1)
        }
    }
    while (input.buttonIsPressed(Button.B)) {
        for (let index = 0; index < 1; index++) {
            gauche90()
            basic.pause(1)
        }
    }
})
