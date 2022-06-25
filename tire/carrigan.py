from tire import Tire 
class Carrigan(Tire):
    def __init__(self, qualities):
        self.qualities = qualities

    def needs_service(self):
        count = 0
        qualities = self.qualities
        for i in range(len(qualities)):
            if qualities[i] >= 0.9:
                count += 1
                if(count >= 1):
                    return True
        return False