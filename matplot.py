import numpy as np
import matplotlib.pyplot as plt
def pic_maker(list) :
    exx = (list[0][1], list[1][1], list[2][1], list[3][1], list[4][1], list[5][1], list[6][1])
    value = (list[0][0], list[1][0], list[2][0], list[3][0], list[4][0], list[5][0], list[6][0])
    position = np.arange(7)

    fig, ax = plt.subplots()

    ax.bar(position, value, color='orange')

    #  Устанавливаем позиции тиков:
    ax.set_xticks(position)

        #  Устанавливаем подписи тиков
    ax.set_xticklabels([list[0][1], list[1][1], list[2][1], list[3][1], list[4][1], list[5][1], list[6][1]])

    fig.set_figwidth(13)
    fig.set_figheight(7)
    fig.savefig('photos/graphic.png')