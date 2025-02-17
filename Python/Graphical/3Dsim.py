import vpython as v
import numpy as np

# vpython documentation: https://www.glowscript.org/docs/VPythonDocs/objects.html#

# SQUARE POOL
# pool 
#poolWall_n = v.box(pos=v.vector(0,1.9,-5.1), color=v.color.white, length=16, width=.2, height=3.8)
#poolWall_s = v.box(pos=v.vector(0,1.9,5.1),color=v.color.white, length=16, width=.2, height=3.8)
#poolWall_e = v.box(pos=v.vector(8.1,1.9,0), color=v.color.white, length=.2, width=10, height=3.8)
#poolWall_w = v.box(pos=v.vector(-8.1,1.9,0), color=v.color.white, length=.2, width=10, height=3.8)
#poolFloor = v.box(pos=v.vector(0,0,0), color=v.color.white, length=16, width=10, height=.1)
# water 
#poolWater = v.box(pos=v.vector(0,1.9,0), color=v.color.blue, opacity=.75, length=16, width=10, height=3.8)

# ROUND POOL
poolVolume = 680 #m3
poolHeight = 4 #m
poolWallThickness = 0.2 #m
poolLevelStart = 3 #m
poolArea = poolVolume/poolHeight
poolRadiusInner = np.sqrt(poolArea/np.pi)
poolRadiusOuter = poolRadiusInner + (2*poolWallThickness)

print(round(poolRadiusInner,2))
print(round(poolRadiusOuter,2))
linepath = [ v.vec(0,0,0), v.vec(0,4,0) ]
poolWall = v.extrusion( shape=[v.shapes.circle(radius=7.36),v.shapes.circle(radius=7.76)], path=linepath, color=v.color.white)
poolFloor = v.cylinder(pos=v.vec(0,0,0), axis=v.vec(0,-0.2,0), radius=7.76, color=v.color.white)

poolWater = v.cylinder(pos=v.vec(0,0,0), axis=v.vec(0,poolLevelStart,0), radius=7.36, texture=v.textures.water, opacity=.85)

light = v.local_light(pos=v.vec(0,7,10), color=v.color.white)

# display text
tankLevel = v.text(pos=v.vec(0,4.5,0), text='Nivå: 0 m', align='center', billboard=True, color=v.color.white)
flowIn = v.text(pos=v.vec(0,4.5,6), text='Flow Inn: 0 m3/t', align='center', billboard=True, color=v.color.white)
flowOut = v.text(pos=v.vec(0,4.5,-6), text='Flow Ut: 0 m3/t', align='center', billboard=True, color=v.color.white)

def setLevel(level):
    #poolWater.pos = v.vector(0,level/2,0)
    #poolWater.height = level
    poolWater.axis = v.vec(0,level,0)
    print(level)

v.sleep(3)
for i in range(15):
    setLevel(poolLevelStart-0.1*i)
    v.sleep(0.2)

#v.sleep(5)
#myBox.color = v.color.yellow

# keep alive
while True:
    pass