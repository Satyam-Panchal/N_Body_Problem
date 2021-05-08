import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection="3d")

N = 3
G = 6.67408e-11
delta_t = 0.100
total_time = 360


def get_a_i(i, m, x, y, z):
    x_sum = 0
    for j in range(N):
        if i == j:
            continue
        rij = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2)
        x_sum += (-G * m[i] * m[j] * (x[i] - x[j]))/np.power(rij, 3)

    y_sum = 0
    for j in range(N):
        if i == j:
            continue
        rij = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2)
        y_sum += (-G * m[i] * m[j] * (y[i] - y[j])) / np.power(rij, 3)

    z_sum = 0
    for j in range(N):
        if i == j:
            continue
        rij = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2)
        z_sum += (-G * m[i] * m[j] * (z[i] - z[j])) / np.power(rij, 3)

    return [x_sum/m[i] , y_sum/m[i], z_sum/m[i]]


# Initial vector definitions

r1_vector = [0, 0, 0]
r2_vector = [0.5, 0, 0]
r3_vector = [-1, 0, 0]

v1_vector = [0, 0, 0.05]
v2_vector = [0, 1.63, 0]
v3_vector = [0, -0.63, 0]

m = [1/G, 1, 1]  # Lists of masses

# creating lists

x1_list, y1_list, z1_list, x2_list, y2_list, z2_list, x3_list, y3_list, z3_list = ([] for i in range(9))
v1x_list, v1y_list, v1z_list, v2x_list, v2y_list, v2z_list, v3x_list, v3y_list, v3z_list = ([] for i in range(9))
t_list = [0]

# Initializations

x1 = r1_vector[0]
y1 = r1_vector[1]
z1 = r1_vector[2]

x2 = r2_vector[0]
y2 = r2_vector[1]
z2 = r2_vector[2]

x3 = r3_vector[0]
y3 = r3_vector[1]
z3 = r3_vector[2]

v1x = v1_vector[0]
v1y = v1_vector[1]
v1z = v1_vector[2]

v2x = v2_vector[0]
v2y = v2_vector[1]
v2z = v2_vector[2]

v3x = v3_vector[0]
v3y = v3_vector[1]
v3z = v3_vector[2]

# Updating Lists
x1_list.append(x1)
y1_list.append(y1)
z1_list.append(z1)

x2_list.append(x2)
y2_list.append(y2)
z2_list.append(z2)

x3_list.append(x3)
y3_list.append(y3)
z3_list.append(z3)

# Calculating accelerations
x_coord_list_for_a = [x1, x2, x3]
y_coord_list_for_a = [y1, y2, y3]
z_coord_list_for_a = [z1, z2, z3]

a1 = get_a_i(0, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
a2 = get_a_i(1, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
a3 = get_a_i(2, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)

t = 0.05

while t <= total_time:
    # Velocities
    v1x += delta_t * a1[0]
    v1y += delta_t * a1[1]
    v1z += delta_t * a1[2]

    v2x += delta_t * a2[0]
    v2y += delta_t * a2[1]
    v2z += delta_t * a2[2]

    v3x += delta_t * a3[0]
    v3y += delta_t * a3[1]
    v3z += delta_t * a3[2]

    # Positions
    x1 += delta_t * v1x
    y1 += delta_t * v1y
    z1 += delta_t * v1z

    x2 += delta_t * v2x
    y2 += delta_t * v2y
    z2 += delta_t * v2z

    x3 += delta_t * v3x
    y3 += delta_t * v3y
    z3 += delta_t * v3z

    # Updating Lists
    x1_list.append(x1)
    y1_list.append(y1)
    z1_list.append(z1)

    x2_list.append(x2)
    y2_list.append(y2)
    z2_list.append(z2)

    x3_list.append(x3)
    y3_list.append(y3)
    z3_list.append(z3)

    # Increasing time by half a factor of delta_t
    t += delta_t / 2
    t_list.append(t)

    # Updating coord_lists to solve for a
    x_coord_list_for_a = [x1, x2, x3]
    y_coord_list_for_a = [y1, y2, y3]
    z_coord_list_for_a = [z1, z2, z3]

    a1 = get_a_i(0, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
    a2 = get_a_i(1, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
    a3 = get_a_i(2, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)

    t += delta_t / 2

ax.plot3D(x1_list, y1_list, z1_list, color="darkblue", label='Body 1')
ax.plot3D(x2_list, y2_list, z2_list, color="tab:red", label='Body 2')
ax.plot3D(x3_list, y3_list, z3_list, color='green', label='Body 3')

ax.set_xlabel("x-coordinate", fontsize=14)
ax.set_ylabel("y-coordinate", fontsize=14)
ax.set_zlabel("z-coordinate", fontsize=14)
ax.set_title("Visualization of orbits of stars in a two-body system\n", fontsize=14)
ax.legend(loc="upper left", fontsize=14)

plt.show()