# -*- Coding: utf-8 -*-
from pylanarian import SequentialGraph
from pylanarian import GraphManager
import numpy as np

def main():
    x = np.arange(0,10,0.1)
    g1 = SequentialGraph(title="sin", margin=0.1)
    g2 = SequentialGraph(title="cos", option=".r", margin=0.1)
    GM = GraphManager(g1,g2)
    GM.init_plot()
    t = 0
    while True:
        x += 0.1
        y1 = np.sin(x)
        y2 = np.cos(x)
        GM.set_alldata(x, y1, y2)
        GM.pause(0.1)
        
        
if __name__ == '__main__':
    main()