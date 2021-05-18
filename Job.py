
class Job:

    id = 0
    typeData = []
    origin = [0,0]
    dest = [0,0]
    demand = 0

    def __init__(self, id):
        self.id = id

    def addTypeData(self, description, cuantity):
        self.typeData.append([description, cuantity])

    #Establece el origen como coordenada X y coordenada Y
    def setOrigin(self,x,y):
        self.origin=[x,y]
    
    #Establece el destino como coordenada X y coordenada Y
    def setDestination(self,x,y):
        self.dest=[x,y]

    #Establece el origen como un punto en el espacio
    def setOrigin(self,value):
        self.origin=[value]
    
    #Establece el destino como un punto en el espacio
    def setDestination(self,value):
        self.dest=[value]
