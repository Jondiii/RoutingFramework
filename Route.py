class Route:

    vehicle = ""
    jobs = []
    typeData = [] #Can be used as route constrains

    def __init__(self):
        pass

    def __init__(self, vehicle):
        self.vehicle = vehicle

    def __init__(self, vehicle, jobs):
        self.vehicle = vehicle

        for job in jobs:
            self.jobs.append(job)

    #Adds a new type
    def addTypeData(self, description, value):
        self.typeData.append([description, value])

    #Simultaneously adds various types
    def addVariousTypeData(self, descriptions, values):
        for description, value in zip(descriptions, values):
            self.addTypeData(description, value)

