ORBITAL_PERIOD = {'Mercury' : 0.2408467,
'Venus' :	0.61519726,
'Earth' :	1.0,
'Mars'	: 1.8808158,
'Jupiter' :	11.862615,
'Saturn' :	29.447498,
'Uranus' :	84.016846,
'Neptune' : 164.79132}
ONE_YEAR_SECONDS = 31557600
class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    
    def on_mercury(self):
        years = self.seconds / (ONE_YEAR_SECONDS * ORBITAL_PERIOD['Mercury'])
        return round(years, 2)
    def on_venus(self):
        years = self.seconds / (ONE_YEAR_SECONDS * ORBITAL_PERIOD['Venus'])
        return round(years, 2)
    def on_earth(self):
        years = self.seconds / (ONE_YEAR_SECONDS * ORBITAL_PERIOD['Earth'])
        return round(years, 2)
    def on_mars(self):
        years = self.seconds / (ONE_YEAR_SECONDS * ORBITAL_PERIOD['Mars'])
        return round(years, 2)
    def on_jupiter(self):
        years = self.seconds / (ONE_YEAR_SECONDS * ORBITAL_PERIOD['Jupiter'])
        return round(years, 2)
    def on_saturn(self):
        years = self.seconds / (ONE_YEAR_SECONDS * ORBITAL_PERIOD['Saturn'])
        return round(years, 2)
    def on_uranus(self):
        years = self.seconds / (ONE_YEAR_SECONDS * ORBITAL_PERIOD['Uranus'])
        return round(years, 2)
    def on_neptune(self):
        years = self.seconds / (ONE_YEAR_SECONDS * ORBITAL_PERIOD['Neptune'])
        return round(years, 2)

