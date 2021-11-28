from abc import ABC, abstractclassmethod, abstractmethod
from datetime import date, datetime, timedelta
from typing import List


class IObject(ABC):
    @abstractmethod
    def __init__(self,id:str):
        """ implement in Child """

class Person(IObject):
    def __init__(self, id:str):
        self.id = id
    
    def print_name():
        print(f'My name is {id}')
  

class Schedule(IObject):
    def __init__(self, id:str, workdays:int, restdays:int):
        self.id = id
        self.workdays = workdays
        self.restdays = restdays

    def print_name(self):
        print(f'My schedule is {self.workdays} days on and {self.restdays} days off')

class Period(IObject):
    workdates = []
    restdates = []
    
    def __init__(self, id:str, startdate:str):
        self.id = id
        self.startdate = datetime.strptime(startdate,'%d-%m-%Y').date()
    
    def work_dates(self, workdays):
        for date in range(workdays):
            day = (self.startdate + timedelta(date))
            self.workdates.append(day)
        # workdates = [self.startdate + timedelta(days=i) for i in range(workdays)]
        # return workdates

    def restdates(self, restdays, workdays):
        restdates = [self.startdate + timedelta(days=i+workdays) for i in range(restdays)]
        return restdates
    
class Roster(IObject):
    def __init__(self, id:str):
        self.id = id
        self.components = []

    def add_component(self, component):
        self.components.append(component.id)

    def print_rooster(self):
        print('Het Rooster')




def main():
    # Person instance
    caro =Person('Caroline')
    # caro.print_name()
    # Schedule instance
    caroSched = Schedule('kort',8,6)
    caroSched.print_name()
    # Period instance
    caroPeriod = Period('1','11-11-2021')
    caroworkdates = caroPeriod.work_dates(caroSched.workdays)
    carorestdates = caroPeriod.restdates(caroSched.restdays, caroSched.workdays)
    print(caroPeriod.workdates)
    # Roster instance   
    CaroRoster = Roster('Caroline dr Rooster')
    CaroRoster.add_component(caro)
    CaroRoster.add_component(caroSched)
    CaroRoster.add_component(caroPeriod)
    print(CaroRoster.components)




if __name__ == '__main__':
    main()
    # Periode1 = ConcretePeriod.get_startdate