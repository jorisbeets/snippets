from typing import List
from datetime import datetime, date, timedelta

class Person:
    name: str
    def __init__(self, name:str):
        self.name = name

class Period:
    """ 
    The Period class provides for the amount of work/rest days.
    The id provides for a name to reference too.
    Period is a generator........
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

    # def __name__(self):
    #     print(self.id)

    def create_period(self):
        """ 
        Gather user inputs needed to create the periods needed in the schedules.
        """
        self.id =input(f"What is the name of the period?:")
        self.workdays = input(f'How many days do you have to work in this period?:')
        self.restdays = input(f'How many restdays do you have after working?:')
class Schedule:
    """ 
    A Schedule is a container for periods and the startdates of all the periods in the schedule.
    The startdates are limited by the scope of the app.
    """
    id:str
    first_date:str
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

    def print_schedules(self):
        print(f'The periodes in {self.id} are:')
        for periode in self.SchedulePeriods:
            print(f'Periode {self.SchedulePeriods.index(periode)+1} heet {periode.id} en is {periode.workdays} dagen op en {periode.restdays} dagen af.')


    def get_first_startdate(self):
        """ 
        get_first_startdate asks the User for the first date of the first Period. This is later used to calculate all other dates.
        """
        self.first_date = '1-1-2021'
        # self.first_date = input(f'What is the date of your first day of work?:(dd-mm-yyyy):')
        return self.first_date

    def get_schedule_length(self)-> int:
        length =0
        for period in self.SchedulePeriods:
            length_period = period.workdays+period.restdays
            length += length_period
        print(length)
        return length

    def get_periodes_in_scope(self)->int:
        """ 
        ! first initioate instance and add periods.
        Returns the amount of periods in the app scope.
        """
        amount=0
        schedule_length=0
        for period in self.SchedulePeriods:
            period_days = period.workdays +period.restdays
            amount += period_days
        amount = (app.scope//amount)+1
        return amount
            
    def get_startdates(self)->List[date]:
        """ 
        Mischien het aantal periodes inde scope in een lijst zetten en dan door de lijst iterreren voor de startdates????????????
        """
        stardates:List[datetime.date]=[]
        schedule_length = self.SchedulePeriods[0].workdays +self.SchedulePeriods[1].workdays+ self.SchedulePeriods[0].restdays+self.SchedulePeriods[1].restdays
        for period in range(0,self.get_periodes_in_scope()):
            startdate = datetime.strptime(self.first_date,'%d-%m-%Y').date()+timedelta(days=schedule_length)
            self.first_date = datetime.strftime(startdate, '%d-%m-%Y')
            self.startdates.append(startdate)
        # for date in self.startdates:
        #     print(date)
        return stardates

        
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
    def scope_range(self, scope):
        return range(1,scope)


# Create an Application with a scope in days. This is the length of the calendar.
app = Application(365)
# Create a Person to Own a Schedule.
Caroline = Person('Caroline')
# print(Caroline.name)
# Create the periods. Example "offshore" is 14 days on and 21 days off. 
VliegenKort = Period('Kort',8,6)
# VliegenKort.create_period()
# print(VliegenKort.id)
# print(VliegenKort.workdays)
# print(VliegenKort.restdays)
VliegenLang= Period('Lang',9,7)
# print(VliegenLang.id)
# print(VliegenLang.workdays)
# print(VliegenLang.restdays)
Offshore = Period('Werk',14,21)
# print(Offshore.id)
# print(Offshore.workdays)
# print(Offshore.restdays)
# Create a schedule. Example
Vliegen = Schedule('Vliegen')
Vliegen.get_first_startdate()
print(Vliegen.first_date)
# print(Vliegen.id)
# Add periodes to the schedule.
Vliegen.add_period(VliegenKort)
Vliegen.add_period(VliegenLang)
# Vliegen.print_schedules()

# Vliegen.get_schedule_length()
# Vliegen.get_periodes_in_scope()
# Based on first startdate and periodes get workdates.
Vliegen.get_startdates()
print(Vliegen.startdates)
# Based on first startdate and periodes get restdates.
# Create a Calendar instance.
calendar= Calendar('Werk Kalender')
# print(calendar.id)
# Fill Calendar with all workdates and rest dates.
