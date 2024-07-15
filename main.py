import driver

driver.ask()
choice = int(input("What choice do you want to choose? "))
m1 = float(input("Enter mass of particle 1 in kg: "))
m2 = float(input("Enter mass of particle 2 in kg: "))
u1 = float(input("Enter initial velocity of particle 1 in m/s: "))
u2 = float(input("Enter initial velocity of particle 2 in m/s: "))
if choice == 1:
    driver.collision_straight(m1, m2, u1, u2)
if choice == 2:
    driver.collision_angle(m1, m2, u1, u2)
