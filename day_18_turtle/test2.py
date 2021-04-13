import turtle

bob = turtle.Turtle()
xx,yy= turtle.window_width(), turtle.window_height()
print (f'window size: {xx},{yy}')
bob.speed(15)

stl=int(input("Please enter length of first side: "))

while stl>turtle.window_width()/2:
    stl=int(input("Please enter a shorter length that will fit into the window: "))

dec=int(input("Please enter the change in length per iteration: "))


while stl > dec:
    bob.forward(stl)
    bob.right(90)
    stl= stl- dec

turtle.done()