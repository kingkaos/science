import numpy as np

from . import constants as const


def capillary(radius, surfTens, gravitation=const.gravitation_constant):
    surface_tension = surfTens
    density = 1000.
    height = (
        2. * surface_tension * np.cos(90/360 * np.pi)
        ) / (density * gravitation * radius)
    # print('Hello World! ', gravitation)
    return height


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    surfTens = 0.0728
    x = np.arange(0.05e-3, 2e-3, 0.01e-3)
    y1 = np.asarray([capillary(i, surfTens) for i in x])
    y2 = np.asarray([capillary(i, surfTens * 1.1) for i in x])
    y3 = np.asarray([capillary(i, surfTens * 0.9) for i in x])

    plt.plot(x * 1e3, y1 * 1e2, label='surface tension 0.0728 (J/m^2)')
    plt.plot(x * 1e3, y2 * 1e2, label='surface tension 0.0801 (J/m^2)')
    plt.plot(x * 1e3, y3 * 1e2, label='surface tension 0.0655 (J/m^2)')
    plt.legend(loc="upper right")
    plt.grid()
    plt.xscale('log')
    # plt.yscale('log')
    plt.xlabel('radius of capillary (mm)')
    plt.ylabel('minimum height (cm)')
    plt.show()
