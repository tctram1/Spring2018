# CIS 465 - Capstone - Spring 2018
### Tuyen Tram
### Western Carolina University


## Description
This repository contains my work studying Python for the Computer Information Systems capstone course in Spring of 2018 at Western Carolina University.

## Folders Description
Below are information about each folder listed in the order that I completed them. Additional information on how to run the applications is included in separated README.md files in each folder.

* **Exercise**: 
  * Junk files that I was practicing Python from miscellaneous sources
  * **edX-Beginner/M1**: exercise files from an EdX course Python Beginner
  * **python-functional**: exercise to learn how class works

* **practices**:
  * Junk files that was practicing Python from miscellaneous sources

* **scripts**:
  * Customized tools that aids in designing process in Autodesk Maya
  * 2 tools:
    * Aligner
    * Randomizer

* **python-hardway**:
  * Exercise from the Learn Python 3 The Hardway book

* **web2py_win**:
  * Original files including websites that I created using Web2Py framework
  * **web2py/applications/pluralsight**: practice files
  * **web2py/applications/farm**: simple website where farmers, hypothetically, can signin and upload the products that they want to sel; and consumer can signin to order those products.
  * **NOTE**: 
    * Web2Py framework for window had changed after a few weeks I completed these exercises. The new framework wouldn't work unless I rewrite everything.
    * The new framework is in the **web2py_new/web2py** folder
    
* **web2py_new/web2py**: new framework for Web2Py applications

* **data-visualization**:
  * Jyputer Notebook files on data visualization
  
* **pyrevit**:
  * An add-on to a building information modeling software to create pattern
  * This add-on was written in Python language
  
* **pygame**:
  * **Game**: Breakout game
    * Menu Scene: at this scene, user can select to start game, check highscore, or quit.
    * Playing Scene:
      * All the bricks are automatically generated. Once level is clear, the next level will also be automatically generated.
      * User has 5 lives to start.
      * "Live Brick" gives user extra life.
      * "Speed Brick" increases the speed of the ball.
      * Score increases in an increment of 100.
    * Game Over Scene: here, user needs to enter name
    * Highscore Scene: 
      * This scene displays the top five highscore.
      * User can select to play again, or go to menu.
    * There is a highscore.dat file that will update each time a score is recorded at the end of each game.
  * **breakout**: (for Breakout game) game architecture from Pluralsight course instructor
  * **Pluralsight File**: (for Breakout game) files from Pluralsight course
  * **M2**: practice files to learn pygame
  * **MemoryPuzzle**: matching game
  * **Snake**: a Snake game using pygame

## What did I learn with Python?
   During the course of this class, I focused on only one coding language - Python. I explored many areas of this coding language. I learned about the basics, scripting for Autodesk Maya, web application, data visualization, pattern making for Autodesk Revit, and pygame.
   
   The following basics I learned from the "Learn Python 3 the Hard Way" book, including comments, numbers and math, variables and printing, strings and text, read from and write to a file, functions, classes, modules, objects, if statements, for loops, while loops, questions-based games, dictionaries, and websites via .venv in C-drive.
   
   Autodesk Maya supports scripting to aid with the three-dimensional design process. It has its own scription language called MEL. But it also supports Python. I learned how to make a randomizer. This tool allows user to quickly populate a space with objects in random locations. The second tool I made is the aligner. This tool allows user to quickly align all objects on either x, y, or z axis. These tools could be useful for animators to generate numerous of objects quickly and efficiently.
   
   I learned two types of web application. One was using virtualenv (virtual environment) from python pip, and another was using Web2Py framework. Overall, Python virtual environment was easier to use because it was more straightfoward. It doesn't require for a model, view, or controller like that of the Web2Py. I also find that Web2Py is not quite stable. After a couple of weeks finished my exercise wit Web2Py, updates were made to the framework. There were no way to merge my existing exercises with this new framework, unless I rewrite everything.
   
   I didn't get too deep with data vitualization. I only finished one course on this on the Pluralsight website. I used Jyputer Notebook for these exercise. Overall, I found it useful to learn about this. I learned how to generate many graphs from an excel data spreadsheet. I learned how to graph bars, lines, scattered plot, and sub-graphs. I also learned how to label the graphs.
   
   Autodesk Revit is a software for building information modeling for interior designers, architects, engineers, etc. to create drawings for buildings, structors, and homes. It has many built-in patterns such as wood grains and tiles. But when it comes to creating custom patterns, Revit has limited functions to support. PyRevit is a third-party add-on that written in Python. The add-on makes it easy to create any pattern within a few clicks. 
   
   Pygame was my favorite area out of everything I learned in this course. It was fun to create games from scratch. I created three games: Breakout, Snake, and Memmory Puzzle.
   
## What area(s) would I like to learn about?
   I didn't get a chance to learn about **automation** with Python as I intented to as the beginning of this class. I will explore this area as well as continue to learn about creating games with Pygame.
   
## My assessment of this coding language
   I love Python. It is a very simple language to learn. It doesn't take a long time to get up-to-speed with this. It is almost like writing in English. Another strength about Python is that there are numerous of libraries to support almost everything and countless of courses and toturials on it. 
   
   One weakness of Python is the error messages. Error messages most of the time are not clear. Although it points to the exact location of the error, sometimes the real error is not there.
