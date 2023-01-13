v# Eteration Case Study
**This repository is contains basic filesystem operations in ROS Noetic, namely workspace, package and launch file configurations, node-to-node communications and is created befittingly regarding the requirements and standards set by Eteration.**

Files include publisher-sucscriber nodes, unit tests, respective launch files as well as the documentation.

ROS Noetic Ninjemys  
Version 1.0  
Kaan Ural  
Created on 13.01.2023  


## Summary
 The work done here is to establish the Robot Operating System middleware and make use of its communication functions. ROS is a modular framework meaning that there are several integrated processes, called nodes on top of the "roscore" which is the main communication ground for nodes. The work is done by creating to nodes in a way that one sends a message, and the other one receives it, then verifying the process.   
 

![alt text](https://www.clearpathrobotics.com/assets/guides/melodic/ros/_images/ros101four.png)

For a better organization of the filesystem, ROS allows for multiple workspaces and these workspaces contain packages that are the parent directory of folders containing source files, configurations, launch files etc.

![alt text](https://www.oreilly.com/api/v2/epubs/9781788627436/files/assets/070b1970-a7b7-43b5-93c6-b4aff111747c.png)


Having ROS Noetic already installed on the machine, the work began direcly by creating the necessary files.

Chronological creation order these is as follows:
eter_ws workspace, 
composiv_tryouts package, 
composiv_talker and composiv_listener nodes,
composiv_tryouts.launch launch file,
unittest_installation, unittest_talker and unittest_listener unit test nodes,
composiv_unittests.launch launch file.



 ## References

http://wiki.ros.org/ROS/Tutorials
http://wiki.ros.org/rostest/Writing
https://ut-ims-robotics.github.io/ros_training/html/day3/workshop_2.html
https://www.theconstructsim.com/ros-qa-098-see-ros-publisher-works-using-ros-unit-testing/
https://www.oreilly.com/library/view/ros-programming-building/9781788627436/1eae3e27-e039-4a9c-996b-3ed068f69a95.xhtml
https://www.clearpathrobotics.com/assets/guides/melodic/ros/Intro%20to%20the%20Robot%20Operating%20System.html
