#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

# Inicialización del EV3
ev3 = EV3Brick()

# Motores conectados a los puertos A Y D
mi = Motor(Port.A)
md = Motor(Port.D)

# Configuración de la base de conducción
robot = DriveBase(mi, md, 55.5, 104)

# Sensor de color conectado al puerto S4
color_sensor = ColorSensor(Port.S4)

# Variables para contar las unidades de distancia
c1 = 0
c2 = 0

# Avanzar hasta encontrar el primer color diferente del blanco
while color_sensor.color() == Color.WHITE:
    robot.straight(1)

# Contar la distancia del primer tramo de color
while color_sensor.color() != Color.WHITE:
    robot.straight(1)
    c1 += 1
ev3.screen.print(c1)  # Imprimir c1 en la pantalla del EV3

# Avanzar hasta encontrar el segundo color diferente del blanco
while color_sensor.color() == Color.WHITE:
    robot.straight(1)

# Contar la distancia del segundo tramo de color
while color_sensor.color() != Color.WHITE:
    robot.straight(1)
    c2 += 1
ev3.screen.print(c2)  # Imprimir c2 en la pantalla del EV3

# Bucle principal
while True:
    c3 = 0
    # Avanzar hasta encontrar un color diferente del blanco
    while color_sensor.color() == Color.WHITE:
        robot.straight(1)

    # Contar la distancia del tramo actual
    while color_sensor.color() != Color.WHITE:
        robot.straight(1)
        c3 += 1
    
    # Comparar la distancia del tramo actual con c1 y c2
    if c2 - 2 <= c3 <= c2 + 2:
        ev3.screen.print("1")  # Imprimir 1 en la pantalla del EV3
    elif c1 - 2 <= c3 <= c1 + 2:
        ev3.screen.print("0")  # Imprimir 0 en la pantalla del EV3