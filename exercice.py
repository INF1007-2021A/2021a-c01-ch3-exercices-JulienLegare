#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def square_root(a: float) -> float:
    num1 = math.sqrt(a)
    return num1


def square(a: float) -> float:
    num2 = a**2
    return num2


def average(a: float, b: float, c: float) -> float:
    num3 = (a+b+c)/3
    return num3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    Num = (angle_degs) + (angle_mins/60) + (angle_secs/3600)
    Deg = Num*(math.pi)/180
    return Deg


def to_degrees(angle_rads: float) -> tuple:
    Num1 = angle_rads * 180/(math.pi)
    Num2 = int(Num1)
    Dec = Num1-Num2
    Min1 = Dec * 60
    Min2 = int(Min1)
    Min3 = Min1 - Min2
    Sec1 = Min3 * 60
    return Num2, Min2, Sec1


def to_celsius(temperature: float) -> float:
    TempC = (temperature-32)/1.8
    return TempC


def to_farenheit(temperature: float) -> float:
    TempF = temperature * 1.8 + 32
    return TempF


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
