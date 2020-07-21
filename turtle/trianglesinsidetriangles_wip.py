from turtle import*
#shape('turtle')
speed(0)
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)
        
def triangle(sidelength=200):
    for i in range(3):
        forward(sidelength)
        rt(120)

def many_squares():
    for i in range (144):
        square()
        rt(5)

def polygon(sides=4,sidelength=100):
    for i in range(sides):
        forward(sidelength)
        right(360/sides)

def turtle_spiral(startlength=0,increase=5,angle=5,loops=160):
    length=startlength

    for i in range(loops):
        length += 5
        square(length)
        rt(angle)


def star(sides=5,sidelength=100):
    for i in range(sides):
        forward(sidelength)
        right(360/sides/0.5)



def starspiral(startlength=0,increase=5,angle=5,loops=160):
    length=startlength

    for i in range(loops):
        length += 5
        star(sides=
             5,sidelength=length)
        rt(angle)


lt(60)
length=200
depth=300
speed(3)
for i in range(depth):
  
    triangle(length)
    length = length / 2
    fd(length*)
    rt(120)
    
    






                       



