from tkinter import *
master = Tk()
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


print(map1[0][0])




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

mainloop()