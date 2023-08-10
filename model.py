import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

def initial_cond(state_var: float,coeff: int, end_time:int):
    x = state_var
    a = coeff
    t = end_time
    results = []
    
    return x,a,t,results

def observe(result : list, state_var:float):
    return result.append(state_var)
    
def update(x,a):
    return a*x
    
stateVar,Coeff,Time,Results = initial_cond(5.3,-0.5,30)

for time in range(Time):
    observe(Results,stateVar)
    stateVar = update(stateVar,Coeff)
    
fig = px.line(Results, title = 'My first difference equation')
fig.update_layout(xaxis_title = 'Time',
                 yaxis_title = 'State variable')
legend_names = {'0': 'x'}

fig.for_each_trace(lambda t:t.update(name = legend_names[t.name]))
fig.show()

    
    
