import turtle, pygame
import random
import time


score = 0

high_score = 0
pygame.mixer.init(44100, -16,2,2048)
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()



wn = turtle.Screen()
wn.setup(width=900, height=700)
wn.bgpic("background.gif")
wn.title("Nyan")
wn.tracer(0)
wn.register_shape("cat.gif")
wn.register_shape("bad.gif")
wn.register_shape("food.gif")




cat = turtle.Turtle()
cat.shapesize(stretch_wid=4,stretch_len=4)
cat.color("green")
cat.shape("cat.gif")
cat.penup()
cat.goto(-250, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score:0", align="center", font=("Courier", 24, "normal"))






def move_up():
    y = cat.ycor()
    y += 35
    cat.sety(y)

def move_down():
    y = cat.ycor()
    y -= 35
    cat.sety(y)
enemys = []

for l in range(5):
    enemy= turtle.Turtle()
    enemy.shapesize(stretch_wid=4,stretch_len=4)
    enemy.color("red")
    enemy.shape("bad.gif")
    enemy.penup()
    enemy.goto(400, 0)
    enemy.speed = random.randint(1, 4)
    enemys.append(enemy)





foods = []
for _ in range(5):
    food = turtle.Turtle()
    food.shapesize(stretch_wid=4,stretch_len=4)
    food.color("blue")
    food.shape("food.gif")
    food.penup()
    food.goto(400, 0)
    food.speed = random.randint(1, 4)
    foods.append(food)

wn.listen()
wn.onkey(move_up, "w")
wn.onkey(move_down, "s")


while True:
    wn.update()

    
    for food in foods:
        x = food.xcor()
        x -= food.speed
        food.setx(x)
            
        if x < -500:
            ye = random.randint(-350, 350)
            food.goto(400, ye)

        if food.distance(cat) < 25:
            ye = random.randint(-350, 350)
            food.goto(400, ye)
            score += 20

    for enemy in enemys:
        x = enemy.xcor()
        x -= enemy.speed
        enemy.setx(x)
            
        if x < -500:
            y = random.randint(-350, 350)
            enemy.goto(400, y)

        if enemy.distance(cat) < 25:
            y = random.randint(-350, 350)
            enemy.goto(400, y)
            score -= 20
    if score > high_score:
        high_score = score
   

    if score < -100:
        cat.goto(-250, 0)
        time.sleep(.1)
        score = 0
            

   



    


    wn.listen()
    wn.onkey(move_up, "w")
    wn.onkey(move_down, "s")
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
    

        



