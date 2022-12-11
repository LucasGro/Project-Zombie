import time
import matplotlib.pyplot as plt


def visualize_simulation(humans, zombies, map2d, t, clf=True):
    showmap = map2d.copy()

    for h in humans:
        x = round(h.x)
        y = round(h.y)
        showmap[y-1:y+1, x-1:x+1] = 0.8

    for z in zombies:
        x = round(z.x)
        y = round(z.y)
        showmap[y-1:y+1, x-1:x+1] = 0.5

    # if t % 5 == 0:
    plt.figure("Simulation")  #
    plt.imshow(showmap, cmap="nipy_spectral", vmin=0, vmax=1)
    plt.title("Time step: " + str(t), fontsize=16)
    plt.show(block=False)
    if clf:
        plt.pause(0.5)
        plt.clf()
    else:
        time.sleep(3)
    # time.sleep(.5)
    # plt.close('all')

