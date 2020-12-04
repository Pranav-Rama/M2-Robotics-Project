<h1 align="center"> Robotics Project </h1> <br>
<p align="center">
University Of Burgundy (VIBOT)
  <p align="center">
      <img src = "vibot.png" width=60>
  </p>
</p>

<h3 align="center">                       
Supervisors: <br>  
 Ralph SEULIN <br>
 Daniel BRAUN
</h3>
<h4 align="center">                       
Students: <br>  
 Muhammad Izzul Azri ZAINOL AZMAN <br>
 Pranavan Ramakrishnan
</h4>
<p align="center">
  <p align = "center">
     <img  src = "https://www.ros.org/news/2016/05/23/kinetic.png" width=400>
     <img  src = "resources/turtlebot3.jpg" width=400>
    
  </p>
</p>

## Table of Content 

- [Introduction](#introduction)
- [Project Implementation ](#Project-Implementation)<br>
  - [How to control the robot with /cmd_vel](#How-to-control-the-robot-with-/cmd_vel)
  - [How to create a mapping program launches to map the environment](#How-to-create-a-mapping-program-launches-to-map-the-environment)
  - [How to set a move base system for creating a goal to move_base and implement the obstacles avoiding algorithm](#How-to-set-a-move-base-system-for-creating-a-goal-to-move_base-and-implement-the-obstacles-avoiding-algorithm)
  - [How to create a navigation program with a set of waypoints using Rviz](#How-to-create-a-navigation-program-with-a-set-of-waypoints-using-Rviz)
- [Conclusion](#Conclusion)
- [References](#References)


## Introduction
<p align="justify">Our project is about the navigation of the Turtlebot 3 model robot. As the introduction of Turtlebot 3 burger, it is a programmable robot which runs completely on ROS and Linux. The turtlebot 3 burger that we use has a feature of LiDAR sensor which is a need for doing the SLAM gmapping. This project  requires us to accomplish a few objective which is:</p> 

- Create a script that moves the robot around with simple /cmd_vel publishing. See the range of movement of this new robot model.
- Create mapping launches, and map the whole environment. You have to finish with a clean map of the full cafeteria. Setup the launch to be able to localize the Turtlebot3 robot.
- Set up the move base system so that you can publish a goal to move_base and Turtlebot3 can reach that goal without colliding with obstacles.
- Create a program that allows the Turtlebot3 to navigate within the environment following a set of waypoints. Waypoints locations are presented on the next page.

<p align="justify">This objective will help us to understand more about using and implementation of our knowledge on the ground-based robot. We will use the constructsim platform which is similar to a virtual environment. This simulation offers us a very good user interface and is user friendly. The main thing that was necessary for the success of this project was understanding the ROS based system, using the right tool for the visualisation of the mapping and the right packages to be used to drive the robot and navigate. Besides that, we will be using RViz for visualization, Gazebo to simulate the virtual world, rqt_graph for the visualizing the ROS computation graph and mainly using a python programming language for the scripts.</p> 


## Project Implementation
__How to control the robot with /cmd_vel__<br>
_Objective_: Create a script that moves the robot around with simple /cmd_vel publishing. See the range of
movement of this new robot model.

<!--Put Your content-->

__How to create a mapping program launches to map the environment__<br>
_Objective_: Create mapping launches, and map the whole environment. You have to finish with a clean map of the full cafeteria. Setup the launch to be able to localize the Turtlebot3 robot.<br>
<!--Put Your content-->

__How to set a move base system for creating a goal to move_base and implement the obstacles avoiding algorithm__<br>
_Objective_: Set up the move base system so that you can publish a goal to move_base and Turtlebot3 can reach that goal without colliding with obstacles.<br>
<!--Put Your content-->

__How to create a navigation program with a set of waypoints using Rviz__<br>
_Objective_: Create a program that allows the Turtlebot3 to navigate within the environment following a set of waypoints. Waypoints locations are presented on the next page.<br>

## Conclusion
<p align="justify">As conclusions, here we are trying to explain from top to bottom on how to handle the turtlebot 3 model burger. We start with the Introduction of the turtlebot 3. Then we continue to explain in detail for the Project Implementation that is started with the creation of a script that moves the robot around with simple /cmd_vel publishing. See the range of movement of this new robot model. Next details on how to create the mapping launches, and map the whole environment. Then, set up the move base system so that it can publish a goal to move_base and Turtlebot3 can reach that goal without colliding with obstacles. Lastly, create a program that allows the Turtlebot3 to navigate within the environment following a set of waypoints. For now, the implementation of task 4 is successfully going and the next plan was to create an autonomous script to go to three of the waypoints. We believe the approach that we demonstrated above is able to be implemented for project development success. </p>
## References
* Amsters, Robin & Slaets, Peter. (2020). Turtlebot 3 as a Robotics Education Platform. 10.1007/978-3-030-26945-6_16.<br> 
* Esteve. (2019, October 25). Turtle_Bot3_BringUp For ROS. WikiROS. http://wiki.ros.org/turtlebot3_bringup?distro=kinetic<br>
* G. (n.d.). Wiki. Retrieved (February 4, 2020). Retrieved from http://wiki.ros.org/gmapping<br> 
* Jung, L. (2019, December 31). ROBOTIS. (ROBOTIS Co.,Ltd.) Retrieved from https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#overview<br> 
* Pyo, Y. (2018, April 4). Wiki ROS. Retrieved from turtlebot3_simulations: http://wiki.ros.org/turtlebot3_simulations


