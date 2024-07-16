import driver

driver.ask()
choice = int(input("What choice do you want to choose? "))

if choice == 1:
    m1, m2, u1, u2 = driver.prompt_mass_and_velocity()
    driver.collision_straight(m1, m2, u1, u2)

if choice == 2:
    m1, m2, u1, u2 = driver.prompt_mass_and_velocity()
    driver.collision_angle(m1, m2, u1, u2)

if choice == 3:
    dp, mode = driver.prompt_pi()
    driver.collision_pi(dp, mode)
