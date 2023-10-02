class Calculator:
    def __init__(self, dist,time):
        self.dist = dist
        self.time = time

    def SplitTime(self,time):
        mins, seconds = map(int, time.split(':'))
        return mins,seconds
    
    def MilesKilometers(self,int):
        return int * 1.609344
    
    def KilometersMiles(self,int):
        return int * .621371
    
    def pace(self, dist , time):
        mins,seconds = self.SplitTime(time)
        seconds = seconds+(mins*60)
        minutedecimal = seconds/60
        singlekmpace = minutedecimal/dist
        singlekmpace = singlekmpace
        minutes = int(singlekmpace)
        secondseconds = int((singlekmpace - minutes) * 60)
        return minutes,secondseconds 

    def KmM(self,dist,time):
        string = ''
        pace = self.pace(dist,time)
        pace = list(pace)
        PaceInSeconds = pace[0]*60+pace[1]
        PaceInSeconds = (self.KilometersMiles(PaceInSeconds))/60
        
        print(round(PaceInSeconds,2))
        
        

    def MkM(self,dist,time):
        pace = self.pace(dist,time)
        pace = list(pace)
        PaceInSeconds = pace[0]*60+pace[1]
        PaceInSeconds = (self.MilesKilometers(PaceInSeconds))/60
        
        print()