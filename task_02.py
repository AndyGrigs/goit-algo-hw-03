import turtle

def koch(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch(length, level - 1)
        turtle.left(60)
        koch(length, level - 1)
        turtle.right(120)
        koch(length, level - 1)
        turtle.left(60)
        koch(length, level - 1)

def main():
    level = int(input("Введіть рівень рекурсії (0 або більше): "))
    length = 300.0  
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(False)  

    turtle.penup()
    turtle.goto(-length / 2.0, length / 3.0)
    turtle.pendown()

    for i in range(3):
        koch(length, level)
        turtle.right(120)

    turtle.update()
    turtle.done()

if __name__ == '__main__':
    main()
