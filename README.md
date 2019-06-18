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
 
The MIT License (MIT)

Copyright (c) 2015 Chris Kibble

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
