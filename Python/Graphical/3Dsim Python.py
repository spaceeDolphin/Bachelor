#
#   3D TANK SIMULATION USING simLog.csv
#

import vpython as v
import numpy as np
import time
import pandas as pd

# Pool parameters
poolVolume = 680 #m3
poolHeight = 4 #m
poolWallThickness = 0.2 #m
poolLevelStart = 3 #m
poolArea = poolVolume/poolHeight
poolRadiusInner = np.sqrt(poolArea/np.pi)
poolRadiusOuter = poolRadiusInner + (2*poolWallThickness)

# ROUND POOL
linepath = [ v.vec(0,0,0), v.vec(0,4,0) ]
poolWall = v.extrusion( shape=[v.shapes.circle(radius=7.36),v.shapes.circle(radius=7.76)], path=linepath, color=v.color.white)
#poolWall = v.extrusion( shape=[v.shapes.circle(radius=7.36),v.shapes.circle(radius=7.76)], path=linepath, texture=v.textures.emiel)
poolFloor = v.cylinder(pos=v.vec(0,0,0), axis=v.vec(0,-0.2,0), radius=7.76, color=v.color.white)
#poolFloor = v.cylinder(pos=v.vec(0,0,0), axis=v.vec(0,-0.2,0), radius=7.76, texture=v.textures.emiel)
poolWater = v.cylinder(pos=v.vec(0,0,0), axis=v.vec(0,poolLevelStart,0), radius=7.36, texture=v.textures.water, opacity=.85)

light = v.local_light(pos=v.vec(0,7,10), color=v.color.white)

# display text
tankLevel = v.label(pos=v.vec(0,4.5,0), text='Nivå: {} m'.format(round(0)))
flowIn = v.label(pos=v.vec(0,4.5,6), text='Flow Inn: {} m3/t'.format(round(0)))
flowOut = v.label(pos=v.vec(0,4.5,-6), text='Flow Ut: {} m3/t'.format(round(0)))

def setLevel(level):
    poolWater.axis = v.vec(0,level,0)

while True:
    df = pd.read_csv('Python\Simulator\simLog.csv')
    currentLevel = round(df['Level'].iloc[-1],1)
    currentFlowIn = round(df['Qin'].iloc[-1],1)
    currentFlowOut = round(df['Qout'].iloc[-1],1)
    print(f'Level: {currentLevel}, F_in: {currentFlowIn}, F_out: {currentFlowOut}')
    # display text
    tankLevel.text='Nivå: {} %'.format(currentLevel)
    flowIn.text='Flow Inn: {} m3/t'.format(currentFlowIn,1)
    flowOut.text='Flow Ut: {} m3/t'.format(currentFlowOut,1)
    setLevel(currentLevel*0.01*poolHeight)
    time.sleep(2)
       
