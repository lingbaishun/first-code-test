import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf


def himmelblau(x):
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


x = np.arange(-6, 6, 0.1)
y = np.arange(-6, 6, 0.1)

X, Y = np.meshgrid(x, y)

Z = himmelblau([X, Y])

fig = plt.figure('himmmelbau')
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z)
ax.view_init(60, -30)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()


x = tf.constant([-4., 0.])

for step in range(200):
    with tf.GradientTape as tape:
        tape.watch([x])
        y = himmelblau(x)

    grads = tape.gradient(y, [x])[0]
    x -= 0.01 * grads

    if step % 30 == 0:
        print('step {}: x = {}, f(x) = {}'.format(step, x.numpy(), y.numpy()))



