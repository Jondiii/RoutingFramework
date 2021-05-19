from Vehicle import Vehicle
from ConstraintManager import ConstraintManager
from Route import Route

vehiculoPrueba = Vehicle(1)
vehiculoPrueba.addCapacity(20, 20, 3, 3)
constraintManager = ConstraintManager()
ruta = Route(vehiculoPrueba)

print(constraintManager.checkConstraints(ruta))
