from Car_class import Car

car1 = Car("Tesla", "Model 3", 2020, 20, [0, 0, 0], [1, 0, 0])
car2 = Car("Ford", "F-150", 2019, 30, [10, 10, 0], [-1, -1, 0])
car3 = Car("Honda", "Civic", 2018, 25, [5, -5, 0], [0, 1, 0])
car4 = Car("Toyota", "Corolla", 2017, 35, [-10, -10, 0], [1, 1, 0])
car5 = Car("BMW", "X5", 2021, 40, [15, -15, 0], [-1, 1, 0])

print(f"Car 1 position: {car1.position()}")
print(f"Car 1 velocity: {car1.velocity}")
print(f"Car 2 position: {car2.position()}")
print(f"Car 2 velocity: {car2.velocity}")
print(f"Car 3 position: {car3.position()}")
print(f"Car 3 velocity: {car3.velocity}")
print(f"Car 4 position: {car4.position()}")
print(f"Car 4 velocity: {car4.velocity}")
print(f"Car 5 position: {car5.position()}")
print(f"Car 5 velocity: {car5.velocity}")

car1.accelerate(10)
print(f"Car 1 speed after acceleration: {car1.speed}")

car2.brake(5)
print(f"Car 2 speed after braking: {car2.speed}")

car3.accelerate(15)
print(f"Car 3 speed after acceleration: {car3.speed}")

car4.brake(10)
print(f"Car 4 speed after braking: {car4.speed}")

car5.accelerate(20)
print(f"Car 5 speed after acceleration: {car5.speed}")

car1.brake(7)
print(f"Car 1 speed after braking: {car1.speed}")

car3.brake(10)
print(f"Car 3 speed after braking: {car3.speed}")

t12 = car1.time_to_collision(car2)
t13 = car1.time_to_collision(car3)
t14 = car1.time_to_collision(car4)
t15 = car1.time_to_collision(car5)
t23 = car2.time_to_collision(car3)
t24 = car2.time_to_collision(car4)
t25 = car2.time_to_collision(car5)
t34 = car3.time_to_collision(car4)
t35 = car3.time_to_collision(car5)
t45 = car4.time_to_collision(car5)

print(f"Time to collision between car 1 and car 2: {t12}")
print(f"Time to collision between car 1 and car 3: {t13}")
print(f"Time to collision between car 1 and car 4: {t14}")
print(f"Time to collision between car 1 and car 5: {t15}")
print(f"Time to collision between car2 and car 3: {t23}")
print(f"Time to collision between car2 and car4: {t24}")
print(f"Time to collision between car2 and car5: {t25}")
print(f"Time to collision between car3 and car4: {t34}")
print(f"Time to collision between car3 and car5: {t35}")
print(f"Time to collision between car4 and car5: {t45}")