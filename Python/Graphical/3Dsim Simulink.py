import vpython as v
import numpy as np
import socket
import struct 
import time
from datetime import datetime

# vpython documentation: https://www.glowscript.org/docs/VPythonDocs/objects.html#

# SQUARE POOL
#poolWall_n = v.box(pos=v.vector(0,1.9,-5.1), color=v.color.white, length=16, width=.2, height=3.8)
#poolWall_s = v.box(pos=v.vector(0,1.9,5.1),color=v.color.white, length=16, width=.2, height=3.8)
#poolWall_e = v.box(pos=v.vector(8.1,1.9,0), color=v.color.white, length=.2, width=10, height=3.8)
#poolWall_w = v.box(pos=v.vector(-8.1,1.9,0), color=v.color.white, length=.2, width=10, height=3.8)
#poolFloor = v.box(pos=v.vector(0,0,0), color=v.color.white, length=16, width=10, height=.1)
#poolWater = v.box(pos=v.vector(0,1.9,0), texture=v.textures.stucco, opacity=.85, length=16, width=10, height=3.8)

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
poolWater = v.cylinder(pos=v.vec(0,0,0), axis=v.vec(0,poolLevelStart,0), radius=7.36, texture=v.textures.waterClear, opacity=.85)

light = v.local_light(pos=v.vec(0,7,10), color=v.color.white)

# display 3D text
#tankLevel = v.text(pos=v.vec(0,4.5,0), text='Nivå: 0 m', align='center', billboard=True, color=v.color.white)
#flowIn = v.text(pos=v.vec(0,4.5,6), text='Flow Inn: 0 m3/t', align='center', billboard=True, color=v.color.white)
#flowOut = v.text(pos=v.vec(0,4.5,-6), text='Flow Ut: 0 m3/t', align='center', billboard=True, color=v.color.white)

# display text
tankLevel = v.label(pos=v.vec(0,4.5,0), text='Nivå: {} m'.format(round(0)))
flowIn = v.label(pos=v.vec(0,4.5,6), text='Flow Inn: {} m3/t'.format(round(0)))
flowOut = v.label(pos=v.vec(0,4.5,-6), text='Flow Ut: {} m3/t'.format(round(0)))

def setLevel(level):
    # Round pool
    poolWater.axis = v.vec(0,level,0)

    # Square pool
    #poolWater.height = level
    #poolWater.pos = v.vec(0,level/2,0)

# Set up a TCP/IP server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Bind the socket to server address and port 81
server_address = ('localhost', 8080)
tcp_socket.bind(server_address)
 
# Listen on port 81
tcp_socket.listen(1)

while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()
 
    try:
        print("Connected to client IP: {}".format(client))
         
        # Receive and print data 32 bytes at a time, as long as the client is sending something
        while True:
            # FLUSH the packet queue
            connection.setblocking(0)  # Set socket to non-blocking mode
            try:
                while True:
                # Try to read any outstanding bytes
                    connection.recv(1024)
            except BlockingIOError:
                pass
            connection.setblocking(1)  # Set socket back to blocking mode

            # READ
            data = connection.recv(32)
            float_value1 = struct.unpack('<d', data[:8])[0]
            float_value2 = struct.unpack('<d', data[8:16])[0]
            float_value3 = struct.unpack('<d', data[16:24])[0]
            
            # print values from simulink
            current_timestamp = datetime.now()
            print(current_timestamp)
            print(float_value1,float_value2,float_value3)
            print("")

            # update sim values
            currentLevel = round(float_value2*0.01*poolHeight,1)
            currentFlowIn = round(float_value1,1)
            currentFlowOut = round(float_value3,1)

            # display text
            tankLevel.text='Nivå: {} m'.format(currentLevel)
            flowIn.text='Flow Inn: {} m3/t'.format(currentFlowIn,1)
            flowOut.text='Flow Ut: {} m3/t'.format(currentFlowOut,1)

            # update tank level
            setLevel(currentLevel)

            # wait
            time.sleep(3)
            
            if not data:
                break
 
    finally:
        connection.close()