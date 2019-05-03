# importing the turtle module to the python enviroment
import turtle

# initiate both a window and a turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
Greg = turtle.Turtle()
Greg.color("blue")
Greg.pensize(2)
Greg.speed(0)
for i in range(100):
    Greg.forward(1+i*i*0.01)
    Greg.left(5+i*0.5)
# Mainloop waits for user to close the window
window.mainloop()