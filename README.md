# Pokemon Game (Python)
![enter image description here](https://res.cloudinary.com/dloadb2bx/image/upload/v1682789789/poke1_iueryd.png)

## Tecnologias utilizadas
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

This project was created using Docker to studying the basic concepts of Python learned at day 01, 02 and 03  in the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)**.  This project is not part of the course curriculum, was created to learn more complex concepts of Python.

## Summary
**Day 03:** Learning how to deal with if/elsa statements

## What player can do?

**Player**: Can select one Pokemon to fight. There is three options to select, each one with their own strenght.  What actions the player can do?
- Choose to attack, defend or use special power

**Enemy:** The enemy will be selected using a random array of objects where exists three Pokemons. Their actions it's also, attack, defend or use special power.

**Turn:** After each action the turn goes to the other part. After the selection the script runs some random values to calculate the chance of success for each action. After that the points of life is calculated. If someone gets less then 1 point of life the game is over.


## How to run this project
This project was created with Docker, the Dockerfile is:

    FROM  python:3
    
    WORKDIR  /app
    
    COPY  .  .
    
    CMD  ["python",  "app/main.py"]

To run just download this project and run the follow commands:  `docker build -t pokemon-game .`  then run `docker run -it pokemon-game`. 