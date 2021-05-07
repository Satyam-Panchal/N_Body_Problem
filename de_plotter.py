import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# e = small time interval
# expression = string expression that defines acceleration of the body as a function of its postions and velocity
# v = second derivative of x

def coordinate_points(total_time, initial_x, initial_v, e, expression):
    t_list = []
    x_list = []
    t_list.append(0)
    # Initialisation
    t = 0.05
    v = initial_v
    x = initial_x
    x_list.append(x)
    a = eval(expression)
    while t <= total_time:
        v += e * a
        x += e * v
        x_list.append(x)
        t += e / 2
        t_list.append(t)
        a = eval(expression)
        t += e / 2

    return x_list







