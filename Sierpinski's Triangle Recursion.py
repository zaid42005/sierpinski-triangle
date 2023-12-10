import turtle #simple graphics library to draw the triangles


x_initial = -500
y_initial = 500


def setup(): #sets up the stage
    turtle.setup(1920, 1080)
    turtle.speed(0) #fastest drawing speed(adjust the timer set in the recursive calls for easier use)


def draw_triangle(x, y, side): #line drawing animation
    x2 = x + side / 2
    y2 = y - side
    x3 = x + side
    y3 = y
    # above is the coords of the tree smaller triangles inside it
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("purple")
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x, y)
    turtle.end_fill()
    #drawing animations^


def tri(x, y, side):
    draw_triangle(x, y, side) #call the draw function inside the recursive call

    side = side / 2 #divide side legnth by 2 to produce smaller triangles

    if side > 10: #once the side legnth is less than 10 pixels we end THE RECURSION (computer couldnt handle infinitely going for it but this value is adjustable I like to use 1 cuz it looks cool)
        turtle.ontimer(lambda: tri(x, y, side), 500)  # Delay animation with ontimer and lambda expression
        turtle.ontimer(lambda: tri(x + side, y, side), 500)
        turtle.ontimer(lambda: tri(x + (side / 2), y - side, side), 500)


def main():
    setup()
    #(NOTHING WILL HAPPEN TILL YOU ENTER THE SIDE START VALUE EHZEM SO ENTER IT INTO THE CONSOLE)
    sideStart = int(input("Enter an initial side legnth (recommended is 1000 pixels)")) #enter the start side size of the triangle (so if 1000 then an equilatiral triangle with sides 1000px)
    turtle.tracer(0, 0)  # Turn off animation
    tri(x_initial, y_initial, sideStart) # start the recursion
    turtle.update()  # Update the screen

    turtle.done()  # Finish the drawing


if __name__ == "__main__":
    main()
