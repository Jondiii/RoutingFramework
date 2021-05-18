import pandas as pd
import numpy as np

class Job:

    id = 0
    priority = 0 #Es algo que tiene Jsprit, lo ponemos como idea
    typeData = [] #Job information and ADHOC constraints.
    origin = []
    dest = []
    demand = []
    serviceTime = 0
    timeInLocation = 0
    timeWindows = []
    timeWindowMargin = 0  #A margin indicates how earlier a job can be done

    def __init__(self, id):
        self.id = id

    def setId(self, id):
        self.id = id

    def setPriority(self, priority):
        self.priority = priority

    #Adds a new type
    def addTypeData(self, description, value):
        self.typeData.append([description, value])

    #Simultaneously adds various types
    def addVariousTypeData(self, descriptions, values):
        for description, value in zip(descriptions, values):
            self.addTypeData(description, value)

    #Stablishes the origin as a pair of X and Y coordinates
    def setOrigin(self,x,y):
        self.origin=[x,y]
    
    #Stablishes the origin as a pair of X and Y coordinates
    def setDestination(self,x,y):
        self.dest=[x,y]

    #Stablishes the origin as a point in space
    def setOrigin(self,value):
        self.origin=[value]
    
    #Stablishes the origin as a point in space
    def setDestination(self,value):
        self.dest=[value]
    
    #TODO de momento solo es una copia del addType
    #Adds a new demand
    def addDemand(self, description, cuantity):
        self.demand.append([description, cuantity])

    #TODO de momento solo es una copia del addVariousTypes
    #Simultaneously adds various demands
    def addVariousDemands(self, descriptions, cuantities):
        for description, cuantity in zip(descriptions, cuantities):
            self.addDemand(description, cuantity)
    
    def setServiceTime(self, time):
        self.serviceTime = time

    def setTimeInLocation(self, time):
        self.timeInLocation = time

    #Adds a new time window
    def addTW(self, begin, end):
        self.timeWindows.append([begin, end])

    #Adds a new time window and a margin
    def addTW(self, begin, end, margin):
        self.timeWindows.append([begin, end])
        self.setTimeWindowMargin = margin

    #Simultaneously adds various time windows
    def addVariousTW(self, begins, ends):
        for begin, end in zip(begins, ends):
            self.addTW(begin, end)

    def setTimeWindowMargin(self, margin):
        self.timeWindowMargin = margin

    