from FactoryClasses.py import *
from HousingClasses.py import *

TestFarm = FarmFactory()
for i in range(10):
  input()
  print(TestFarm.TypeOfResourceExport)
  print(TestFarm.StockCapacityExport)
  print(TestFarm.StockCapacityMaxExport)
