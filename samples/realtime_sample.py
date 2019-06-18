# -*- Coding: utf-8 -*-
from pylanarian import SequentialGraph
from pylanarian import GraphManager
import math
import numpy as np

def main():
    times = [0 for i in range(10)]
    sinxs = [0 for i in range(10)]
    cosxs = [0 for i in range(10)]
    g1 = SequentialGraph(title="sin", margin=0.1)
    g2 = SequentialGraph(title="cos", option=".r", margin=0.1)
    GM = GraphManager(g1, g2)
    GM.init_plot()
    t = 0
    while True:
        t += 0.5
        times.append(t)
        times.pop(0)

        sinx = math.sin(t)
        sinxs.append(sinx)
        sinxs.pop(0)

        cosx = math.cos(t)
        cosxs.append(cosx)
        cosxs.pop(0)

        GM.set_alldata(times, sinxs, cosxs)
        GM.pause(0.1)

if __name__ == '__main__':
    main()