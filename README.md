# WEB 3.0 recruitment task

The project contains two files one is Car_class.py and main.py.



```markdown
# Car Class

This is a Python program that defines a Car class and some methods to manipulate and compare car objects.

## Description

The Car class has the following attributes:

- make: the manufacturer of the car
- model: the model name of the car
- year: the year of production of the car
- speed: the current speed of the car
- coordinates: a list of three numbers representing the x, y, and z coordinates of the car
- direction: a list of three numbers representing the unit vector of the direction of the car
- velocity: a list of three numbers representing the velocity vector of the car

The Car class has the following methods:

- __init__: the constructor method that initializes the attributes of the car object
- accelerate: a method that increases the speed of the car by a given amount
- brake: a method that decreases the speed of the car by a given amount
- move: a method that updates the coordinates of the car based on its speed, direction, and a given time interval
- position: a method that returns a numpy array of the coordinates of the car
-iscollide: a method that takes another Car object as input and returns true if cars collide
-time-to-collision: method that takes another Car object as input and returns time taken for cars to collide.
- distance: a method that takes another car object as an argument and returns the Euclidean distance between them



## Description


To use this program, you need to import numpy as np and then create some car objects with different attributes. For example:


import numpy as np

# Create two car objects with different attributes
car1 = Car("Tesla", "Model 3", 2020, 20, [0, 0, 0], [1, 0, 0])
car2 = Car("Ford", "F-150", 2019, 30, [10, 10, 0], [-1, -1, 0])
```

Then you can use the methods of the Car class to manipulate and compare the car objects. For example:

```python
# Accelerate car 1 by 10 units
car1.accelerate(10)
print(f"Car 1 speed after acceleration: {car1.speed}")

# Brake car 2 by 5 units
car2.brake(5)
print(f"Car 2 speed after braking: {car2.speed}")

# Find the time to collision of the cars
t = car1.time_to_collision(car2)
print(f"Time to collision: {t}")

# Move the cars for t seconds
car1.move(t)
car2.move(t)

# Check if the cars collide
print(f"Do the cars collide? {car1.is_collide(car2)}")
```

You can also create more car objects and use different methods to manipulate and compare them. For example:

```python
# Create five car objects with different attributes
car1 = Car("Tesla", "Model 3", 2020, 20, [0, 0, 0], [1, 0, 0])
car2 = Car("Ford", "F-150", 2019, 30, [10, 10, 0], [-1, -1, 0])
car3 = Car("Honda", "Civic", 2018, 25, [5, -5, 0], [0, 1, 0])
car4 = Car("Toyota", "Corolla", 2017, 35, [-10, -10, 0], [1, 1, 0])
car5 = Car("BMW", "X5", 2021, 40, [15, -15, 0], [-1, 1, 0])
 ```
