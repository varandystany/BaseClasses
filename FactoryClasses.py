class Factory():
  def ___init___(.self):

    self.Squares = [] #список занимемых квадратов. в СвЕТОВЫХ КОДАХ [[001, 001, 001],[002, 001, 001]] смотри доску в https://miro.com/app/board/uXjVLNKZfEk=/
    self.Area = self.Pos_x 
    
    self.Effective
    
    self.TypeOfResource 
    
    self.Level #от 1 до 10
    
    self.StockCapacityExport
    self.StockCapacityMaxExport
    #Импорт добавляем понадобномти
    
    self.EfficiencyLossRate
    
    self.EfficiencyLossCounter
    
  def EfficiencyLoss(): #потеря эффективность когда счетчик EfficiencyLossCounter заполняеться!
    self.EfficiencyLossCounter += 1
    if self.EfficiencyLossCounter >= self.EfficiencyLossRate:
      self.Effective -= 0.01




class FarmFactory(Factory):
  def ___init___(.self):
    self.SoilQuality
    
    self.StockCapacityMaxExport = 24 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceExport = "Урожай"
#########################################################
class IronMineFactory(Factory):
  def ___init___(.self):
    self.MiningOfResource
    
    self.StockCapacityMaxExport = 50 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceExport = "Железная Руда"

class CoalMineFactory(Factory):
  def ___init___(.self):
    self.MiningOfResource
    
    self.StockCapacityMaxExport = 50 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceExport = "Угольная Руда"
#########################################################
class FoodFactory(Factory):
  def ___init___(.self):
    self.StockCapacityMaxExport = 24 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceImport = "Урожай"
    self.TypeOfResourceExport = "Пища"
    
class BeerFactory(Factory):
  def ___init___(.self):
    self.StockCapacityMaxExport = 24 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceImport = "Урожай"
    self.TypeOfResourceExport = "Пиво"

class MeatFactory(Factory):
  def ___init___(.self):
    self.StockCapacityMaxExport = 24 * self.level
    self.EfficiencyLossRate = 10 # недель это для теста
    self.TypeOfResourceImport = "Урожай"
    self.TypeOfResourceExport = "Mясо"
#########################################################







