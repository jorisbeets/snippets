from typing import List
from datetime import datetime, date

class Person:
    name: str
    def __init__(self, name):
        self.name = name

class Period:
    id:str
    startdate = datetime.datetime.date
    workdays:int
    restdays:int

    def __init__(self, id:str, startdate:datetime.date, workdays:int, restdays:int):
        self.id = id
        self.startdate = startdate
        self.workdays = workdays
        self.restdays = restdays

class Schedule:
    id:str
    workdates:list[datetime.date]
    restdates:list[datetime.datetime.date]
    startdates:list[datetime.datetime.date]
    def __init__(self,id:str, workdates:List[datetime.date], restdates:List[datetime.date], startdates:List[datetime.date]):
        self.id = id
        self.workdates = workdates
        self.restdates = restdates
        self.startdates = startdates

