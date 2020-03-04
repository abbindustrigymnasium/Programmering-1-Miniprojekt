from tkinter import *
import time
master = Tk()

cheeseeaten=0
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
       dx= mouse1[0]*sizevalue
       dy= mouse1[1]*sizevalue
       C.move(Movingobject, dx, dy)
       C.update()


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
       print(Map[col][row])
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
mouse= [5,5]
Mouse=C.create_rectangle(getcoord(mouse[0],mouse[1]), fill="brown")

# flytta musen
mousemove=["upp","upp","vänster","vänster","vänster","upp","upp","höger"]

while len(mousemove)>0:
       print(str(mouse[0])+"  "+str(mouse[1])) #Så man ser vad som händer
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
# T = Text(root, height=2, width=30)
# T.insert(END, "Just a text Widget\nin two lines\n")
# C.update()
mainloop()