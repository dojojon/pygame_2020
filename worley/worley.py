import pgzrun
import math
import pygame
import random

WIDTH=600
HEIGHT=480

def distance_between_points(p1, p2):
    d = (p2[0]-p1[0])**2 +  (p2[1]-p1[1])**2
    d = math.sqrt(d)
    return d

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

MAX_DISTANCE = distance_between_points((0,0), (WIDTH, HEIGHT))

points = [ ]
for n in range(0, 10):
    points.append((random.randrange(0, WIDTH), random.randrange(0, HEIGHT)))

pixels = []
for p in range(0, WIDTH * HEIGHT):
    pixels.append({"c":(100, 100, 0)} )

def update():
    n = 0
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            p = x + y * WIDTH        
            distances = [0]* len(points)
            for i in range(0, len(points)):
                distances[i] = distance_between_points((x, y), points[i])
            distances.sort()
            # pixels[p]["c"] = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
            noise = translate(distances[n], 0, MAX_DISTANCE, 0, 255)
            pixels[p]["c"] = (noise, noise, noise)
    pass


def draw():
    screen.clear()
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            p = x + y * WIDTH
            c = pixels[p]["c"]
            screen.surface.set_at((x, y), c)

    for p in points:
        screen.surface.set_at(p, (255, 0,0 ))


pgzrun.go()