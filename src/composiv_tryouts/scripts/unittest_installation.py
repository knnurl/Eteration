#!/usr/bin/env python3
PKG = 'rostest'
import roslib; roslib.load_manifest(PKG)  # This line is not needed with Catkin.

import sys
import unittest

## A sample python unit test
print("\n\n\n*** Starting the installation unit test*** \n") 
        
#definition of class for unittest
class TestBareBones(unittest.TestCase):
    ## test 1 == 1

    def test_one_equals_one(self): # only functions with 'test_'-prefix will be run!

        self.assertEquals(1, 1, "1!=1")

#rostest wrapper is required since this test is meant to be a ROS node launched via rostest
if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_bare_bones', TestBareBones)
    
    
