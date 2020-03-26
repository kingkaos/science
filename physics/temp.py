import numpy as np

import constants as const


def capillary(radius, gravitation=const.gravitation_constant):
    surface_tension = 0.0728
    density = 1000.
    height = (
        2. * surface_tension * np.cos(20/360 * np.pi)
        ) / (density * gravitation * radius)
    # print('Hello World! ', gravitation)
    return height


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x = np.arange(0.01e-3, 10e-3, 0.01e-3)
    y = np.asarray([capillary(i) for i in x])
    print(y)
    plt.plot(x, y)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('radius of capillary')
    plt.ylabel('minimum height')
    plt.show()
