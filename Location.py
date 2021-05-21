class Location: 
    id_location = 0 #Optional
    x = 0
    y = 0

    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def setId(self, id_location):
        self.id_location = id_location

    def setX(self, x):
        self.x = x
        
    def  setY(self, y): 
        self.y = y