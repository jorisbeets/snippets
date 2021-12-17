""" 
Deze variant is bedoeld om de rooster te maken met het gebruik van dictionaries/tuples ipv classes.
Dit sluit het gebruik van classes niet uit, maar ik probeer de data in dicts/tuples te vangen ipv classes.

voorbeeld:
self.group = dict(a=1, b=2, c=3)
print self.group['a']
https://docs.python.org/3/library/collections.html#collections.namedtuple
 """
from collections import namedtuple
from typing import NamedTuple
 
# class Schedule: weet niet of dat de class iets toevoegt.
# Schedule = namedtuple('Schedule',['workdays0','restdays0','workdays1','restdays1'], defaults=[None,None])
class Schedule(NamedTuple):
    name:str= ''
    workdays0:int = None
    restdays0:int = None
    workdays1:int = None
    restdays1:int = None


vliegen =Schedule( 'vliegen',8 ,6, 9,7)
Offshore = Schedule('offhsore',14,21)
# print(vliegen.workdays0,vliegen.restdays0,vliegen.workdays1,vliegen.restdays1)
# print(Offshore.workdays0,Offshore.restdays0,Offshore.workdays1,Offshore.restdays1)