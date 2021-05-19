class ConstraintManager:

    def __init__(self):
        pass

    def checkConstrains(Route):
        vehicle = Route.vehicle

        if(checkMaxCapacity(vehicle) < vehicle.load):
            return False
        
        if(checkMinLoad(vehicle) > vehicle.load):
            return False


    def checkMaxCapacity(vehicle):
        return vehicle.capacity

    def checkMinLoad(vehicle):
        return vehicle.minLoad