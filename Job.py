import pandas as pd
import numpy as np
class Job:

    id = 0
    typeData = []
    origin = []
    dest = []
    demand = []

    def __init__(self, id):
        self.id = id

    def setID(self, id):
        self.id = id

    #Adds a new type
    def addTypeData(self, description, cuantity):
        self.typeData.append([description, cuantity])

    #Simultaneously adds various types
    def addVariousTypeData(self, descriptions, cuantities):
        for description, cuantity in zip(descriptions, cuantities):
            self.addTypeData(description, cuantity)

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
