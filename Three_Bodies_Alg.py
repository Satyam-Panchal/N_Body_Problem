import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation

ax = plt.axes(projection='3d')

N = 3
G = 6.67e-11
delta_t = 0.01
total_time = 200



def get_a_i(i, m, x, y, z):
    x_sum = 0
    for j in range(N):
        if i == j:
            continue

        x_sum += (-G * m[i] * m[j] * (x[i] - x[j]))/np.power(np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2), 3)

    y_sum = 0
    for j in range(N):
        if i == j:
            continue
        rij = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2)
        y_sum += (-G * m[i] * m[j] * (y[i] - y[j])) / np.power(np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2), 3)

    z_sum = 0
    for j in range(N):
        if i == j:
            continue
        rij = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2)
        z_sum += (-G * m[i] * m[j] * (z[i] - z[j])) / np.power(np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2), 3)

    return [x_sum/m[i], y_sum/m[i], z_sum/m[i]]


# Initial vector definitions

r1_vector = [-0.5, 0, 0]
r2_vector = [0.5, 0, 0]
r3_vector = [0, 1, 0]

v1_vector = [0.01, 0.01, 0]
v2_vector = [-0.05, 0, -0.1]
v3_vector = [0, -0.01, 0]

m = [1.1e8, 0.9e8, 1e8]  # Lists of masses

# creating lists

x1_list, y1_list, z1_list, x2_list, y2_list, z2_list, x3_list, y3_list, z3_list = ([] for i in range(9))
v1x_list, v1y_list, v1z_list, v2x_list, v2y_list, v2z_list, v3x_list, v3y_list, v3z_list = ([] for j in range(9))
a1x_list, a1y_list, a1z_list, a2x_list, a2y_list, a2z_list, a3x_list, a3y_list, a3z_list = ([]for k in range(9))


# Initializations

x_coord_list_for_a = [r1_vector[0], r2_vector[0], r3_vector[0]]
y_coord_list_for_a = [r1_vector[1], r2_vector[1], r3_vector[1]]
z_coord_list_for_a = [r1_vector[2], r2_vector[2], r3_vector[2]]

