import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    dish_soap = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    dish_soap.shape('turtle')
    # Set your turtle's speed using .speed(2)
    dish_soap.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    dish_soap.color('green')
    dish_soap.pencolor('blue')
    # Move your turtle forward using .forward(100)
    for i in range(4):
        dish_soap.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
        dish_soap.left(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    dish_soap.goto(0, 0)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    dish_soap.circle(radius=90, steps=30)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    dish_soap.begin_fill()
    dish_soap.goto(0, -100)
    dish_soap.circle(radius=900, steps=100)
    dish_soap.end_fill()
    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
