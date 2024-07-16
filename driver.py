import math


import numpy

choice = stop = 0  # initializing variables


def ask():  # initial prompt driver code
    print("Please Enter type of collision: ")
    print("1: Two objects colliding in a straight line with +ve direction as right")
    print("2: Two objects colliding at an angle to the line joining the centres with +ve direction as right")
    print("3: NEW: Calculate the value of pi using colliding balls to some precision")


def prompt_mass_and_velocity():
    m1 = float(input("Enter mass of particle 1 in kg: "))
    m2 = float(input("Enter mass of particle 2 in kg: "))
    u1 = float(input("Enter initial velocity of particle 1 in m/s: "))
    u2 = float(input("Enter initial velocity of particle 2 in m/s: "))
    return m1, m2, u1, u2


def prompt_pi():
    mode = ""
    # check-expects
    # if d = 0, m = 1
    # if d = 1, m = 100
    # if d = 2, m = 10000

    # therefore, m = 100^(d)

    dp = int(input("How many d.p do you want to calculate pi to?: "))  # 1
    print("What level of output do you want? ")
    print("     'so' for Simple Output")
    print("     'vm' for Verbose Mode")

    mode = str(input("Please enter either 'so' or 'vm': "))
    print(mode)
    flag = False

    if mode == "so" or mode == "vm":
        flag = True
    while not flag:
        mode = input("Incorrect input. Please enter either 'so' or 'vm':")
        if mode == "so" or mode == "vm":
            break

    return dp, mode


def collision_straight(m1, m2, u1, u2):
    e = float(input("Enter coefficient of restituition: "))
    if u1 > u2:
        vfinal1, vfinal2 = calculate_velocity(e, u1, u2, m1, m2)
        print("The velocity of Particle A is", "%.3f" % vfinal1,
              "m/s and the velocity of Particle B after collision is", "%.3f" % vfinal2, "m/s")
    else:  # the "%.3f" above and below is being used to simplify to 3.d.p
        print("The particles will never meet.")


def collision_angle(m1, m2, u1, u2):
    a1 = float(input(
        "Enter the acute angle that particle 1 will make with the line that connects the centre of the particles(in degrees): "))
    a2 = float(input(
        "Enter the acute angle that particle 2 will make with the line that connects the centre of the particles(in degrees): "))
    e = float(input("Enter coefficient of restituition: "))
    u1sincomp = u1 * math.sin(math.radians(a1))  #
    u2sincomp = u2 * math.sin(math.radians(a2))  # converting to radians because math.sin/math.cos requires radians
    u1coscomp = u1 * math.cos(math.radians(a1))  #
    u2coscomp = u2 * math.cos(math.radians(a2))  #
    if u1coscomp > u2coscomp:
        vfinal1, vfinal2 = calculate_velocity(e, u1coscomp, u2coscomp, m1, m2)
        finalanglea = math.degrees(math.atan(u1sincomp / vfinal1))
        finalangleb = math.degrees(math.atan(u2sincomp / vfinal2))
        print("The velocity of Particle A is", "%.3f" % math.hypot(vfinal1, u1sincomp), "m/s with an angle of",
              "%.3f" % finalanglea, "° and the velocity of Particle B after collision is",
              "%.3f" % math.hypot(vfinal2, u2sincomp), "m/s with an angle of", "%.3f" % finalangleb, "°.")
    else:
        print("The particles will never meet.")


def calculate_velocity(e, u1, u2, m1, m2):
    # Replicating the way it would be solved on paper but using matrices instead of simultaneous equations
    EEEEE = (u1 - u2) * e
    mom = (m1 * u1) + (m2 * u2)  #
    matrixA = numpy.array([[-1, 1], [m1, m2]])  #
    matrixB = numpy.array([EEEEE, mom])  #
    C = list(numpy.linalg.solve(matrixA, matrixB))  #
    vfinal1, vfinal2 = C
    return vfinal1, vfinal2


def collision_pi(dp, mode):
    m1 = 1
    u1 = 0
    u2 = -1
    m2 = 100 ** dp
    collisions = 0

    # assume the ball on the right is hurling towards the ball on the left
    # (after the first collision) while abs of the block on the left is greater than the block on the right,
    # more collisions will occur

    while not (u1 >= 0 and u2 >= 0 and abs(u2) >= abs(u1)):
        if u1 < 0:
            u1 = -u1
            collisions += 1
            print_info(collisions, u1, u2, mode, rebound=True)
            if u1 >= 0 and u2 >= 0 and abs(u2) >= abs(u1):
                break

        u1, u2 = calculate_velocity(1, u1, u2, m1, m2)
        collisions += 1
        print_info(collisions, u1, u2, mode)

    print("\033[1m" + "The value of pi to", dp, "d.p is:", collisions / (10 ** dp), "\033[0m")


def print_info(collisions, u1, u2, output_mode, rebound=False):
    """
        Prints information about the collision simulation.

        SP1 and SP2 refer to simulated particle 1 and simulated particle 2 with speeds u1 and u2 respectively.

        Parameters:
        collisions (int): The current number of collisions.
        u1 (float): The velocity of SP1 (simulated particle 1).
        u2 (float): The velocity of SP2 (simulated particle 2).
        output_mode (str): The mode of output. 'so' for Simple Output, 'vm' for Verbose Mode.
        rebound (bool): Flag indicating if the collision is a rebound (default is False).

        Returns:
        None
        """
    if output_mode == "so":
        if rebound:
            print("[u1:", u1, "u2:", u2, "collisions:", collisions, "] <<REBOUND>>")
        else:
            print("[u1:", u1, "u2:", u2, "collisions:", collisions, "]")

    if output_mode == "vm":
        if rebound:
            print("SP1 has collided against the wall and its velocity has changed from", "%.3f" % -u1,
                  "to", "%.3f." % u1, "[u1 =", "%.3f," % u1, "u2 =", "%.3f]" % u2, "with", collisions, "collisions")
        else:
            print("SP1 has collided with SP2 and their velocities are [u1 =", "%.3f," % u1,
                  "u2 =", "%.3f]," % u2, "                                    with", collisions, "collisions")

