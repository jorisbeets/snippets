from typing import List
from datetime import datetime, date

class Person:
    name: str
    def __init__(self, name):
        self.name = name

class Period:
    id:str
    # startdate = datetime.date
    workdays:int
    restdays:int

    def __init__(self, id:str, workdays:int, restdays:int): # startdate:datetime.date,
        self.id = id
        # self.startdate = startdate
        self.workdays = workdays
        self.restdays = restdays

    def create_period(self):
        self.id =input(f"What is the name of the period?:")
        self.workdays = input(f'How many days do you have to work in this period?:')
        self.restdays = input(f'How many restdays do you have after working?:')
class Schedule:
    id:str
    SchedulePeriods:List[Period]=[]
    startdates:list[datetime.date] =[]
    periodes:List[Period] = []

    def __init__(self,id:str,  startdates:List[datetime.date]): #workdates:List[datetime.date], restdates:List[datetime.date],
        self.id = id
        # self.workdates = workdates
        # self.restdates = restdates
        self.startdates = startdates

    

    def get_startdates(self):
        return self.startdates
    def get_workdates(self):
        pass

class Calendar:
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