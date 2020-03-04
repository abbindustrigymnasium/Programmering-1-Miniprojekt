class Person():

    
    def GetFamilyName(self):
        name=self.mother.name
        names=[]
        if self.male==True:
            self.father.name
        return name

    def Marry(self,other):
        if self.male==False:
            self.lastname=other.lastname
        else:
            other.lastname=self.lastname
        self.married=True
        
    
    def __init__(self,name=None, father=None,mother=None,male=True ):
        self.mother = mother
        self.father = father
        self.male=male
        self.syskon = []
        if name==None:
            self.name = self.GetFamilyName()
        else:
            self.name = name
        if mother!=None:
            self.lastname = mother.lastname
        else:
            self.lastname="Snow"


    def ReturnName(self):
        if self.father==None or self.mother==None:
            print( "I am",self.name,self.lastname, "first of my kind")
        else:
            print( "I am",self.name,self.lastname," daugther of", self.father.name, "and", self.mother.name)


Jon = Person("Jon",None, None)
Joana = Person("Joana",None, None,False)
Joana.lastname="Anka"
Joana.Marry(Jon)
Gini= Person(None,Jon,Joana,False)
Gini.ReturnName()
        
Starks={"father":"Rickard","mother":"Lyarra","lastname":"Stark","Married":True,"Children":["Brandon","Eddard","Lyanna","Benjen"]}
Rickard = Person(Starks.get("father"),None, None)
Lyarra = Person(Starks.get("mother"),None, None,False)
Rickard.lastname=Starks.get("lastname")
if Starks.get("married")==True:
    Rickard.Marry(Lyarra)
Peps=[Rickard,Lyarra]
for Child in Starks.get("Children"):
    Pep = Person(Child,Rickard,Lyarra)
    Peps.append(Pep)

for Pep in Peps:
    Pep.ReturnName()


https://grammis.se/wp-content/uploads/2016/11/Grammisvinnare-1969-2018.doc
https://grammis.se/wp-content/uploads/2016/11/Nominerade-vinnare-1969-2018.xlsx
    Nominerade-vinnare-1969-2017.xlsx