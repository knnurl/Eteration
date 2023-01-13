#!/usr/bin/env python3

#import required libraries for unittest to work
import unittest
import rospy
from std_msgs.msg import String
from time import sleep
import rostest

#definition of class for unittest
class TalkerTestCase(unittest.TestCase):
	
#wait for installation unit test to finish
	sleep(6)
	print("\n\n***composiv_talker unit test started!***\n\n")	
#we first set the okay condition to False to prevent false positive results
	talker_ok = False

#if the the node works properly and callback function is called,
# this method sets the okay condition to True
	def callback(self, data):
		self.talker_ok = True

#given that this rospy is running, this method checks if there's an  
# upcoming message in topic "chatter" which the talker node publishes to
# and then calls the callback function for required indication
# if there is no messages in the topic, the method keeps listening for 
# 5 seconds and then terminates.
	def test_if_talker_publishes(self):
		rospy.init_node('test_talker')
		rospy.Subscriber('/chatter', String, self.callback)

		counter = 0
		while not rospy.is_shutdown() and counter < 5 and (not self.talker_ok):
			sleep(1)
			counter += 1

		self.assertTrue(self.talker_ok)

	
#rostest wrapper is required since this test is meant to be a ROS node launched via rostest
if __name__ == '__main__':
	rostest.rosrun('composiv_tryouts', 'test_talker', TalkerTestCase)
