from tire import Tire 
class Carrigan(Tire):
    def __init__(self, qualities):
        self.qualities = qualities

    def needs_service(self):
       
        qualities = self.qualities    
        return sum(qualities) >=3