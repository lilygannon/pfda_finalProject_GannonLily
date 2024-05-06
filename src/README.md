# pfda_finalProject_GannonLily
# RAIN OR SNOW

## Demo
Demo Video: <https://youtu.be/N0gQgx_bg7E>

## GitHub Repository
GitHub Repo: <https://github.com/lilygannon/pfda_finalProject_GannonLily.git>

## Description
I created a game of sorts that allows the player to choose between playing
an animation of snowfall or rainfall. I created the raindrop and the landscape
for the snowfall so i will use the images instead of a pygame surface or shape.

- Snowfall.py
	- The code for the snowfall animation. When called it plays an animation of
    dark mountain forest with snow falling in the midground.
- Rainfall.py
	- The code for the rainfall animation. When called it plays an animation of
    bright blue raindrops falling over a gray blue background.
- main.py
	- The main code that sets the default screen to one that reads "Welcome to
    Rain or Snow! For rainfall press 'r' and snowfall press 's'. To escape
    press 'esc'. Have fun!
- Harmond-SemBdItaCond.otf
    - The font I used in this project
- Raindrop.png
    - A .png file of a raindrop for the Rainfall code
- trees_back.png
    - A .png file of mountains and trees for the background of the snowfall
    animation
- trees_fall.png
    - A .png file of trees for the foreground of the snowfall animation

Challenges
    I could not get the snowfall to move the way I wanted with a picture, it
    needed to be a pygame surface. But I still used my are for the back and 
    foreground
    The rainfall stops after a few seconds when called in the main file. I
    continued endlessly by itself but something about being called made it stop
    after a few seconds. 

Future Areas of Improvement
    Firgure out how to get the rainfall to work fully
    Find a way to save the animations as .mp4s