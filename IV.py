import turtle
import math
from math import degrees


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
    for i in range(2):
        for features in ((base, interior_angle), (leg, 180 - interior_angle)):
            polyline(1, features[0], features[1])

def isosceles_triangle(leg, base_angle):
    base = 2 * leg * math.sin(math.radians(90 - base_angle))  # Length of the base of a triangle.
    angle = 180 - base_angle
    polyline(1, leg, angle)
    polyline(1, base, angle)
    polyline(1, leg, 2 * base_angle)

def draw_pie(n, leg):
    """Uses isosceles_triangle to draw the triangle parts of regular polygons.

    :param n: Number of sides of  polygon
    :param leg: Length of side of isosceles triangle forming polygon triangles.
    :return: None
    """
    base_angle = 90 - 180 / n  # The base angle of the isosceles triangle
    center_angle = 2 * base_angle  # The center angle of the triangle in the center of the polygon
    # print(f"B:{base_angle}\nC:{center_angle}\n")
    for i in range(n):  # Loop on the number of sides/triangles we need to create.
        isosceles_triangle(leg, base_angle)  # Draw a triangle
        my_turtle.left(180 - center_angle)   # Turn turtle to location for next triangle

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
# isosceles_triangle(100, 40)
my_turtle.color( "green" )
draw_pie(5, 50)
my_turtle.color( "red" )
draw_pie(6, 100)
my_turtle.color( "purple" )
draw_pie(7, 150)
my_turtle.color( "yellow" )
draw_pie(8, 200)

# Close the turtle graphics window when clicked
turtle.exitonclick()