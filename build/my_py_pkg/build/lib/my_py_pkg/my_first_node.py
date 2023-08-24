#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Test")
        self.create_timer(1, self.timer_callback) #calls timer_callback every 1 sec

    #prints hello [x] every time it's called - x is the call amount
    def timer_callback(self):
        self.counter_ += 1 
        self.get_logger().info("Hello " + str(self.counter_)) 

def main(args=None):
    rclpy.init(args=args) #stars ros2 comms

    node = MyNode() #creates a node obj 

    rclpy.spin(node) #important function - allows pgrm to still run and wait for callbacks, etc later on - ctrl+c to stop spin
    
    rclpy.shutdown() #shutsdown ros2 comms

if __name__ == "__main__":
    main()