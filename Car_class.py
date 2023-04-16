import numpy as np
def dot(a, b):
    sumq = 0
    for i in a:
        for j in b:
            sumq += i+j
    return sumq


class Car:
    def __init__(self, make, model, year, speed, coordinates, direction):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        self.coordinates = coordinates
        self.direction = direction
        self.velocity = (x*self.speed for x in direction)

    def accelerate(self, speed_increment):
        self.speed += speed_increment

    def brake(self, speed_decrement):
        self.speed -= speed_decrement

    def move(self, dt):
        self.coordinates[0] += self.speed * dt * (self.direction[0])
        self.coordinates[1] += self.speed * dt * (self.direction[1])
        self.coordinates[2] += self.speed * dt * (self.direction[2])

    def position(self):
        return [self.coordinates[0], self.coordinates[1], self.coordinates[2]]

    def distance(self, car2):
        return np.linalg.norm(x-y for x in self.position() for y in car2.position())

    def iscollide(self, car2):
        return self.distance(car2) == 0

    def time_to_collision(self, car2):
        disp_vectr = (x-y for x in self.position() for y in car2.position())
        rel_vel_vect = (x-y for x in self.velocity for y in car2.velocity)
        a = dot(rel_vel_vect, rel_vel_vect)
        b = dot(rel_vel_vect, disp_vectr)
        c = dot(disp_vectr, disp_vectr)
        if a == 0:
            return None
        d = b ** 2 - 4 * a * c
        if d < 0:
            return None
        t1 = (-b - np.sqrt(d)) / (2 * a)
        t2 = (-b + np.sqrt(d)) / (2 * a)
        if t1 > 0:
            return t1
        elif t2 > 0:
            return t2
        else:
            return None
