from typing import List
from datetime import datetime, date

class Person:
    name: str
    def __init__(self, name:str):
        self.name = name

class Period:
    """ 
    The Period class provides for the amount of work/rest days.
    The id provides for a name to reference too.
    """
    id:str
    # startdate = datetime.date
    workdays:int
    restdays:int

    def __init__(self, id:str='period 1', workdays:int=None, restdays:int=None): # startdate:datetime.date,
        self.id = id
        # self.startdate = startdate
        self.workdays = workdays
        self.restdays = restdays

    def create_period(self):
        self.id =input(f"What is the name of the period?:")
        self.workdays = input(f'How many days do you have to work in this period?:')
        self.restdays = input(f'How many restdays do you have after working?:')
class Schedule:
    """ 
    A Schedule is a container for periods and the startdates of all the periods in the schedule.
    The startdates are limited by the scope of the app.
    """
    id:str
    SchedulePeriods:List[Period]=[]
    startdates:list[datetime.date] =[]

    def __init__(self,id:str): #startdates:List[datetime.date],workdates:List[datetime.date], restdates:List[datetime.date],
        self.id = id
        # self.workdates = workdates
        # self.restdates = restdates
        # self.startdates = startdates

    def add_period(self, Period: Period):
        self.SchedulePeriods.append(Period)
        return self.SchedulePeriods


    def get_first_startdate(self):
        first_date = input(f'What is the date of your first day of work?:(dd-mm-yyyy')
        return first_date

    # def get_workdates(self):
    #     pass
    # def get_restdates(self):
    #     pass
# class workdates ???????????????????????
# class overlap ?????????????????????
class Calendar:
    """
    The Calendar contains the workdates and restdate of the schedules. 
    """
    workdates:list[datetime.date] =[]
    restdates:list[datetime.date] =[]

    def __init__(self, id:str):
        self.id = id

    def get_workdates(self):
        pass
    def get_restdates(self):
        pass

class Application:
    scope:int
    def __init__(self, scope:int):
        self.scope = scope
    def scope(self, scope):
        return range(1,scope)


# Create an Application with a scope in days. This is the length of the calendar.
app = Application(365)
# Create the periods. Example "offshore" is 14 days on and 21 days off. 
VliegenKort = Period('Kort',8,6)
# VliegenKort.create_period()
print(VliegenKort.id)
print(VliegenKort.workdays)
print(VliegenKort.restdays)
VliegenLang= Period('Lang', 9,7)
print(VliegenLang.id)
print(VliegenLang.workdays)
print(VliegenLang.restdays)
Offshore = Period('Werk', 14,21)
print(Offshore.id)
print(Offshore.workdays)
print(Offshore.restdays)
# Create a schedule. Example
Vliegen = Schedule('Vliegen')
print(Vliegen.id)
calendar= Calendar('Werk Kalender')
print(calendar.id)
# Add periodes to the schedule.
# Based on first startdate and periodes get workdates.
# Based on first startdate and periodes get restdates.
# Create a Calendar instance.
# Fill Calendar with all workdates and rest dates.
