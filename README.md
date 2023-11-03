# MTT CoHack Challenge: Python Snake Game

## Introduction

The snake game is an arcade game and it has very simple logic, which is why it's any ideal example to demonstrate how to build games with [pygame](https://www.pygame.org/news), a python library to build games.

<p align="center">
  <img src="./media/snake_game.gif" alt="Snake Game GIF">
</p>

*GIF by User:Ustone07, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons*

## Requirements

- You will need to have **git** installed in your computer, so that you can clone this repository to use the application code prepared for you.
```
git clone https://github.com/mttcohack/python-snake-game.git
```
- You will need to have **python** installed in your computer.
- You can also use your computer base environment for development, but as a best practice we can also create a python virtual environment. Navigate to your project folder and then execute this code (Be sure to replace {name-of-your-environment} with the name of your virtual environment.)
```
python -m venv {name-of-your-environment}
{name-of-your-environment}/Scripts/Activate #To activate your virtual env
```
- You will need to install the python libraries included in the *requirements.txt* file in the virtual environment or computer where you plan on developing the application using the following code.

```
pip install -r requirements.txt
```

## Learning Objectives

This hack will help you:

- Get introduced to object oriented programming (OOP) with python, and understand how to create and manage game objects, like the snake and the apple (food).
- Understand the basics of Python programming, including variables, loops, and functions.
- Understand the concept of game loops and how to control game state.

## Success Criteria

### Challenge 1

- The snake should move in all four directions: up, down, left, and right.
- An image of an apple with a black background is displayed as the apple in the game instead of the white block. It has to be a 10 pixel by 10 pixel image.
- When the snake crosses the apple, a couple of things should happen:
  - The current apple should disappear and the new apple must be created in a different random location.
  - The length of the snake should increase by one.

#### Resources

- [Python Classes (w3schools.com)](https://www.w3schools.com/python/python_classes.asp)
- [Python Functions (w3schools.com)](https://learn.microsoft.com)
- [Python Conditions (w3schools.com)](https://www.w3schools.com/python/python_conditions.asp)
- [The import system — Python 3.12.0 documentation](https://docs.python.org/3/reference/import.html)

### [Optional] Challenge 2

- The game should end if the snake collides with itself.
- The game should also end if the snake collides with the wall or the boundaries of the game.
- Make the game more challenging by adding levels to the game, depending on the size of the snake, increase the speed of the snake!

#### Resources

- [python snake game - Python Tutorial (pythonspot.com)](https://pythonspot.com/snake-with-pygame/)
- [python - Increase the speed of the snake when food is eaten - Stack Overflow](https://stackoverflow.com/questions/73766527/increase-the-speed-of-the-snake-when-food-is-eaten)
- [How to have an image appear in python/pygame - Stack Overflow](https://stackoverflow.com/questions/8767129/how-to-have-an-image-appear-in-python-pygame)
