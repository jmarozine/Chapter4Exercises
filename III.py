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

def parallelogram(base, leg, interior_angle):
    """Draws a quadrilateral with parallel sides, a more generalized form of rhombus and rectangle.

    :param base: base of quadrilateral
    :param leg: side of quadrilateral
    :param interior_angle: first interior angle of quadrilateral
    :return: None
    """
    for i in range(2):  # Just like rhombus and rectangle before, there are 2 symmetric parts.
        for side, angle in ((base, interior_angle), (leg, 180 - interior_angle)):
            # Draw base and turn, then draw leg and turn complementary
            polyline(1, side, angle)

def rhombus(base, interior_angle):
    """Rhombus drawn with generalized parallelogram / quadrilateral function

    :param base: side of rhombus
    :param interior_angle: First interior angle of rhombus
    :return: None
    """
    parallelogram(base, base, interior_angle)

def rectangle(b, h):
    """Rectangle drawn with generalized parallelogram / quadrilateral function

    :param b: base of rectangle
    :param h: height of rectangle
    :return: None
    """
    parallelogram(base=b, leg=h, interior_angle=90)


# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=600, height=600)

# Create a new turtle object, equivalent to Jupyter's make_turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape and color
my_turtle.shape( "arrow" )  # Other options: arrow, classic, square, triangle, and turtle
my_turtle.color( "green" )

# Draw with a turtle.
my_turtle.speed(5)  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).
parallelogram(200, 100, 60)
my_turtle.color( "red" )
rhombus(50, 60)
my_turtle.color( "purple" )
rectangle(100, 50)

# Close the turtle graphics window when clicked
turtle.exitonclick()