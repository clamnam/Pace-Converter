import datetime
class Calculator:
    def __init__(self, dist,*time):
        self.dist = dist
        self.time = time


    
    def MilesKilometers(dist):
        return dist * 1.609344
    
    def KilometersMiles(dist):
        return dist * .621371
    
    def pace(dist,time):
        mins, seconds = map(int, time.split(':'))
        seconds = seconds+(mins*60)
        minutedecimal = seconds/60
        singlekmpace = minutedecimal/dist
        singlekmpace = singlekmpace
        minutes = int(singlekmpace)
        secondseconds = int((singlekmpace - minutes) * 60)
        return minutes,":",secondseconds ,"per km",
