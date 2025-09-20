import turtle

def polyline(n, length, angle):  # This is really generalized and flexible now.
    """Draws line segments with the given length and angle between them.

    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degrees)
    """
    for i in range(n):
        my_turtle.forward(length)
        my_turtle.left(angle)

def polygon(n, length):
    angle = 360.0 / n
    # Now this is more generalized as it uses polyline, but still fixes the length and angle for regular polygons.
    polyline(n, length, angle)

def jump(length):
    """Move forward length units without leaving a trail.

    Postcondition: Leaves the pen down.
    """
    my_turtle.penup()
    my_turtle.forward( length )
    my_turtle.pendown()

def rectangle(b, h):
    """Takes a base and height and draws a rectangle using polyline.

    :param b: width of the rectangle, or its base
    :param h: height of the rectangle
    :return: None
    """
    for i in range(2):  # Since a rectangle is 2 symmetric bases and heights
        for s in (b, h):  # iterate: draw base, turn 90, draw height turn 90
            polyline(1, s, 90)


# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=500, height=500)

# Create a new turtle object, equivalent to Jupyter's make_turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape and color
my_turtle.shape( "circle" )  # Other options: arrow, classic, square, triangle, and turtle
my_turtle.color( "green" )

# Draw with a turtle.
my_turtle.speed(5)  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).
rectangle(80, 40)

# Close the turtle graphics window when clicked
turtle.exitonclick()