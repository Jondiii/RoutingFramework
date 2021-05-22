class ConstraintManager:

    def __init__(self):
        pass

    def checkMaxCapacity(self, route):
        return route.maxCapacity

    def checkMinLoad(self, route):
        return route.minLoad

    def checkConstraints(self, route):
        vehicle = route.vehicle
        maxCapacity=self.checkMaxCapacity(vehicle)    
        minLoad=self.checkMinLoad(vehicle)
        for i in range (0,len(maxCapacity)):
            if (maxCapacity[i]<vehicle.currentLoad[i]):
                return False

        return True

""" # Así es como se me ocurre que podríamos comprobar los constrains introducidos en special data (esto iría dentro de checkConstraints).
    # El problema es que tendríamos que definir cómo gestionar cada uno de esos constraints especiales, así que esta manera no es muy flexible.
        
        for constraint in route.specialData:
            if constraint[0]=="minLoad":            # En specialData, el primer elemento de la lista es la "descripción" del constraint.
                value = list(constraint[1])         # Mientras que el segundo es el valor de dicho constraint.
                if value > route.currentLoad:
                    return False
            
            elif constraint[0]=="minTimeInRoad":
                value = list(constraint[1])         # Idea: que todas las variables se llamen value, de esta forma no se tendrá que asignar
                if value > route.routeDuration:     # memoria a cada variable de todos los constraints. 
                    return False
"""
