""" 
In deze File probeer ik het rooster te maken dmv de factory methode. 
De producten zijn Person en schema, en de factory is rooster. 
"""

from abc import ABC, abstractmethod
from datetime import date, datetime, timedelta

class Person(ABC):
    """ Basic representation of a Person """
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def name(self):
        return self.name
    
    def print_name(self):
        """ Prints the name """

class Schedule(ABC):
    """
    Basic representation of a schedule. 
    It has a name.
    It has a start date.
    The amount of days that have to be worked, and the amount of rest days earned.
    The methods return lists of dates.
    """
    workdates =[]
    restdates =[]
    def __init__(self,name, workdays, restdays, startdate):
        self.name = name
        self.workdays = workdays
        self.restdays = restdays
        startdate = startdate

    @abstractmethod
    def print_schedule(self):
        """ Prints the details of the schedule """

class RoosterFactory(ABC):
    def __init__(self, name):
        self.name = name

    def get_person(self, person):
        """ Gets the person how the rooster belongs to. """

    def add_schedule(self, schedule):
        """
        Adds a schedule to the rooster. A rooster kan have multiple schedules.
        The schedule are ordered one after the other
        """
    def print_rooster():
        """ Prints the rooster """


    @abstractmethod
    def print_rooster():
        """ Prints the details of the rooster """

class Offshore(Person):
    def __init__(self,name):
        self.name = name
        
    def name(self):
        return self.name

    def print_name(self):
        print(f'My name is {self.name} and I work Offshore.')

class Aviator(Person):
    def __init__(self,name):
        self.name = name

    def name(self):
        return self.name

    def print_name(self):
        print(f'My name is {self.name} and I fly Aeroplanes.')

class OffshoreSched(Schedule):
    def __init__(self, name, workdays, restdays):
        self.name = name
        self.workdays = workdays
        self.restdays = restdays
        
    
    def get_workdates(self, startdate):
        workdates=[]
        startdate= datetime.strptime(startdate,'%d-%m-%Y').date()
        for date in range(self.workdays):
            day = (startdate + timedelta(days=date))
            self.workdates.append(day.strftime('%d-%m-%Y'))
        return workdates
    
    def get_restdates(self, startdate):
        restdates = []
        startdate= datetime.strptime(startdate,'%d-%m-%Y').date()
        for date in range(self.workdays):
            day = (startdate + timedelta(date+self.workdays))
            self.restdates.append(day.strftime('%d-%m-%Y'))
        return restdates
    
    def print_schedule(self):
        print(f'My {self.name} work schedule has {self.workdays} days on and {self.restdays} days off.')

class AviatorSched(Schedule):
    def __init__(self, name, workdays, restdays):
        self.name = name
        self.workdays = workdays
        self.restdays = restdays
        
    
    def get_workdates(self, startdate):
        workdates=[]
        startdate= datetime.strptime(startdate,'%d-%m-%Y').date()
        for date in range(self.workdays):
            day = (startdate + timedelta(days=date))
            self.workdates.append(day.strftime('%d-%m-%Y'))
        return workdates
    
    def get_restdates(self, startdate):
        restdates = []
        startdate= datetime.strptime(startdate,'%d-%m-%Y').date()
        for date in range(self.workdays):
            day = (startdate + timedelta(date+self.workdays))
            self.restdates.append(day.strftime('%d-%m-%Y'))
        return restdates
    
    def print_schedule(self):
        print(f'My {self.name} work schedule has {self.workdays} days on and {self.restdays} days off.')
   
class Offshore_rooster(RoosterFactory):
    def __init__(self, name, person, schedule):
        self.name = name
        self.person = person
        self.schedule = schedule

    def get_person(self) -> Person:
        return Offshore

    def add_schedule(self) -> Schedule:
        return OffshoreSched

    def print_rooster(self):
        print(f'Dit is {self.name} Rooster')


def main():
    joris = Offshore('Joris')
    print(joris.name)
    joris_schedule = OffshoreSched('normal',14,21)
    joris_schedule.get_workdates('11-11-2021')
    joris_schedule.get_restdates('11-11-2021')
    print(joris_schedule.workdates)
    print(joris_schedule.restdates)
    joris_schedule.print_schedule()
    jorisRooster = Offshore_rooster('Joris',joris,joris_schedule)
    jorisRooster.add_schedule()
    jorisRooster.print_rooster()
if __name__ == '__main__':
    main()