Python Assessment Task


Task Overview

Create a Python project to perform simple statistics on a list of values.
Task Details
Declare a list of numbers in Python. The list should have at least 50 numbers. Take input from user, 
about the statistics which they would like to see. Based on the user input, return the value of the 
statistic to the user. 
The statistics that the project should be able to perform are:
• Average
• Mean Deviation
• Count
• Length
• Maximum value
• Minimum value
• Range
• Sum
• Sort
• Variance
• Standard Deviation
• Median
• Linear Regression (Optional)
Do not use any built-in libraries. Instead calculate the statistics using formulae.

plan

note: for this project we will be doing test driven design as this is the first time i will be using python as a language the tests are likly to need editing so it wont be full tdd

1. as this is my first time coding in python first thing is to set up my coding enviroment, installing the nessesary dependencies and linter preferences and such

2. write tests via the unittest package

3. create a class for the storage of the data that will push and pull information from the interface. this includes:
a default list incase the user does not want to enter their own one
the working list that will be used for all calculations i.e will be set to the users input list or the default list on programe start 
the results of any calculations done so that if these results are needed again for any reason we dont need to go through the calculations again saving cost (we dont just have all the calculations run on start for the same reason)

4. write each of the function classes for the calculations. this is self explanitary the classes have to pull information from the inteface then work on it and finally send back the results to the interface 

5. create the interface class that will deal with getting the user inputs as well as sending information to the users as well as data storage class and the methods so that those can all be decoupled from each other


summary 

by the end of this i should have a psudo full stack develpment project with the interface acting as the front end and the method classes and data class working in place of the back end and data base respectivly 