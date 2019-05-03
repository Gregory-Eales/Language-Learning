
class MySubClass(object):
    pass


class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("If this were a real order we would send"
              " '{}' order to '{}'".format(order, self.name))

""""
c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
print([a.name for a in Contact.all_contacts.search('J')])
"""

class LongNameDic(dict):
    def lengest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                pass

class Ultimate(LongNameDic, Supplier):
    pass



class Location:
    def __init__(self, long, lat, country, abm):
        self.long = long
        self.lat = lat
        self.country = country
        self.abm = abm

    def location_hit(self):
        self.long = None
        self.lat = None
        self.country = None

    def distance_from(self, item):
        distance = ((self.long - item.long) ** 2 + (self.lat - item.lat) ** 2) ** 0.5
        return distance


class City(Location):
    def __init__(self, long, lat, country, abm, pop):
        super().__init__(long, lat, country, abm)
        self.pop = pop

    def location_hit(self):
        super().location_hit()
        self.pop = None


class Launch_Point(Location):
    def __init__(self, long, lat, country, abm, missiles, missile_range):
        super().__init__(long, lat, country, abm)
        self.missiles = missiles
        self.missile_range = missile_range

    def location_hit(self):
        super().location_hit()
        self.missiles = None

    def missile_attack(self, target):
        if self.country == target.country:
            raise InvalidTarget("You cannot attack your own country")

        if self.missile_range < self.distance_from(target):
            raise TargetOutOfRange(self.distance_from(target), self.missile_range)

        else:
            target.location_hit()




class Vehicle(Launch_Point):
    def __init__(self, long, lat, country, abm, missiles, detect_rate):
        super().__init__(long, lat, country, abm, missiles)
        self.detect_rate = detect_rate

    def location_hit(self):
        super().location_hit()
        self.detect_rate = None


class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


class InvalidTarget(Exception):
    pass


class TargetOutOfRange(Exception):
    def __init__(self, distance, missile_range):
        super().__init__("Missile is {} units out of range".format(int(distance-missile_range)))
        self.distance = distance
        self.missile_range = missile_range

    def range_overage(self):
        return self.distance - self.missile_range



class Missiles:
    def __init__(self, pay_load, range):
        self.pay_load = pay_load
        self.range = range




Shyan_MT = Launch_Point(100, 100, "USA", 5, 5, 100)
Moscow = Launch_Point(800, 800, "Russia", 5, 5, 100)
Shyan_MT.missile_attack(Moscow)



try:



