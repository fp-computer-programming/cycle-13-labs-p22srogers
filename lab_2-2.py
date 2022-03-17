# Author: SMR (AMDG) 03/04/22
def build_car(a,b,c,d):
    wheels=a
    axels=b
    doors=c
    color=d
    print("The car has {0} wheels, {1} axels, {2} doors, and is the color {3}".format(wheels,axels,doors,color))
wheels = input("How many wheels does the car have?")
axels = input("How many axels does the car have?")
doors = input("How many doors does the car have?")
color = input("What color is the car?")
build_car(wheels,axels,doors,color)