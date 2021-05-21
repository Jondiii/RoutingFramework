from Location import Location
import pandas as pd
import numpy as np

class Job:

    id_job = 0
    priority = 0 #Es algo que tiene Jsprit, lo ponemos como idea
    specialData = [] #Job information and ADHOC constraints.
    origin =  Location.init(0,0)
    destination =  Location.init(0,0)
    demand = []
   
    pickupservicetime = 0 
    dropoffservicetime = 0 

    #timeInLocation = 0
    timeInLocationForPickUp = 0 
    timeInLocationForDelivery = 0

    #timeWindows = []
    timeWindowsPickUp = []
    timeWindowDelivery = []
    
    timeWindowMargin = 0  #A margin indicates how earlier a job can be done

    def __init__(self, id_job):
        self.id_job = id_job

    def setId(self, id_job):
        self.id_job = id_job

    def setPriority(self, priority):
        self.priority = priority

    #Adds a new type
    def addSpecialData(self, description, value):
        self.specialData.append([description, value])

    #Simultaneously adds various types
    def addVariousSpecialData(self, descriptions, values):
        for description, value in zip(descriptions, values):
            self.addSpecialData(description, value)

    #Simultaneously adds various types
    def setOrigin(self,x,y):
        #self.origin=[x,y]
        self.origin(x, y)
    
   #Stablishes the origin as a pair of X and Y coordinates
    def setDestination(self,x,y):
        self.destination(x, y)
        #self.destination=[x,y]


    #Stablishes the origin as a point in space
    def setOrigin(self,value):
        self.origin=[value]
    
    #Stablishes the origin as a point in space
    def setDestination(self,value):
        self.destination=[value]
    
    #TODO de momento solo es una copia del addType
    #Adds a new demand
    def addDemand(self, description, cuantity):
        self.demand.append([description, cuantity])

    #TODO de momento solo es una copia del addVariousTypes
    #Simultaneously adds various demands
    def addVariousDemands(self, descriptions, cuantities):
        for description, cuantity in zip(descriptions, cuantities):
            self.addDemand(description, cuantity)
    
    #def setServiceTime(self, time):
    #    self.serviceTime = time

    def setPickupServiceTime(self, pickupservicetime): 
        self.pickupservicetime = pickupservicetime

    def setDropoffServiceTime (self, dropoffservicetime): 
        self.dropoffservicetime = dropoffservicetime

    def setTimeInLocationForPickUp(self, timeInLocationForPickUp):
        self.timeInLocationForPickUp = timeInLocationForPickUp

    def setTimeInLocationForDelivery(self, timeInLocationForDelivery): 
        self.timeInLocationForDelivery = timeInLocationForDelivery
    
    
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

    