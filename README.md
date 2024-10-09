# Dynamic Billiards Simulator

A Python project demonstrating the principles of dynamic billiards through various collision scenarios. Originally created by me during high school as a proof of concept for collisions based on Newton's Law of Restitution for my CAIE A Level Further Maths 9231 Mechanics course, this project has been expanded to include more complex and interesting collision simulations.

![image](https://github.com/user-attachments/assets/9dccad1a-9e8a-499c-8201-422c1d3c5138)
![image](https://github.com/user-attachments/assets/1cf3c35e-fc91-4805-af9b-ce00ed6bcce4)
![image](https://github.com/user-attachments/assets/98f1d033-1eff-46a7-89ff-62000dfe65ee)
![image](https://github.com/user-attachments/assets/40a5bcd1-340e-4c26-a318-d764dc971d25)


### Features
Linear Collisions: Simulate two objects colliding in a straight line, demonstrating the basic principles of conservation of momentum and energy.

Angular Collisions: Model collisions at an angle, reflecting more realistic and intricate billiard dynamics.

**New! (2024-07-15)**
Pi Approximation: Use colliding balls to approximate the value of π, showcasing a creative application of elastic collision principles.
  This project was inspired by Grant Sanderson's (3Blue1Brown) video on the topic [(Approximating Pi with Colliding Blocks)](https://www.youtube.com/watch?v=jsYwFizhncE) and the associated paper upon which it is based:
  Galperin, G. (2003). Playing pool with π (the number π from a billiard point of view). Regular and Chaotic Dynamics, 8(4), 375-394. https://doi.org/10.1070/RD2003v008n04ABEH000252

**Planned Features:**
- GUI Implementation
- Visual Physics Engine for Particles colliding
- Port program to C to [improve the efficiency of inefficiency.](https://c.tenor.com/7UarUv_Z1QYAAAAd/tenor.gif)



## User Stories:

- **As a user, I want to simulate billiard balls colliding head on with arbitrary initial velocities and COR's**

- **As a user, I want to be able to model collisions between billiard balls at angles with arbitrary initial velocities and calculate their velocities and angles after collision**

-  **As a user,  I want to use a ridiculously inefficient and unnessesary algorithm to calculate the value of pi to an arbitary number of significant figures using a completely unconventional approach when far better and more appropriate methods are available.**
    
- **As a user, I want to be able to use a GUI to model these collisions and see them occur in real time**
    








### OLD DESCRIPTION:
#### Restitution Momentum Calculator

A Python3 project I made as a proof of concept for collisions based on newtons law of restitution for my CAIE A Level Further Maths 9231 Mechanics course.
This project uses the math library and matrices from the numpy library in order to make simultaneous equations using conservation of momentum and Newtons law of restitution to calculate speeds of objects after colliding given a coefficient of restitution x, where 0 ≤ x ≤ 1.
It greatly helped me understand the topic better and also helped me verify my answers for my calculations.

It **requires** numpy to be installed, which can be done with
>pip3 install numpy

in an app such as terminal, cmd, or powershell. 
^skip this step if it is already installed.
