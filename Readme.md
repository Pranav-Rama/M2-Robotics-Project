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


## Project Implementation<br>

## How to control the robot with /cmd_vel<br>
_Objective_: Create a script that moves the robot around with simple /cmd_vel publishing. See the range of
movement of this new robot model.

<!--Put Your content-->

## How to create a mapping program launches to map the environment<br>
_Objective_: Create mapping launches, and map the whole environment. You have to finish with a clean map of the full cafeteria. Setup the launch to be able to localize the Turtlebot3 robot.<br>
<!--Put Your content-->

## How to set a move base system for creating a goal to move_base and implement the obstacles avoiding algorithm<br>
_Objective_: Set up the move base system so that you can publish a goal to move_base and Turtlebot3 can reach that goal without colliding with obstacles.<br>
<!--Put Your content-->

## How to create a navigation program with a set of waypoints using Rviz<br>
_Objective_: Create a program that allows the Turtlebot3 to navigate within the environment following a set of waypoints. Waypoints locations are presented on the next page.<br>
To launch the navigation file:   
<br>
_Execution_: The next task is to create a program that allows the Turtlebot3 to navigate within the environment following a set of waypoints. Waypoints locations are presented on the below figures. 
<p align="center">
  <img src = "Resources/Images/w1.png">
</p>
<p align="center">
  <img src = "Resources/Images/w2.png">
</p>
<p align="center">
  <img src = "Resources/Images/w3.png">
</p>
<br>
<p align="justify"> In here we got three figures which are the three different waypoints that need to be achieved. In order to develop a ROS program that allows the robot to navigate to those locations, we first need to know what are the (x,y) coordinates of these waypoints onto the map. Then, we will use the coordinate to define the navigation mission that we submit to the robot’s navigation stack to execute it. Remember that any robot on ROS  runs the move_base navigation stack which allows the robot to find a path towards a goal and execute the path following while avoiding obstacles. The setup of the terminal, gazebo and RViz should follow as below for easiness of getting the coordinates.</p>
<p align="center">
  <img src = "Resources/Images/amcl.png">
</p>

<p align="justify"> The first step is to open the map which we have been mapping. By using the RViz to visualize the map, we use the 2D Pose estimate to get the waypoint coordinates. After all, it has been set up as below, open another terminal and write rostopic echo /amcl_pose to get the location of the robot on the map. While not closing the terminal, go back to RViz the click on 2D Pose Estimate button, then click to one of the waypoints on the map. Go back to the terminal where the command of rostopic echo /amcl_pose been running, and you will find the coordinate of the point selected.</p>

The second step is to find the location of interest. As an example, the (x,y) coordinates of the three waypoints should look like these values:

- Waypoint1(27.70, 12.50) /example value
- Waypoint2(30.44, 14.50) /example value
- Waypoint3(35.20, 12.50) /example value

<br>
<p align="justify">The final step is to write the navigation program. The navigation program will be written in Python languages which will use the rospy, actionlib and others ROS or turtlebot library. In the program code, we will include the coordinates of the waypoints and will let the user choose either to go to the waypoint 1, 2 or 3. Besides that, it can autonomously navigate through the whole 3 waypoints. The figure below shows the flowchart of the navigation program for turtlebot to reach all of the waypoints. The points set in the flowchart are as an example of the program flow.</p>

To launch the navigation
    
    roslaunch t3_navigation start_navigation.launch
 <br>
To launch the autonomous navigation to waypoints:

    roslaunch t3_waypoint autonomous_navigation.launch

## Conclusion
<p align="justify">As conclusions, here we are trying to explain from top to bottom on how to handle the turtlebot 3 model burger. We start with the Introduction of the turtlebot 3. Then we continue to explain in detail for the Project Implementation that is started with the creation of a script that moves the robot around with simple /cmd_vel publishing. See the range of movement of this new robot model. Next details on how to create the mapping launches, and map the whole environment. Then, set up the move base system so that it can publish a goal to move_base and Turtlebot3 can reach that goal without colliding with obstacles. Lastly, create a program that allows the Turtlebot3 to navigate within the environment following a set of waypoints. For now, the implementation of task 4 is successfully going and the next plan was to create an autonomous script to go to three of the waypoints. We believe the approach that we demonstrated above is able to be implemented for project development success. </p> <br>

## References
* Amsters, Robin & Slaets, Peter. (2020). Turtlebot 3 as a Robotics Education Platform. 10.1007/978-3-030-26945-6_16.<br> 
* Esteve. (2019, October 25). Turtle_Bot3_BringUp For ROS. WikiROS. http://wiki.ros.org/turtlebot3_bringup?distro=kinetic<br>
* G. (n.d.). Wiki. Retrieved (February 4, 2020). Retrieved from http://wiki.ros.org/gmapping<br> 
* Jung, L. (2019, December 31). ROBOTIS. (ROBOTIS Co.,Ltd.) Retrieved from https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#overview<br> 
* Pyo, Y. (2018, April 4). Wiki ROS. Retrieved from turtlebot3_simulations: http://wiki.ros.org/turtlebot3_simulations


