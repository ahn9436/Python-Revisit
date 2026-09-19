import turtle as pychart

circle__radius = 100

def pie__chart(l1):
    colors = ["yellow","brown","white","crimson","cyan","green","violet","gray","blue"]
    l2 = [0,0,0,0,0,0,0,0,0]
    for i in l1:
        l2[i-1] += 1

    pychart.left(90)

    color = 0
    for b in l2:
        if b == 0: continue
        else:
            frac = 360 / (len(l1))

            pychart.fillcolor(colors[color])

            pychart.begin_fill()
            pychart.forward(circle__radius)
            pychart.left(90)
            pychart.circle(circle__radius,b * frac)
            pychart.left(90)
            pychart.forward(circle__radius)

            pychart.end_fill()
            pychart.right(180)
            
            color += 1


# pie__chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,3,4,3])
# pie__chart([3,4,3,3,2,2,2,3,7,8,2,3,3,3,4,3,6,3,7,3,3,4,8,4])
pie__chart([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])

pychart.hideturtle()
pychart.done()