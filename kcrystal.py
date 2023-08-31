# We can use this function to approximate the solution of the Kyber’s crystal problem:
def kcrystal (t , x , k ) :
"""
Calculates the rate of change for a Kyber crystal ’s energy using the given
differential equation .

: param t: Time at which the rate of change is calculated .
: param x: Current energy of the crystal .
: param k: Growth coefficient determining the rate of energy .
: return : The rate of change of the crystal ’s energy at the given time .
"""
return -k * x

# Parameters :
# Decay constant
k = 0.1
# Initial condition
x0 = 1.0
# Start time
t0 = 0.0
# End time
t_final = 10.0
# Time step size
delta_t = 0.1

t_values , x_values = fos . euler_solver ( func = kcrystal , y0 = x0 , t0 = t0 , t_final = t_final ,
delta_t = delta_t , k = k )

# Plot the approximate solution
plt . plot ( t_values , x_values , label =’ Approximate Solution ’)
plt . xlabel (’Time ’)
plt . ylabel (’x(t)’)
plt . title (’ Approximate Solution of dx/dt = -kx using Euler \ ’s Method ’)
plt . legend ()
plt . grid ( True )
plt . show ()
    