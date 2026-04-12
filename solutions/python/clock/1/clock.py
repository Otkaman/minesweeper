class Clock:
    def __init__(self, hour, minute):
        self.total = (hour * 60 + minute)%1440
        
    def __repr__(self):       
        return f'Clock({self.total//60}, {self.total%60})'

    def __str__(self):  
        return f'{self.total//60:02}:{self.total%60:02}'

    def __eq__(self, other):
        return self.total == other.total 

    def __add__(self, minutes):
        return Clock(0,self.total+minutes)

    def __sub__(self, minutes):
        return Clock(0,self.total-minutes)
