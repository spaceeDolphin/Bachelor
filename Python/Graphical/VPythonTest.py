from vpython import *

#triangleshape = [ [2,0], [0,4], [-2,0], [2,0] ]
triangleshape = shapes.circle(radius=5)
linepath = [ vec(0,0,0), vec(0,4,0) ]
wedge = extrusion( shape=[shapes.circle(radius=5.0),shapes.circle(radius=4.5)], path=linepath, color=color.magenta)

# keep alive
while True:
    pass