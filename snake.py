"""Snake, classic arcade game.

Este juego es el clasico juego de "Snake" donde una serpiente
se mueve a lo largo del mapa donde se encuenttra comida y
con esta va creciendo.
Sin embrago nuestra propuesta sigue esta idea pero añade obstaculos
en el mapa con el objetivo de incrementar la dificultad ya que si
la serpiente choca con este el juego termina. Los obstaculos son
aleatorias y cambian cada que la serpiente come.

"""
from turtle import update, clear, ontimer,\
    setup, hideturtle, tracer, listen, onkey, done
from random import randrange
from freegames import square, vector
import pygame

"""Se carga y reproduce la cancion tetris21"""
mp3_path = 'tetris21.mid'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play(0)

"""Se crean vectores para guardar datos"""
food = vector(0, 0)
snake = [vector(0, 0)]
aim = vector(0, -10)
obs = vector(0, 0)
obs2 = vector(0, 0)
obs3 = vector(0, 0)

"""Las cordenadas inciales de la comida con aleatorias"""
food.x = randrange(-15, 15) * 10
food.y = randrange(-15, 15) * 10

"""Los colores de la serpiente y la comida varian en 5 tonos pero
estos no pueden ser iguales entre si """
colores = ['blue', 'green', 'black', 'orange', 'grey']
colorini = colores[randrange(0, 4)]
colorcom = colores[randrange(0, 4)]

while True:
    if colorini == colorcom:
        colorcom = colores[randrange(0, 4)]
    else:
        break


def change(x, y):
    "Cambio de direccion de la serpiente."
    aim.x = x
    aim.y = y


def inside(head):
    "Si la cabeza esta fuera de los limites del juego pierde."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Si la serpiente toca su cuerpo pierde."
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    """Si la serpiente toca la comida esta crece y la comida
    como los obstaculos toman una nueva posicion"""
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        obs.x = randrange(-15, 15) * 10
        obs.y = randrange(-15, 15) * 10
        obs2.x = randrange(-15, 15) * 10
        obs2.y = randrange(-15, 15) * 10
        obs3.x = randrange(-15, 15) * 10
        obs3.y = randrange(-15, 15) * 10
        """La comida ni los obstaculos pueden estar en mismo lugar
        que la serpiente"""
        while True:
            if food == obs or food == obs2 or food == obs3:
                food.x = randrange(-15, 15) * 10
                food.y = randrange(-15, 15) * 10
            else:
                break

        while True:
            if head == obs or head == obs2 or head == obs3:
                obs.x = randrange(-15, 15) * 10
                obs.y = randrange(-15, 15) * 10
                obs2.x = randrange(-15, 15) * 10
                obs2.y = randrange(-15, 15) * 10
                obs3.x = randrange(-15, 15) * 10
                obs3.y = randrange(-15, 15) * 10
            else:
                break

    else:
        snake.pop(0)
    clear()

    for body in snake:
        square(body.x, body.y, 9, colorini)

    square(food.x, food.y, 9, colorcom)
    square((obs.x), (obs.y), 9, 'brown')

    """Se crean los obstaculos y el cuerpo de la serpiente"""
    for i in range(10):
        square((obs.x+(10*i)), (obs.y), 9, 'brown')

    square((obs2.x), (obs2.y), 9, 'brown')

    for i in range(10):
        square((obs2.x+(10*i)), (obs2.y), 9, 'brown')

    square((obs3.x), (obs3.y), 9, 'brown')

    for i in range(10):
        square((obs3.x+(10*i)), (obs3.y), 9, 'brown')

    """Si la serpiente toca el obstaculo pierde."""
    for i in range(10):
        if head == obs or head == obs2 or head == obs3 or\
            (head.x == (obs.x+(10*i)) and head.y == obs.y)\
            or (head.x == (obs2.x+(10*i)) and head.y == obs2.y)\
                or (head.x == (obs3.x+(10*i)) and head.y == obs3.y):
            square(head.x, head.y, 9, 'red')
            update()
            return
    update()
    ontimer(move, 100)


"""El mapa"""
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
"""Las teclas de movimiento"""
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
