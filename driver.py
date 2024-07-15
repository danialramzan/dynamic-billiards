import math
import numpy

choice = stop = 0  # initializing variables


def ask():  # initial prompt driver code
    print("Please Enter type of collision: ")
    print("1: Two objects colliding in a straight line with +ve direction as right")
    print("2: Two objects colliding at an angle to the line joining the centres with +ve direction as right")


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
