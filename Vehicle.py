
class Vehicle: 
    id = 0; 
    # TYPE will be a matrix that will look like this: 
    # Company    Nestle
    # MTR        600
    # MinLoad    10
    typeData = []
    
    origin = [0,0] # First Pick Up
    dest = [0,0] # Last Drop Off

    capacity = []
    
    hourDriveTime = 240 
    hourBreakTime = 45

    dayDriveTime = 720
    dayBreakTime = 600


    def __init__(self, id) :
        self.id = id

    def addTypeData(self, description, cuantity):
        self.typeData.append([description, cuantity])

    #Define the origin with a set of coordinates (x,y)
    def setOrigin(self,x,y):
        self.origin=[x,y]
    
    #Define the destination with a set of coordinates (x,y)
    def setDestination(self,x,y):
        self.dest=[x,y]

    #Define the origin like a point in the space
    def setOrigin(self,value):
        self.origin=[value]
    
    #Define the destination like a point in the space
    def setDestination(self,value):
        self.dest=[value]

    # Define the max amount of time a driver can drive without making a break 
    # hourDriveTime - minutes
    def setHourDriveTime(self, hourDriveTime): 
        self.hourDriveTime = hourDriveTime
    
    # Define the min amount of time a driver should stop to take a break after the hourDriveTime
    # hourBreakTime - minutes
    def setHourBreakTime(self, hourBreakTime): 
        self.hourBreakTime = hourBreakTime
   

    # Define the max amount of minutes a driver can drive in a day
    # DayDriveTime - minutes
    def setDayDriveTime(self, DayDriveTime): 
        self.DayDriveTime = DayDriveTime
   

    # Define the min amount of time a driver should stop to take a break after a DayHourTime
    # DayBreakTime - minutes
    def setDayBreakTime(self, DayBreakTime): 
        self.DayBreakTime = DayBreakTime



