#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
from example_interfaces.msg import String
 
class RobotNewsStationNode(Node): 
    def __init__(self):
        super().__init__("robot_news_station") #name of node is same name of class & class - ROS standard
        
        #creates a publisher                    data type, topic name Queue size - 10 messages will be kept
        self.publisher_ = self.create_publisher(String, "robot_news", 10)
        
        #creates a timer that calls publish_news every second
        self.timer = self.create_timer(1, self.publish_news)
        
        #Outputs once, lets user know the news station has been started
        self.get_logger().info("Robot News Station has been started")
    
    #publishes "Hello" everytime it's called
    def publish_news(self):
        msg = String()
        msg.data = "Hello!"
        self.publisher_.publish(msg)
 
def main(args=None):
    #start comms
    rclpy.init(args=args)
    
    #creates node(s)
    node = RobotNewsStationNode() 
    
    #spins node
    rclpy.spin(node)

    #shutsdown comms
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()