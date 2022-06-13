import numpy, math
choice = stop = 0 #initializing variables
def ask(): #initial prompt driver code
    print("Please Enter type of collision: ") 
    print("1: Two objects colliding in a straight line with +ve direction as right")
    print("2: Two objects colliding at an angle to the line joining the centres with +ve direction as right")
def c1():
    e = float(input("Enter coefficient of restituition: "))
    if u1 > u2:
        EEEEE = (u1 - u2) * e #this is replicating the way it would be solved on paper but using matrices instead of simultaneous equations
        mom = (m1 * u1) + (m2 * u2) #
        matrixA = numpy.array([[-1,1],[m1,m2]]) #
        matrixB = numpy.array([EEEEE,mom]) #
        C = list(numpy.linalg.solve(matrixA,matrixB)) #
        vfinal1, vfinal2 = C 
        print("The velocity of Particle A is", "%.3f" % vfinal1, "m/s and the velocity of Particle B after collision is", "%.3f" % vfinal2, "m/s")
    else:    #the "%.3f" above and below is being used to simplify to 3.d.p                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        print("The particles will never meet.")
def c2():
    a1 = float(input("Enter the acute angle that particle 1 will make with the line that connects the centre of the particles(in degrees): "))
    a2 = float(input("Enter the acute angle that particle 2 will make with the line that connects the centre of the particles(in degrees): "))
    e = float(input("Enter coefficient of restituition: "))
    u1sincomp = u1 * math.sin(math.radians(a1)) #
    u2sincomp = u2 * math.sin(math.radians(a2)) # converting to radians because math.sin/math.cos requires radians
    u1coscomp = u1 * math.cos(math.radians(a1)) #
    u2coscomp = u2 * math.cos(math.radians(a2)) #
    if u1coscomp > u2coscomp:
        EEEEE = (u1coscomp - u2coscomp) * e #
        EEEEE = (u1 - u2) * e #replicating the way it would be solved on paper
        mom = (m1 * u1coscomp) + (m2 * u2coscomp) # 
        matrixA = numpy.array([[-1,1],[m1,m2]]) #
        matrixB = numpy.array([EEEEE,mom]) #
        C = list(numpy.linalg.solve(matrixA,matrixB)) #
        vfinal1, vfinal2 = C #the results of the matrix are stored in 2 different variables 
        finalanglea = math.degrees(math.atan(u1sincomp / vfinal1))
        finalangleb = math.degrees(math.atan(u2sincomp / vfinal2))
        print("The velocity of Particle A is", "%.3f" % math.hypot(vfinal1,u1sincomp), "m/s with an angle of","%.3f" % finalanglea, "° and the velocity of Particle B after collision is", "%.3f" % math.hypot(vfinal2,u2sincomp), "m/s with an angle of", "%.3f" % finalangleb, "°.")
    else:
        print("The particles will never meet.")
#########prompt and execute###########
ask()
choice = int(input("What choice do you want to choose? "))
m1 = float(input("Enter mass of particle 1 in kg: "))
m2 = float(input("Enter mass of particle 2 in kg: "))
u1 = float(input("Enter initial velocity of particle 1 in m/s: "))
u2 = float(input("Enter initial velocity of particle 2 in m/s: "))
if choice == 1:
    c1()
if choice == 2:
    c2()