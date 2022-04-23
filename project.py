from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor,LandmarkMap
from math import pi , atan2
import matplotlib.pyplot as plt

# This function uses the RangeBearingSensor to detect the position of obstacles
def detect_obstacles(veh, map):
    sensor = RangeBearingSensor(robot = veh, map = map ,animate=True)
    readings = sensor.h(veh.x)
    return readings

anim = VehicleIcon('robot', scale = 2)

#creating lists to store the initial and position values
initpos = [0, 0, 0];
targetpos = [None]*2

#getting the target positions inputs from the user
targetpos[0] = float(input("Enter target x co-ordinate: "))
targetpos[1] = float(input("Enter target y co-ordinate: "))

#getting the initial position inputs from the user
initpos[0] = float(input("Enter initial x co-ordinate: "))
initpos[1] = float(input("Enter initial y co-ordinate: "))
initpos[2] = float(input("Enter initial theta: "))

#getting the number of obstacles from the user
no_obstacles = int(input("Enter the number of obstacles: "))

#creating an instance of the bicycle class (our robot)
veh = Bicycle(
animation = anim,
control = RandomPath,
dim = 10,
x0=initpos,
)

veh.init(plot=True)
veh._animation.update(veh.x)

#marking the target position on the map
target_marker_style = {
    "marker": "D",
    "markersize" : "6",
    "color" : "g",
}
plt.plot(targetpos[0], targetpos[1], **target_marker_style)

#creating obstacles on the map
map = LandmarkMap(no_obstacles, 20)
map.plot()

#using the detect_obstacles function to get the positions of the obstacles
sensor_readings = detect_obstacles(veh, map)
print(sensor_readings)


#this while loop will keep running until run = False
run = True
while(run):
    #checks every sensor reading to see if it is less than 3 units away 
    for i in sensor_readings:
        # if it is less than 3 and is in the way of the robot the robot will stop
        if (i[0] < 3):
            if(abs(i[1]) < pi/4):
                run = False
                
        # otherwise the robot will continue to move towards the target point
        else:
            #calculating the target heading relevant to the robot position
            target_heading = atan2(
                targetpos[1] - veh.x[1],
                targetpos[0] - veh.x[0]
            )
            #calculating the steering angle
            steer = target_heading-veh.x[2]
            if steer > pi:
                steer = steer-2*pi
            veh.step(0.8, steer)
            if((abs(targetpos[0]-veh.x[0]) > 0.3) or (abs(targetpos[1]-veh.x[1]) > 0.3)):
                run = True
            else:
                run = False
            
            veh._animation.update(veh.x)
            plt.pause(0.005)

plt.pause(100)
