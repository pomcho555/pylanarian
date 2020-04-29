https://img.shields.io/github/license/pomcho555/pylanarian
# pylanarian

A plotting package for real time and animation.
It is EASY to visualize your IoT sensor data.
It could be multi-plot using subplot.
It works up to 16th graphs.

![demo](https://raw.github.com/wiki/pomcho555/pylanarian/images/graph_animation.gif)


## Prequisite
- python3.5+
- matplotlib

## Get Started,
`git clone https://github.com/pomcho555/pylanarian.git`  
`cd <installed directory>`  
`pip install -e .` 

## Tutorial
import modules   
`from pylanarian import SequentialGraph`   
`from pylanarian import GraphManager`   

1. Make a graph instance. You can use various options!   
`g1 = SequentialGraph(title="sin", margin=0.1)`   
Also instantiate a second graph.   
`g2 = SequentialGraph(title="cos", option=".r", margin=0.1)`   
1. Then bind graphs to <span style="color: red; ">GraphManager</span>  
`GM = GraphManager(g1, g2)`   
Also, you could write list type.   
`GM = GraphManager(*[g1, g2])`   
1. Initilize plot configure.   
`GM.init_plot()`   
1. Put data into GM(before this you prepare list type data)   
`GM.set_alldata(x, y1, y2) # y1 is g1's parameter, and y2 is also g2's`   
1. After put the data, you must pause.   
`GM.pause(0.1)`   

You can demonstorate sample script on /samples/ directory.   
`python sample.py`   
Real time plot version is:   
`python realtime_sample.py`   

## License
 
[MIT](./LICENSE)
