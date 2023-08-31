# HAND - ON 3
'''
1. Modify the Euler’s method code so you can generate a single plot for the following initial conditions: x0 =
1.0, 2.0, 3.0, 10, 50, 100. Your plot should look like this one:
'''
import matplotlib.pyplot as plt

def euler_solver(func, y0, t0, t_final, delta_t):

    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0

    while t < t_final:
        y += delta_t * func(t, y)
        t += delta_t

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

def kcrystal(t, x):
    k = 0.1  # Decay constant
    return -k * x

# Initial conditions for x0 = 1.0, 2.0, 3.0, 10, 50, 100
x0_values = [1.0, 2.0, 3.0, 10, 50, 100]
t0 = 0.0
t_final = 10.0
delta_t = 0.1

# Plotting
plt.figure(figsize=(10, 6))

for x0 in x0_values:
    t_values, x_values = euler_solver(func=kcrystal, y0=x0, t0=t0, t_final=t_final, delta_t=delta_t)
    plt.plot(t_values, x_values, label=f'x0 = {x0}')

plt.xlabel('Time')
plt.ylabel('x(t)')
plt.title('Approximate Solution of dx/dt = -kx using Euler\'s Method')
plt.legend()
plt.grid(True)
plt.show()


#  How much time is needed for a Kyber crystal with an initial energy level of 50 to get close to zero? The
# time is step is given in years.
from math import log

# Parameters:
k = 0.1
x0 = 50
threshold = 1

t = log(threshold /x0) / -k
print(f'Time: {t:.2f} years')

# Is there a difference if the initial energy level is 10000?
from math import log

# Parameters:
k = 0.1
x0 = 100
threshold = 1

t = log(threshold /x0) / -k
print(f'Time: {t:.2f} years')

# Modify the values of k as follows and summarize your findings:
# – k>0
def kcrystal(t, x):
    k = 0.1  # Decay constant
    return -k * x

# Initial conditions for x0 = 1.0, 2.0, 3.0, 10, 50, 100
x0_values = [1.0, 2.0, 3.0, 10, 50, 100]
t0 = 0.0
t_final = 10.0
delta_t = 0.1

# Plotting
plt.figure(figsize=(10, 6))

for x0 in x0_values:
    t_values, x_values = euler_solver(func=kcrystal, y0=x0, t0=t0, t_final=t_final, delta_t=delta_t)
    plt.plot(t_values, x_values, label=f'x0 = {x0}')

plt.xlabel('Time')
plt.ylabel('x(t)')
plt.title('Approximate Solution of dx/dt = -kx using Euler\'s Method')
plt.legend()
plt.grid(True)
plt.show()

# – k=0
def kcrystal(t, x):
    k = 0 # Decay constant
    return -k * x

# Initial conditions for x0 = 1.0, 2.0, 3.0, 10, 50, 100
x0_values = [1.0, 2.0, 3.0, 10, 50, 100]
t0 = 0.0
t_final = 10.0
delta_t = 0.1

# Plotting
plt.figure(figsize=(10, 6))

for x0 in x0_values:
    t_values, x_values = euler_solver(func=kcrystal, y0=x0, t0=t0, t_final=t_final, delta_t=delta_t)
    plt.plot(t_values, x_values, label=f'x0 = {x0}')

plt.xlabel('Time')
plt.ylabel('x(t)')
plt.title('Approximate Solution of dx/dt = -kx using Euler\'s Method')
plt.legend()
plt.grid(True)
plt.show()

# – k<0
def kcrystal(t, x):
    k = -0.1 # Decay constant
    return -k * x

# Initial conditions for x0 = 1.0, 2.0, 3.0, 10, 50, 100
x0_values = [1.0, 2.0, 3.0, 10, 50, 100]
t0 = 0.0
t_final = 10.0
delta_t = 0.1

# Plotting
plt.figure(figsize=(10, 6))

for x0 in x0_values:
    t_values, x_values = euler_solver(func=kcrystal, y0=x0, t0=t0, t_final=t_final, delta_t=delta_t)
    plt.plot(t_values, x_values, label=f'x0 = {x0}')

plt.xlabel('Time')
plt.ylabel('x(t)')
plt.title('Approximate Solution of dx/dt = -kx using Euler\'s Method')
plt.legend()
plt.grid(True)
plt.show()


# Plot the slope fields for:
# dx/dt = −ax + bxy
import numpy as np
import matplotlib . pyplot as plt

# Define the differential equation
def dy_dx (x , y ) :

    return -a*x + b*x*y


# Points to evaluate the differential equation
x_range = np . linspace ( -2 , 2 , 20)
y_range = np . linspace ( -2 , 2 , 20)

# Points to our grid
X , Y = np . meshgrid ( x_range , y_range )

# Calculate the slopes using the differential equation
slopes = dy_dx (X , Y )

# Create the slope field
plt . figure ( figsize =(8 , 6) )
plt . quiver (X , Y , np . ones_like ( X ) , slopes , color ='b', angles ='xy')
plt . xlabel ('x')
plt . ylabel ('y')
plt . title ('Slope Field')
plt . grid ( True )
plt . savefig ('my_first_slope_field .png')