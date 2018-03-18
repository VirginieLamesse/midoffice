from django.core.management.base import BaseCommand, CommandError
from gds.models import SchedChange, SegmentSched
from gds.pnr import Pnr, token
from gds.reservation import *
from datetime import datetime

class ScheduleChange(object):

    def __init__(self, object_xml):
        self._object_xml = object_xml

    def getNewListDeparture(self,departure_list):
        new_list_departure = []
        list_departure = []
            
        for i in departure_list:
            new_list_departure.append(datetime.strptime(i, '%Y-%m-%d %H:%M').strftime('%d%B %H:%M')).
        print(new_list_departure)
        

class Command(BaseCommand):
    help = 'Fetch the schedule changes in Q70 - Custom commannd'

    def handle(self, *args, **options):
        
        
        obj_xml = Pnr().display_pnr('CXZMRB')
        schChng = ScheduleChange(obj_xml)
        departure_list = Itinerary().departure_datetime_list(obj_xml)
        sch = schChng.getNewListDeparture(departure_list)
        print(sch)

            