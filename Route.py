class Route:

    vehicle = ""
    jobs = []
    typeData = [] #Can be used as route constrains

    def __init__(self, vehicle, jobs=None):
        self.vehicle = vehicle

        if jobs != None:
            for job in jobs:
                self.jobs.append(job)

    #Adds a new type
    def addTypeData(self, description, value):
        self.typeData.append([description, value])

    #Simultaneously adds various types
    def addVariousTypeData(self, descriptions, values):
        for description, value in zip(descriptions, values):
            self.addTypeData(description, value)

