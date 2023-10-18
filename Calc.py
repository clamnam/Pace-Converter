
class Calculator:
    def __init__(self, dist,time):
        
        self.dist = dist
        self.time = time


        
    def SplitTime(self):
        # handle if input isnt given
        try:
            # make inputted time, machine readable by splitting mins+secs using the mandatory 

            mins, seconds = map(int, self.time.split(':'))
            return mins,seconds
        except:
            return 'Failed on SplitTime'
    
    def MilesKilometers(self):
        # handle if input isnt given
        try:
            # turn miles into km
            return self.dist * 1.609344
        except:
            return 'Failed on MilesKilometers'
    
    def KilometersMiles(self):
        # handle if input isnt given
        try:
            # turn km into miles
            return self.dist * .621371
        except:
            return 'Failed on KilometersMiles'
    
    
    def pace(self):
        # handle if input isnt given
        try:
            mins, seconds = self.SplitTime() #call splitTime to use the entered time easier
        
            seconds = seconds + (mins * 60) #then turn it into seconds
            
            minutedecimal = seconds / 60
            
            singlekmpace = minutedecimal / self.dist
            
            singlekmpace = singlekmpace
            minutes = int(singlekmpace)
            secondseconds = int((singlekmpace - minutes) * 60)

            return minutes, secondseconds
        except:
            return 'Failed on Pace'

    def KmM(self):
        try:
            mins, seconds = self.pace()
            
            # Convert the pace to seconds to complete
            totalSeconds = mins * 60 + seconds

            # Calculate the pace in seconds per kilometer
            kmPace = totalSeconds / .621371

            # Calculate the time to complete 1 kilometer at this pace (in seconds)
            timeToComplete1Unit = kmPace 
            # Convert time to minutes and remaining seconds
            minutes = timeToComplete1Unit // 60
            remainingSeconds = timeToComplete1Unit % 60

            return int(minutes), int(remainingSeconds)
        except:
            return 'Failed on KmM'


    def MkM(self):
        try :
            # Calculate the pace for 1 mile
            mins, seconds = self.pace()
            
            # Convert the pace to seconds per mile
            totalSeconds = mins * 60 + seconds

            # Calculate the pace in seconds per km
            milePace = totalSeconds / 1.609344

            # Calculate the time to complete 1 km at in seconds
            timeToComplete1Unit = milePace

            # Convert time to minutes and remaining seconds
            minutes = timeToComplete1Unit // 60
            remainingSeconds = timeToComplete1Unit % 60

            return int(minutes), int(remainingSeconds)
        except:
            return 'Failed on Mkm'