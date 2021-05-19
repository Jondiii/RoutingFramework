class ConstraintManager:

    def __init__(self):
        pass

    def checkMaxCapacity(self, vehicle):
        return vehicle.capacity

    def checkMinLoad(self, vehicle):
        return vehicle.minLoad

    def checkConstraints(self, Route):
        vehicle = Route.vehicle

        if(checkMaxCapacity(vehicle) < vehicle.load):
            return False
        
        if(checkMinLoad(vehicle) > vehicle.load):
            return False

        return True