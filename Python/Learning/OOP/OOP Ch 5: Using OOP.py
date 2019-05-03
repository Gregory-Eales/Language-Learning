from urllib.request import urlopen


class ExampleLocation:
    def __init__(self, long, lat, country):
        self.long = long
        self.lat = lat
        self._country = country

    def _set_country(self, country):
        if not country:
            raise Exception("Not a Country")
        self._country = country

    def _get_country(self):
        return self._country

    def distance_from(self, locatition):
        distance = ((self.long - location.long) ** 2 + (self.lat - location.lat) ** 2) ** 0.5
        return distance

    name = property(_get_country, _set_country)


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content


#####################################################
#                    Exercises                     #
#####################################################

class Country:
    def __init__(self, name):
        self.name = name


class Location:
    def __init__(self, lat, long, abm):
        self.lat = lat
        self.long = long
        self._abm = abm

    def _set_abm(self, abm):
        if not abm:
            raise Exception("Not valid abm value")
        self._abm = abm

    def _get_abm(self):
        return self._abm


class Neutron:
    def __init__(self, number):
        self.number = number

class Atom:
    def __init__(self, protons, neutrons):
        self.protons = protons
        self.neutrons = Neutron(neutrons)
        self.atomic_weight = protons + neutrons

    def return_constituants(self):
        return self.neutrons.number

class MyClass:
    pass

from collections import namedtuple

Stock = namedtuple("Stock", "Symbol Current High Low")
Microsoft = Stock("MSFT", 100, 120, 80)
print(str(Microsoft.High) + " is today's highest stock value for Microsoft")













