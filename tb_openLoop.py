## Scenario 1: x = vt

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

    desired_displacement = 10  # The desired displacement in front of the robot
    desired_time = 10   # desired time to execute the action

    # Open Loop Velocity Controller based on time and displacement 
    desired_velocity = desired_displacement / desired_time


    # Move robot at the desired x velocity
    twist.linear.x = desired_velocity
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)

    # Have the robot move for the right amount of time at the right velocity x = vt
    time.sleep(desired_time)

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
