class Calculator:
    def __init__(self, dist: int, time: str):
        self.dist = dist
        self.time = time

    def split_time(self):
        # handle if incorrect input isnt given
        try:
            # make inputted time, machine readable by splitting mins+secs using the mandatory

            mins, seconds = map(int, self.time.split(":"))
            if mins < 0 or seconds < 0 or seconds >= 60:
                return "Minutes need to be positive. Seconds need to be 0-60"
            return mins, seconds
        except:
            return "Incorrect time format"

    def miles_kilometers(self):
        # handle if incorrect input isnt given
        print(self.dist)

        try:
            # turn miles into km
            return self.dist * 1.609344
        except:
            return "Failed on miles_kilometers"

    def kilometers_miles(self):
        # handle if incorrect input isnt given
        try:
            # turn km into miles
            return self.dist * 0.621371
        except:
            return "Failed on kilometers_miles"

    def pace(self):
        # handle if input isnt given

        try:
            (
                mins,
                seconds,
            ) = self.split_time()  # call split_time to use the entered time easier

            seconds = seconds + (mins * 60)  # then turn it into seconds

            minutedecimal = seconds / 60  # make total time into minutes as a decimal

            singlekmpace = minutedecimal / self.dist  # find hard to read single km pace

            # convert singlekmpace to useable format
            minutes = int(singlekmpace)
            secondseconds = int((singlekmpace - minutes) * 60)

            return minutes, secondseconds
        except:
            return "Invalid Time Entry"

    def user_pace(self):
        mins, secs = self.pace()
        result = mins, ":", secs
        return result

    def km_to_miles(self):
        try:
            mins, seconds = self.pace()
            # Convert the pace to seconds to complete
            totalSeconds = mins * 60 + seconds

            # Calculate the pace in seconds per kilometer
            kmPace = totalSeconds / 0.621371

            # Calculate the time to complete 1 kilometer at this pace (in seconds)
            timeToComplete1Unit = kmPace

            # Convert time to minutes and remaining seconds
            minutes = timeToComplete1Unit // 60
            remainingSeconds = timeToComplete1Unit % 60

            result = int(minutes), ":", int(remainingSeconds), "mins/mile"
            return result
        except:
            return "Invalid Time Entry"

    def miles_to_km(self):
        try:
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

            result = int(minutes), ":", int(remainingSeconds), "mins/km"
            return result
        except:
            return "Invalid Time Entry"
