#Written by Ahmad Mubashir Naqshbandi on 3rd December 2021
from graphics import *
from time import *
win=GraphWin("Bouncing Circles",400,400)
win.setCoords(0,400,400,0)
n=int(input("Enter the number of circles you want: "))
t=eval(input("Enter the number of iteration you want: "))
circList=[]
dxList=[]
dyList=[]
radList=[]
centerList=[]
colourList=[]
sleepList=[]
for i in range(n):
    rad=float(input("Enter the radius of circle {0}: ".format(i+1)))
    x,y=eval(input("Enter the center of the circle {0}: ".format(i+1)))
    center=Point(x,y)
    dx=float(input("enter the amount you want the move the circle {0} in x: ".format(i+1)))
    dy=float(input("enter the amount you want the move the circle {0} in y: ".format(i+1)))
    colour=input("Enter the colour of the circle: ")
    s=float(input("Enter the sleep time you want for this crcle: "))
    circ=Circle(center,rad)
    circList.append(circ)
    dxList.append(dx)
    dyList.append(dy)
    radList.append(rad)
    colourList.append(colour)
    centerList.append(center)
    sleepList.append(s)
for i in range(n):
    circList[i].draw(win)
    circList[i].setFill(colourList[i])
    circList[i].setOutline(colourList[i])
for i in range(t):
    for i in range(n):
        if dxList[i]+radList[i]+circList[i].getCenter().getX()>400:
            dxList[i]=-dxList[i]
        if dxList[i]-radList[i]+circList[i].getCenter().getX()<0:
            dxList[i]=-dxList[i]
        if dyList[i]+radList[i]+circList[i].getCenter().getY()>400:
            dyList[i]=-dyList[i]
        if dyList[i]-radList[i]+circList[i].getCenter().getY()<0:
            dyList[i]=-dyList[i]
        circList[i].move(dxList[i],dyList[i])
        sleep(sleepList[i])
    
    
    
