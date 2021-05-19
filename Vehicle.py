
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

    kilometerBreakTime=10 #descanso para repostar en minutos
    kilometerDriveTime=360 #tiempo que tarda en repostar 360 por poner algo 


    def __init__(self, id) :
        self.id = id

    #Adds a new type
    def addTypeData(self, description, cuantity):
        self.typeData.append([description, cuantity])

    #Simultaneously adds various types
    def setOrigin(self,x,y):
        self.origin=[x,y]
    
   #Stablishes the origin as a pair of X and Y coordinates
    def setDestination(self,x,y):
        self.dest=[x,y]

    #Stablishes the origin as a point in space
    def setOrigin(self,value):
        self.origin=[value]
    
   #Stablishes the destination as a point in space
    def setDestination(self,value):
        self.dest=[value]

    # Define the max amount of time a driver can drive without making a break 
    # hourDriveTime - minutcityes
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

    #TODO 
    def addCapacity(self, frontCapacity, backCapacity): 
        self.capacity.append([frontCapacity, backCapacity ])

    def setKilometerBreakTime(self,breakTime):
        self.kilometerBreakTime=breakTime

    def setKilometerDriveTime(self, driveTime):
        self.kilometerDriveTime=driveTime
