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

def rhombus(base, interior_angle):
    """Draws a rhombus of varying length and angle.

    :param base: Length of side of rhombus. Rhombus have equal lengthed sides
    :param interior_angle: The first interior angle of a rhombus, the complementary angle will bie 180 minus this angle
    :return: None
    """
    for i in range(2):  # A rhombus is also symmetric like the rectangle, draw a pair of base angle parts.
        for angle in (interior_angle, 180 - interior_angle):  # draw base, turn small angle, draw base, turn sharp angle
            polyline(1, base, angle)


# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=500, height=500)

# Create a new turtle object, equivalent to Jupyter's make_turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape and color
my_turtle.shape( "arrow" )  # Other options: arrow, classic, square, triangle, and turtle
my_turtle.color( "green" )

# Draw with a turtle.
my_turtle.speed(5)  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).
rhombus(50, 60)

# Close the turtle graphics window when clicked
turtle.exitonclick()