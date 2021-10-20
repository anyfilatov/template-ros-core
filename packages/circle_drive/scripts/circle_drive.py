#!/usr/bin/env python3
import os
import rospy
from duckietown.dtros import DTROS, NodeType
from duckietown_msgs.msg import Twist2DStamped, StopLineReading

class MyNode(DTROS):

    def __init__(self, node_name):
        super(MyNode, self).__init__(node_name=node_name, node_type=NodeType.DEBUG)
        self.pub = rospy.Publisher("~car_cmd", Twist2DStamped, queue_size=1)
        self.sub_stop_line = rospy.Subscriber("stop_line_filter_node/stop_line_reading", StopLineReading, self.cb_stop_line)

    def cb_stop_line(self, msg):
        print("cb_stop_line():")
        print(msg.stop_line_detected)
        print(msg.stop_line_point.x)

    def run(self):
        # publish message every 1 second
        rate = rospy.Rate(0.5) # 1Hz
        while not rospy.is_shutdown():
            msg = Twist2DStamped()
            msg.v = 0.0
            msg.omega = 5.0
            rospy.loginfo("Publishing message")
           # self.pub.publish(msg)
            rate.sleep()
            msg.omega = 0.0
            rospy.loginfo("Publishing message -")
           # self.pub.publish(msg)
            rate.sleep()

if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='circle_drive_node')
    # run node
    node.run()
    # keep spinning
    rospy.spin()