a1 = get_a_i(0, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
a2 = get_a_i(1, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
a3 = get_a_i(2, m ,x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)

a1x_list.append(a1[0])
a1y_list.append(a1[1])
a1z_list.append(a1[2])

a2x_list.append(a2[0])
a2y_list.append(a2[1])
a2z_list.append(a2[2])

a3x_list.append(a3[0])
a3y_list.append(a3[1])
a3z_list.append(a3[2])

wx1 = r1_vector[0]
wy1 = r1_vector[1]
wz1 = r1_vector[2]

wx2 = r2_vector[0]
wy2 = r2_vector[1]
wz2 = r2_vector[2]

wx3 = r3_vector[0]
wy3 = r3_vector[1]
wz3 = r3_vector[2]

x1_list.append(wx1)
y1_list.append(wy1)
z1_list.append(wz1)

x2_list.append(wx2)
y2_list.append(wy2)
z2_list.append(wz2)

x3_list.append(wx3)
y3_list.append(wy3)
z3_list.append(wz3)

wv1x = v1_vector[0]
wv1y = v1_vector[1]
wv1z = v1_vector[2]

wv2x = v2_vector[0]
wv2y = v2_vector[1]
wv2z = v2_vector[2]

wv3x = v3_vector[0]
wv3y = v3_vector[1]
wv3z = v3_vector[2]

v1x_list.append(wv1x)
v1y_list.append(wv1y)
v1z_list.append(wv1z)

v2x_list.append(wv2x)
v2y_list.append(wv2y)
v2z_list.append(wv2z)

v3x_list.append(wv3x)
v3y_list.append(wv3y)
v3z_list.append(wv3z)

hx1 = r1_vector[0] + (v1_vector[0] * delta_t/2)
hy1 = r1_vector[1] + (v1_vector[1] * delta_t/2)
hz1 = r1_vector[2] + (v1_vector[2] * delta_t/2)

hx2 = r2_vector[0] + (v2_vector[0] * delta_t/2)
hy2 = r2_vector[1] + (v2_vector[1] * delta_t/2)
hz2 = r2_vector[2] + (v2_vector[2] * delta_t/2)

hx3 = r3_vector[0] + (v3_vector[0] * delta_t/2)
hy3 = r3_vector[1] + (v3_vector[1] * delta_t/2)
hz3 = r3_vector[2] + (v3_vector[2] * delta_t/2)

x1_list.append(hx1)
y1_list.append(hy1)
z1_list.append(hz1)

x2_list.append(hx2)
y2_list.append(hy2)
z2_list.append(hz2)

x3_list.append(hx3)
y3_list.append(hy3)
z3_list.append(hz3)

hv1x = v1_vector[0] + (a1[0] * (delta_t/2))
hv1y = v1_vector[1] + (a1[1] * (delta_t/2))
hv1z = v1_vector[2] + (a1[2] * (delta_t/2))

hv2x = v2_vector[0] + (a2[0] * (delta_t/2))
hv2y = v2_vector[1] + (a2[1] * (delta_t/2))
hv2z = v2_vector[2] + (a2[2] * (delta_t/2))

hv3x = v3_vector[0] + (a3[0] * (delta_t/2))
hv3y = v3_vector[1] + (a3[1] * (delta_t/2))
hv3z = v3_vector[2] + (a3[2] * (delta_t/2))

v1x_list.append(hv1x)
v1y_list.append(hv1y)
v1z_list.append(hv1z)

v2x_list.append(hv2x)
v2y_list.append(hv2y)
v2z_list.append(hv2z)

v3x_list.append(hv3x)
v3y_list.append(hv3y)
v3z_list.append(hv3z)

t = delta_t

while t <= total_time:

    wx1 += hv1x * delta_t
    wy1 += hv1y * delta_t
    wz1 += hv1z * delta_t

    wx2 += hv2x * delta_t
    wy2 += hv2y * delta_t
    wz2 += hv2z * delta_t

    wx3 += hv3x * delta_t
    wy3 += hv3y * delta_t
    wz3 += hv3z * delta_t

    x1_list.append(wx1)
    y1_list.append(wy1)
    z1_list.append(wz1)

    x2_list.append(wx2)
    y2_list.append(wy2)
    z2_list.append(wz2)

    x3_list.append(wx3)
    y3_list.append(wy3)
    z3_list.append(wz3)

    x_coord_list_for_a = [hx1, hx2, hx3]
    y_coord_list_for_a = [hy1, hy2, hy3]
    z_coord_list_for_a = [hz1, hz2, hz3]

    a1 = get_a_i(0, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
    a2 = get_a_i(1, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
    a3 = get_a_i(2, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)

    a1x_list.append(a1[0])
    a1y_list.append(a1[1])
    a1z_list.append(a1[2])

    a2x_list.append(a2[0])
    a2y_list.append(a2[1])
    a2z_list.append(a2[2])

    a3x_list.append(a3[0])
    a3y_list.append(a3[1])
    a3z_list.append(a3[2])

    wv1x += a1[0] * delta_t
    wv1y += a1[1] * delta_t
    wv1z += a1[2] * delta_t

    wv2x += a2[0] * delta_t
    wv2y += a2[1] * delta_t
    wv2z += a2[2] * delta_t

    wv3x += a3[0] * delta_t
    wv3y += a3[1] * delta_t
    wv3z += a3[2] * delta_t

    v1x_list.append(wv1x)
    v1y_list.append(wv1y)
    v1z_list.append(wv1z)

    v2x_list.append(wv2x)
    v2y_list.append(wv2y)
    v2z_list.append(wv2z)

    v3x_list.append(wv3x)
    v3y_list.append(wv3y)
    v3z_list.append(wv3z)

    hx1 += wv1x * delta_t
    hy1 += wv1y * delta_t
    hz1 += wv1z * delta_t

    hx2 += wv2x * delta_t
    hy2 += wv2y * delta_t
    hz2 += wv2z * delta_t

    hx3 += wv3x * delta_t
    hy3 += wv3y * delta_t
    hz3 += wv3z * delta_t

    x1_list.append(hx1)
    y1_list.append(hy1)
    z1_list.append(hz1)

    x2_list.append(hx2)
    y2_list.append(hy2)
    z2_list.append(hz2)

    x3_list.append(hx3)
    y3_list.append(hy3)
    z3_list.append(hz3)

    x_coord_list_for_a = [wx1, wx2, wx3]
    y_coord_list_for_a = [wy1, wy2, wy3]
    z_coord_list_for_a = [wz1, wz2, wz3]

    a1 = get_a_i(0, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
    a2 = get_a_i(1, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)
    a3 = get_a_i(2, m, x_coord_list_for_a, y_coord_list_for_a, z_coord_list_for_a)

    a1x_list.append(a1[0])
    a1y_list.append(a1[1])
    a1z_list.append(a1[2])

    a2x_list.append(a2[0])
    a2y_list.append(a2[1])
    a2z_list.append(a2[2])

    a3x_list.append(a3[0])
    a3y_list.append(a3[1])
    a3z_list.append(a3[2])

    hv1x += a1[0] * delta_t
    hv1y += a1[1] * delta_t
    hv1z += a1[2] * delta_t

    hv2x += a2[0] * delta_t
    hv2y += a2[1] * delta_t
    hv2z += a2[2] * delta_t

    hv3x += a3[0] * delta_t
    hv3y += a3[1] * delta_t
    hv3z += a3[2] * delta_t

    v1x_list.append(hv1x)
    v1y_list.append(hv1y)
    v1z_list.append(hv1z)

    v2x_list.append(hv2x)
    v2y_list.append(hv2y)
    v2z_list.append(hv2z)

    v3x_list.append(hv3x)
    v3y_list.append(hv3y)
    v3z_list.append(hv3z)

    t += delta_t



ax.plot3D(x1_list, y1_list, z1_list, color="darkblue", label='Body 1')
ax.plot3D(x2_list, y2_list, z2_list, color="tab:red", label='Body 2')
ax.plot3D(x3_list, y3_list, z3_list, color="green", label='Body 3')

ax.set_xlabel("x-coordinate", fontsize=14)
ax.set_ylabel("y-coordinate", fontsize=14)
ax.set_zlabel("z-coordinate", fontsize=14)
ax.set_title("Visualization of orbits of stars in a three-body system\n", fontsize=14)
ax.legend(loc="upper left", fontsize=14)

plt.show()

# fig = plt.figure()
# ax = plt.axes(projection="3d")
#
# data_skip = 50
# #
# def init_func():
#     ax.clear()
#     plt.xlabel('time')
#     plt.ylabel('theta')
#
#
# def animating(i):
#     ax.plot3D(x1_list[i:i+data_skip], y1_list[i:i+data_skip], z1_list[i:i+data_skip], color='red')
#     ax.plot3D(x2_list[i:i + data_skip], y2_list[i:i + data_skip], z2_list[i:i + data_skip], color='blue')
#     ax.plot3D(x3_list[i:i + data_skip], y3_list[i:i + data_skip], z3_list[i:i + data_skip], color='green')
#
#
#
# anim = FuncAnimation(fig, animating, frames=np.arange(0, len(x1_list), data_skip), init_func=init_func, interval=100)
#
# plt.show()
#
# anim.save('twobodygif.mp4', dpi=150, fps=60, writer='ffmpeg')