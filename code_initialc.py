import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

def initial_cond(state_var1: float,state_var2: float, coeff: int, end_time:int):
    x1 = state_var1
    x2 = state_var2
    a = coeff
    t = end_time
    results = [x1,x2]
    
    return x1,x2,a,t,results

def update(result : list, state_var1:float, state_var2:float):
    for k in range(2, 100):
        y = 2 * result[k-1] - result[k-2]
        result.append(y)
    return result.append(y)
    

    
stateVar1,stateVar2, Coeff,Time,Results = initial_cond(1,10,-0.5,30)
update(Results,stateVar1,stateVar2)


    
fig = px.line(Results, title = 'My first difference equation')
fig.update_layout(xaxis_title = 'Time',
                 yaxis_title = 'State variable')
legend_names = {'0': 'x'}

fig.for_each_trace(lambda t:t.update(name = legend_names[t.name]))
fig.show()

    
    