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
   
    pickupServiceTime = 0 
    dropoffServiceTime = 0 

    #timeInLocation = 0
    timeInLocationForPickUp = 0 
    timeInLocationForDelivery = 0

    #timeWindows = []
    timeWindowsPickUp = []
    pickupTimeWindowMargin = 0 

    timeWindowDelivery = []
    deliveryTimeWindowMargin = 0
    
    #timeWindowMargin = 0  #A margin indicates how earlier a job can be done


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
    def addDemand(self, description, quantity):
        self.demand.append([description, quantity])

    #TODO de momento solo es una copia del addVariousTypes
    #Simultaneously adds various demands
    def addVariousDemands(self, descriptions, quantities):
        for description, quantity in zip(descriptions, quantities):
            self.addDemand(description, quantity)
    
    #def setServiceTime(self, time):
    #    self.serviceTime = time

    def setPickupServiceTime(self, pickupServiceTime): 
        self.pickupServiceTime = pickupServiceTime

    def setDropoffServiceTime (self, dropoffServiceTime): 
        self.dropoffServiceTime = dropoffServiceTime

    def setTimeInLocationForPickUp(self, timeInLocationForPickUp):
        self.timeInLocationForPickUp = timeInLocationForPickUp

    def setTimeInLocationForDelivery(self, timeInLocationForDelivery): 
        self.timeInLocationForDelivery = timeInLocationForDelivery
    
    
    #Adds a new time window
    def addTWPickup(self, begin, end):
        self.timeWindowsPickUp.append([begin, end])

    #Adds a new time window and a margin
    def addTWPickup(self, begin, end, margin):
        self.timeWindowsPickUp.append([begin, end])
        self.setPickUpTimeWindowMargin = margin

    #Simultaneously adds various time windows
    def addVariousPickUpTW(self, begins, ends):
        for begin, end in zip(begins, ends):
            self.addTWPickup(begin, end)

    def setPickUpTimeWindowMargin(self, margin):
        self.pickupTimeWindowMargin = margin
    
    #Adds a new time window
    def addTWDelivery(self, begin, end):
        self.timeWindowDelivery.append([begin, end])

    #Adds a new time window and a margin
    def addTWDelivery(self, begin, end, margin):
        self.timeWindowDelivery.append([begin, end])
        self.setDeliveryTimeWindowMargin = margin

    #Simultaneously adds various time windows
    def addVariousDeliveryTW(self, begins, ends):
        for begin, end in zip(begins, ends):
            self.addTWDelivery(begin, end)

    def setDeliveryTimeWindowMargin(self, margin):
        self.deliveryTimeWindowMargin = margin

   

    