from abc import ABC, abstractmethod


class Event(ABC):
    """ Basic representation of a event. """
    
    dates =[]

    @abstractmethod 
    def get_startdate(self):
        """ Retreive the startdate of the event """

    def get_enddate(self):
        """ Retrieve the end date of the event """

class ConcreteEvent(Event):
    get_startdate =input("Start date: dd-mm-yyyy")
    get_enddate =input("End date: dd-mm-yyyy")
