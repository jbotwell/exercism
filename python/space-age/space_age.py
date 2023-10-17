class SpaceAge:
    planet_years_in_seconds = {
        "mercury": 7600544,
        "venus": 19414149,
        "earth": 31558149,
        "mars": 59355036,
        "jupiter": 374355660,
        "saturn": 929292360,
        "uranus": 2651370000,
        "neptune": 5200418600,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def space_age(self, planet):
        return round(self.seconds / self.planet_years_in_seconds[planet], 2)

    def on_mercury(self):
        return self.space_age("mercury")

    def on_venus(self):
        return self.space_age("venus")

    def on_earth(self):
        return self.space_age("earth")

    def on_mars(self):
        return self.space_age("mars")

    def on_jupiter(self):
        return self.space_age("jupiter")

    def on_saturn(self):
        return self.space_age("saturn")

    def on_uranus(self):
        return self.space_age("uranus")

    def on_neptune(self):
        return self.space_age("neptune")
