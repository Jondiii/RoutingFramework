class ConstraintManager:

    def __init__(self):
        pass

    def checkMaxCapacity(self, vehicle):
        return vehicle.capacity

    def checkMinLoad(self, vehicle):
        return vehicle.minLoad

    def checkConstraints(self, Route):
        vehicle = Route.vehicle
        maxCapacity=self.checkMaxCapacity(vehicle)
        minCapacity=self.checkMinLoad(vehicle)
        for i in range (0,len(maxCapacity)):
            if (maxCapacity[i]<vehicle.currentLoad[i]):
                #if(checkMaxCapacity(vehicle) < vehicle.load):#esto esta mal si gestionamos capacity como bidimensional
                return False
        
            if(minCapacity[i] > vehicle.currentLoad[i]):
                return False

        return True