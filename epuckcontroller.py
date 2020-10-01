"""pi_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor

# create the Robot instance.
robot = Robot()

MAX_SPEED = 6.28
speed = 0.9 * MAX_SPEED
counter = 0
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

states = ['forward', 'turn_right', 'turn_left']
current_state = states[0]

gs = []
gsNames = ['gs0', 'gs1', 'gs2']
for i in range(3):
    gs.append(robot.getDistanceSensor(gsNames[i]))
    gs[i].enable(timestep)

# motors
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    gsValues = []
    for i in range(3):
        gsValues.append(gs[i].getValue())

    print(gsValues[0], gsValues[1], gsValues[2])

    line_right = gsValues[0] > 600
    line_left = gsValues[2] > 600

    if current_state == states[0]:
        leftSpeed = speed
        rightSpeed = speed
        if line_right and not line_left:
            current_state = states[1]
            counter = 0
        elif line_left and not line_right:
            current_state = states[2]
            counter = 0

    if current_state == states[1]:
        leftSpeed = speed
        rightSpeed = 0.4 * speed
        if counter == 9:
            current_state = states[0]

    if current_state == states[2]:
        leftSpeed = 0.4 * speed
        rightSpeed = speed
        if counter == 9:
            current_state = states[0]

    counter += 1

    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
    print(current_state)
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
