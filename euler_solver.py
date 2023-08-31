# Euler’s Method
''' Euler’s Method is a first-order numerical method used to approximate solutions to Ordinary Differential Equations
(ODEs).The method’s simplicity makes it a great starting point for understanding numerical integration and solving
initial value problem when exact solutions are elusive or when dealing with complex systems.
'''

# Here’s how it works:
'''
1. Start with What You Know: You have your equation, and you know what’s happening at the beginning
– that’s your starting point, the initial condition.
2. Baby Steps: Pick a small step size, like a baby step. We’re not jumping, just tiptoeing.
3. Follow the Arrows: Imagine your equation as a set of arrows telling you how things change. Take a baby
step in the direction of those arrows.
4. Guess What’s Next: At your new spot, guess where you’ll be next. It’s like predicting the weather – not
perfect, but close enough.
5. Repeat and Keep Going: Keep taking baby steps and guessing, hopping from point to point, until you
reach where you want to go.
'''

def euler_solver ( func , y0 , t0 , t_final , delta_t ) :
'''
Implements the Euler ’s method to approximate solutions of an ordinary differential
equation .
param func : The derivative function representing the rate of change , defined as
func (t, y).
param y0: The initial value of the dependent variable .
param t0: The initial time .
param t_final : The final time until which the solution will be approximated .
param delta_t : The step size , determining the interval between calculations .
return : Lists of time values and corresponding approximate solution values .
'''

# Start with What You Know
t_values = [ t0 ]
y_values = [ y0 ]
t = t0
y = y0

# Baby steps
while t < t_final : # Repeat and keep going
# Follow the Arrows and guess what ’s next
y += delta_t * func (t , y )
t += delta_t

t_values . append ( t )
y_values . append ( y )

return t_values , y_values

