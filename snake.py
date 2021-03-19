"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(0, 0)]
aim = vector(0, -10)
obs = vector(0, 0)
obs2 = vector(0, 0)
obs3 = vector(0, 0)


food.x = randrange(-15, 15) * 10
food.y = randrange(-15, 15) * 10


colores=['blue', 'green', 'black', 'orange', 'grey']
colorini=colores[randrange(0, 4)]
colorcom=colores[randrange(0, 4)]


while True:
    if colorini==colorcom:
        colorcom=colores[randrange(0, 4)]
    else:
        break

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()    
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        obs.x= randrange(-15, 15) * 10
        obs.y= randrange(-15, 15) * 10
        obs2.x= randrange(-15, 15) * 10
        obs2.y= randrange(-15, 15) * 10
        obs3.x= randrange(-15, 15) * 10
        obs3.y= randrange(-15, 15) * 10
        while True:
            if food==obs or food==obs2 or food==obs3:
                food.x = randrange(-15, 15) * 10
                food.y = randrange(-15, 15) * 10
            else:
                break

        while True:
            if head==obs or head==obs2 or head==obs3:
                obs.x= randrange(-15, 15) * 10
                obs.y= randrange(-15, 15) * 10
                obs2.x= randrange(-15, 15) * 10
                obs2.y= randrange(-15, 15) * 10
                obs3.x= randrange(-15, 15) * 10
                obs3.y= randrange(-15, 15) * 10
            else:
                break

    else:
        snake.pop(0)


    clear()

    for body in snake:
        square(body.x, body.y, 9, colorini)

    square(food.x, food.y, 9, colorcom)
    
    square((obs.x), (obs.y),9, 'brown')

    for i in range(10):
        square((obs.x+(10*i)), (obs.y),9, 'brown')

    square((obs2.x), (obs2.y),9, 'brown')

    for i in range(10):
        square((obs2.x+(10*i)), (obs2.y),9, 'brown')

    square((obs3.x), (obs3.y),9, 'brown')

    for i in range(10):
        square((obs3.x+(10*i)), (obs3.y),9, 'brown')

    for i in range(10):
        if head == obs or head == obs2 or head == obs3 or (head.x==(obs.x+(10*i)) and head.y==obs.y) or (head.x==(obs2.x+(10*i)) and head.y==obs2.y)\
        or (head.x==(obs3.x+(10*i)) and head.y==obs3.y) :
            square(head.x, head.y, 9, 'red')
            update()
            return
    

    update()
    ontimer(move, 100)

def store(key, value):
    "Store value in state at key."
    state[key] = value
    

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
