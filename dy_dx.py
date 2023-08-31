import numpy as np
import matplotlib . pyplot as plt

# Define the differential equation
def dy_dx (x , y ) :
"""
Compute the value of the derivative dy/dx at a given point (x, y) using the function x
- y.

: param x: The x- coordinate of the point .
: param y: The y- coordinate of the point .
: return : The value of the derivative dy/dx at the point (x, y).
"""
return x - y


# Points to evaluate the differential equation
x_range = np . linspace ( -2 , 2 , 20)
y_range = np . linspace ( -2 , 2 , 20)

# Points to our grid
X , Y = np . meshgrid ( x_range , y_range )

# Calculate the slopes using the differential equation
slopes = dy_dx (X , Y )

# Create the slope field
plt . figure ( figsize =(8 , 6) )
plt . quiver (X , Y , np . ones_like ( X ) , slopes , color =’b’, angles =’xy ’)
plt . xlabel (’x’)
plt . ylabel (’y’)
plt . title (’Slope Field ’)
plt . grid ( True )
plt . savefig (’ my_first_slope_field .png ’)