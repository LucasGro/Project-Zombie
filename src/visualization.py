
import matplotlib.pyplot as plt


def visualize_simulation(humans, zombies, map2d, t):
    map2d_cp = map2d.copy()
    for h in humans:
        x = round(h.x)
        y = round(h.y)
        map2d_cp[y-1:y+1, x-1:x+1] = 0.8

    for z in zombies:
        x = round(z.x)
        y = round(z.y)
        map2d_cp[y-1:y+1, x-1:x+1] = 0.5

    plt.figure("Symulacja")
    plt.imshow(map2d_cp, cmap='nipy_spectral', vmin=0, vmax=1)
    plt.title(f"Symulacja {t}", fontsize=15)
    plt.show(block=False)

    plt.pause(0.5)
    plt.clf()
