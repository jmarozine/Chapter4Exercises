import turtle
import math

# Note the usage of "docstring" to document the polyline function. A docstring should at a minimum do:
#   1. Explain concisely what the function does, without getting into the details of how it works,
#   2. Explain what effect each parameter has on the behavior of the function, and
#   3. Indicate what type each parameter should be, if it is not obvious.
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

def arc(radius, angle):  # Similar to circle, but can do fractional circles.
    arc_length = 2 * math.pi * radius * angle / 360  # Here we calculate how much of the arc of a circle to draw.
    n = 30  # We fix the segments to 30 still, but this is 30 segments per arc, so smaller arcs will appear smoother.
    length = arc_length / n
    step_angle = angle / n  # Since we are covering a fraction of the arc of a circle, we need smaller angles too.
    polyline(n, length, step_angle)  # And now we approximate the arc with polyline.

def petal(radius, angle=90):
    return_angle = 180 - angle
    for i in range(2):
        arc( radius, angle )
        my_turtle.left( 180 - angle )


def flower(num_petals, radius, petal_angle=None):
    rotate_angle = 360 / num_petals
    petal_angle = rotate_angle if not petal_angle else petal_angle
    for p in range(num_petals):
        petal(radius, petal_angle)
        my_turtle.left(rotate_angle)


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
my_turtle.speed(10)  # Somewhat equivalent to Jupyter turtle's delay parameter (1 slow to 10 fast).
flower(10, 90, 90)

# Close the turtle graphics window when clicked
turtle.exitonclick()