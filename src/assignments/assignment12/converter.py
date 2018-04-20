class Converter:
    def get_miles_from_km(self,km):
        
        miles = km * .621371
        miles = round(miles, 2)
        return 'Miles: ' + str(miles)
