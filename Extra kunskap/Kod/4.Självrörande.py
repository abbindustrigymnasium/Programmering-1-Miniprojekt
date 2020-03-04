from tkinter import *
import time
master = Tk()
from random import randint

cheeseeaten=0
#musdetaljer
korttidsminne=[]
långtidsminne=[]
energi=50
mouse= [1,2] #position

#rightsize
def rs(inputval,sizevalue):
       return inputval*sizevalue
# Get coordinates, send in x and y value and return them + the size  of the object
def getcoord(x,y):
       sizevalue=50
       x= rs(x,sizevalue)
       y= rs(y,sizevalue)
       return x, y,x +sizevalue, y+sizevalue

def FoundCheese(mousepos):
    if Map[mousepos[0]][mousepos[1]]==1:
        outputtext= "Found Cheese at"+str(mouse[0])+" X  "+str(mouse[1])+ " Y"
        global cheeseeaten
        cheeseeaten+=1
        text.insert(INSERT, outputtext)

def Movemouse(mouse1,Movingobject):
       time.sleep(1)
       global mouse  
       print(mouse+mouse1)     
       if mouse[0]<=-1:
           mouse1[0]=1
           mouse[0]= mouse[0]+2
       elif mouse[1]<=-1:
           mouse1[1]=1
           mouse[1]= mouse[1]+2
       elif mouse[0]>=w:
           mouse1[0]=-1
           mouse[0]= mouse[0]-2
       elif mouse[1]>=h:
           mouse1[1]=-1
           mouse[1]= mouse[1]-2
       dx= mouse1[0]*sizevalue
       dy= mouse1[1]*sizevalue
       C.move(Movingobject, dx, dy)
       C.update()

# def MovePlanner(steps):
#     steglista=[]
#     while steps>0:
#         typavsteg=randint(0, 3)
#         if typavsteg==0:
#             steglista.append("upp")
#         elif typavsteg==1:
#             steglista.append("ner")
#         elif typavsteg==2:
#             steglista.append("vänster")
#         elif typavsteg==3:
#             steglista.append("höger")
#         steps-=1
#     return steglista
def MovePlanner(steps):
    steglista=[]
    formerstep=5
    while steps>0:
        samma=False
        typavsteg=randint(0, 3)
        if typavsteg==0 and formerstep!=1:
            steglista.append("upp")
        elif typavsteg==1 and formerstep!=0:
            steglista.append("ner")
        elif typavsteg==2 and formerstep!=3:
            steglista.append("vänster")
        elif typavsteg==3 and formerstep!=2:
            steglista.append("höger")
        else:
            samma=True
        if samma==False:
            formerstep=typavsteg
            steps-=1
    return steglista
# def MovePlanner(steps,goal):
#     goalx=goal[0]
#     goaly=goal[1]
#     steglista=[]
#     while steps>0:
#         typavsteg=randint(0, 3)
#         if typavsteg==0:
#             steglista.append("upp")
#         elif typavsteg==1:
#             steglista.append("ner")
#         elif typavsteg==2:
#             steglista.append("vänster")
#         elif typavsteg==3:
#             steglista.append("höger")
#         steps-=1
#     return steglista


#Create world
w = 10
h = 10
Map = [[0 for x in range(w)] for y in range(h)] 
food= 1
wall=2
Map[3][3]= food
Map[0][1]= food
map1=([[ 0,0,0,0],
       [ 0,0,0,0],
       [ 0,0,0,0],
       [ 0,0,0,0],
       [ 0,0,0,0]])

#Create world
w = 10
h = 10
Map = [[0 for x in range(w)] for y in range(h)] 
food= 1
wall=2
Map[2][2]= food
Map[0][1]= wall

#Skapa spelplan
C = Canvas(master, bg="green", height=600, width=600)
C.pack()
distanceY=0
distanceX=0
sizevalue=50
for row in range(0,w): 
    for col in range(0,h):
       coord = distanceX, distanceY, distanceX+sizevalue, distanceY+sizevalue #y,x, w, h
       distanceX+=sizevalue
       if Map[col][row]==1:
              C.create_rectangle(coord, fill="yellow")
       elif col%2==0:
              C.create_rectangle(coord, fill="white")
       elif col%2==1:
              C.create_rectangle(coord, fill="gray")
    distanceY+=sizevalue
    distanceX=0

text = Text(master, height=2, width=30)
text.pack()
# Skapa musen v2

Mouse=C.create_rectangle(getcoord(mouse[0],mouse[1]), fill="brown")



# flytta musen
mousemove=MovePlanner(13)
# MovePlanner(13,långtidsminne[0])    #["upp","upp","vänster","vänster","vänster","upp","upp","höger"]

while len(mousemove)>0:
       steg=[0,0]
       C.create_rectangle(getcoord(mouse[0],mouse[1]), fill="blue")
       if mousemove[0]=="upp":
              mouse[1]= mouse[1]-1
              steg[1]-=1
       elif mousemove[0]=="ner":
              mouse[1]= mouse[1]+1 
              steg[1]+=1             
       elif mousemove[0]=="vänster":
              steg[0]-=1
              mouse[0]= mouse[0]-1
       elif mousemove[0]=="höger":
              steg[0]+=1
              mouse[0]= mouse[0]+1
       Movemouse(steg,Mouse)
       FoundCheese(mouse)
       mousemove.pop(0)
       

text.delete("insert linestart", "insert lineend")
text.insert(END, "Out of steps\n Cheese eaten "+str(cheeseeaten))
mainloop()