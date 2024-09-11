## Scenario 2: x = vt

import rclpy
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
import time 

def main():

    # Initialize Node and Publishing Information
    rclpy.init()
    node = rclpy.create_node('tb_openLoop')
    qos = QoSProfile(depth=10)
    node = rclpy.create_node('teleop_keyboard')
    pub = node.create_publisher(Twist, 'cmd_vel', qos)
    twist = Twist()


    # Open Loop Velocity Controller based on time and displacement 
    acceleration = .5 
    max_velocity = 2.0
    velocity = 0.0
    desired_displacement = 3.0
    update_rate = .1

    # This while loop will accelerate the robot to the desired max speed
    print('Accelerating!')
    while velocity < max_velocity:
        velocity = velocity + acceleration*.1

        # Move robot at the desired x velocity
        twist.linear.x =  velocity
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)

        time.sleep(.1)

    # Once at speed move robot the distance of the desired displacement
    print('Max Speed!') 
    twist.linear.x =  max_velocity
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)
    time.sleep(desired_displacement/max_velocity) #Time needed to cover the desired displacement 

    print('Slowing Down!')
    while velocity > 0:
        velocity = velocity - acceleration*.1

        # Move robot at the desired x velocity
        twist.linear.x =  velocity
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)
        time.sleep(.1)

    print('Stop!')
    # Stop the Robot
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)

if __name__ == '__main__':
    main()
