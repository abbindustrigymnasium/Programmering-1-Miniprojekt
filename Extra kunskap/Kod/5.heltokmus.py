from tkinter import *
import time
master = Tk()
from random import randint


#musdetaljer
korttidsminne=[]
långtidsminne=[]
energi=50
mouse= [1,2] #position
#cheese
cheeseeaten=0
cheeseamount=10
currentcheeses=0
cheeseplaces=[[3,3],[2,1],[4,5],[7,3],[2,8],[9,1],[5,7],[8,3],[4,1],[2,7],[5,4]]
speed=0.2

def Createcheese():
    global currentcheeses
    if cheeseamount>currentcheeses:
        ptpc= randint(0, len(cheeseplaces)-1) #placetoplacecheese
        x=cheeseplaces[ptpc][0]
        y=cheeseplaces[ptpc][1]
        C.create_rectangle(getcoord(x,y), fill="yellow")
        currentcheeses+=1
        global Map
        Map[x][y]=1

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
    global Map
    if Map[mousepos[0]][mousepos[1]]==1:
        outputtext= "Found Cheese at"+str(mouse[0])+" X  "+str(mouse[1])+ " Y/nAdded to longterm memory"
        global cheeseeaten
        cheeseeaten+=1
        text.insert(INSERT, outputtext)
        global långtidsminne
        långtidsminne.append([mousepos[0],mousepos[1]])
        C.create_rectangle(getcoord(mousepos[0],mousepos[1]), fill="orange")
        Map[mousepos[0]][mousepos[1]]=0
        global energi
        energi+=10
        global currentcheeses
        currentcheeses-=1

def Movemouse(mouse1,Movingobject):
       time.sleep(speed)
       global mouse    
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
       Createcheese()
       C.update()

def MovePlanner(steps):
    whattodo= randint(0,3)
    if whattodo==0:
        print("kortis")
        korttidsminne= Lookinlongterm(steps)
    elif whattodo==1:
        print("långis")
        korttidsminne= Lookinshortterm(steps)
    else:
        print("random")
        korttidsminne= Wanderrandom(steps)
    print(korttidsminne)
    return korttidsminne


def Lookinshortterm(steps):
    if len(korttidsminne)==0:
        return Wanderrandom(steps)
    else:
        meströrelse=[0,0,0,0]
        for minnen in korttidsminne:
            if minnen=="upp":
                meströrelse[0]+=1
            elif minnen=="ner":
                meströrelse[1]+=1
            elif minnen=="väster":
                meströrelse[2]+=1
            elif minnen=="höger":
                meströrelse[3]+=1
        Lodrätt=""
        Vågrätt=""
        if meströrelse[0]>meströrelse[1]:
            Lodrätt="upp"
        else:
            Lodrätt="ner"
        if meströrelse[2]>meströrelse[3]:
            Vågrätt="väster"
        else:
            Vågrätt="höger"
        steglista=[]
        while steps>0:
            if steps%2==0:
                steglista.append(Lodrätt)
            else:
                steglista.append(Vågrätt)
            steps-=1
        return steglista


def Lookinlongterm(steps):
    if len(långtidsminne)==0:
        return Wanderrandom(steps)
    else:
        Memoryplace= randint(0,len(långtidsminne)-1)
        Minnet=långtidsminne[Memoryplace]
        målX=Minnet[0]-mouse[0]
        målY=Minnet[1]-mouse[1]
        steglista=[]
        while steps>0:
            if målX<0:
                steglista.append("upp")
                målX+=1
            elif målX>0:
                steglista.append("ner")
                målX-=1
            elif målY<0:
                steglista.append("vänster")
                målY+=1
            elif målY>0:
                steglista.append("höger")
                målY-=1
            else:
                steglista.append(Wanderrandom(1)[0])
            steps-=1
        return steglista

def Wanderrandom(steps):
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
       if col%2==0:
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

# MovePlanner(13,långtidsminne[0])    #["upp","upp","vänster","vänster","vänster","upp","upp","höger"]
while energi>0:
    energiförbrukning=randint(1,energi)
    mousemove=MovePlanner(energiförbrukning)
    energi-=energiförbrukning
    print(energiförbrukning)
    while len(mousemove)>0: #Gamla
        steg=[0,0]
        # C.create_rectangle(getcoord(mouse[0],mouse[1]), fill="blue")
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
    text.insert(END, str(energiförbrukning)+" steps taken, "+str(energi)+" energy left!")
       

text.delete("insert linestart", "insert lineend")
text.insert(END, "Out of steps\n Cheese eaten "+str(cheeseeaten))
mainloop()