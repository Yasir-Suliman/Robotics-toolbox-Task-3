# Robotics-toolbox-Task-3
## Contributers:
#### _Yasir Ahmed Ali Ahmed Suliman 202101327_
#### _Mohammedahmed Emadeldin Ahmed Mohammed 202101449_
This is our Computer Engineering roboticstoolbox task where a robot is given a target point to reach and a number of random obstacles are generated on the map and the robot has to reach the target point without colliding with the obstacles.

## Code Output:
![Image of code output](/map.png)

When the program is run, the output seen is the robot moving along the map steering itself towards the target avoiding the obstacles

## User Inputs:
#### The program requires Input from the User for the robot. These Are:
1. Target positions:
The User must specify the X and Y co-ordinate of the target position
2. Initial positions:
The User must specify the X and Y co-ordinate of the Initial position and the angle.
3. Number of obstacles:
The User must specify the number of obstacles to be randomly generated on the map

## Dependencies required and software versions
1. Roboticstoolbox library: The library can be downloaded from [Here](https://github.com/petercorke/robotics-toolbox-python).
2. Python 3: Any python version from 3.6 - 3.8.

## Code Explanation
The way the code works is firstly a map is generated with obstacles using inputs from the user and the target position is identified. Then using the range bearing sensor the obstacles are identified and how far is the robot from them. If the there is no obstacles within 3 units of the robot then the robot starts calculating the steering angle to get to the target relative to its position. The robot will keep moving until it reaches the target position. In the case where an obstacle is within 3 units of the robot then the robot will stop to avoid collision.

#### Flowchart
![Image of flowchart](/flowchart.png)

## Results
![Image of robot at target](/success.png)
##### The green dot represents the target point.
##### The black marks represent the obstacles.
The Robot stops when it successfully reached the target position

## Further Improvement
The main problem in this code is when there is an obstacle within 3 units from the robot. Implementing a method where the robot can reverse itself and turn away from the obstacle.
