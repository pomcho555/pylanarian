# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
from abc import ABC
from abc import abstractmethod

__all__ = ['SequentialGraph', 'GraphManager']

# Font configurations
font = {'family':'monospace', 'size':'9'}
mpl.rc('font', **font)

class SubGraph(ABC):
    def __init__(self, x=[-1,-1], y=[1,1], option="b",\
        title="The graph", x_label="x", y_label="y", **kwargs):
        """
        Parameters
        ----------
        x: list of float or integer
        A initial value of x.

        y: list of flaot or integer
        A initial value of y.

        option: str
        A plot option such as color and dot.
        Learn more => https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

        title: str
        A title of this graph

        x_label: str
        A label name of this graph's x.

        y_label: str
        A label name of this graph's y.

        y_lim: tuple of integer
        A range of graph's y you see.

        maring: float
        upper and lower margin of y.
        """
        self.x = x
        self.y = y
        self.option = option
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        if 'y_lim' in kwargs: self.y_lim = kwargs['y_lim']
        if 'margin' in kwargs: self.margin = kwargs['margin']
        # A keyword value name is used to identify instance.
        if 'name' in kwargs: self.name = kwargs['name']
        
    @abstractmethod
    def initialize_graph(self, nrows, ncols, index):
        pass

    @abstractmethod
    def set_data(self, x,y):
        pass

class SequentialGraph(SubGraph):
    """
    A standard graph which shows sequential data like IoT sensor data.
    """
    def initialize_graph(self, nrows, ncols, index):
        self.ax = plt.subplot(nrows, ncols, index)
        self.ax.grid(True)
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        # initialize a plot
        self.lines, = self.ax.plot(self.x, self.y, self.option)

    def set_data(self, x, y):
        self.lines.set_data(x, y)
        self.ax.set_xlim((min(x), max(x)))
        if 'y_lim' in self.__dict__.keys(): self.ax.set_ylim(self.y_lim)
        elif 'margin' in self.__dict__.keys(): self.ax.set_ylim((min(y)-self.margin, max(y)+self.margin))
        else: self.ax.set_ylim((min(y), max(y)))

 
class GraphManager():
    def __init__(self, *graphs):
        self.graphs = graphs

    def init_plot(self):
        self.fig = plt.figure(figsize=(12,8))
        self.fig.subplots_adjust(left=0.05, bottom=0.1, right=0.95, \
            top=0.90, wspace=0.2, hspace=0.6)
        grid_row = calc_grid(len(self.graphs))
        cnt = 1
        for g in self.graphs:
            g.initialize_graph(grid_row,grid_row,cnt)
            cnt += 1

    def set_alldata(self,x, *y):
        y_ix = 0
        for g in self.graphs:
            try:
                g.set_data(x, y[y_ix])
            except IndexError:
                print("Input the correct number of ys!")
            y_ix += 1

    def pause(self, sec=0.5):
        plt.pause(sec)

def calc_grid(n_graphs):
    return math.ceil(math.sqrt(n_graphs))
