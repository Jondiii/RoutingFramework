class Route:

    vehicle = None
    jobs = []
    specialData = [] #Can be used as route constrains

    currentLoad = [] # Current load of the vehicle
    maxCapacity = []

    routeDuration = 0

    def __init__(self, vehicle, jobs=None):
        self.vehicle = vehicle

        if jobs != None:
            for job in jobs:
                self.jobs.append(job)

    #Adds a new type
    def addSpecialData(self, description, value):
        self.specialData.append([description, value])

    #Simultaneously adds various types
    def addVariousSpecialData(self, descriptions, values):
        for description, value in zip(descriptions, values):
            self.specialData(description, value)

