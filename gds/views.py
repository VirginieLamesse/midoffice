from django.db.models import Q
from rest_framework import generics, mixins
from gds.serializers import *
from gds.models import *
from gds.request.detail import Mail
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


# this view allow only read methods
class SchedChangeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pnr'
    serializer_class = SchedChangeSerializer

    def get_queryset(self):
        qs = SchedChange.objects.all() # Getting all contracts
        
        # ------ Getting querystrings if exists ----------
        dk = self.request.GET.get("dk")
        
        if dk is not None:
            qs = qs.filter(
                Q(dk = dk) # searching for contracts with agency_id
                ).distinct()

        return qs


    def post(self, request, *args, **kwargs): # remove this
        return self.create(request, *args, **kwargs)


class PassengerAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PassengerSerializer

    def get_queryset(self):
        return Passenger.objects.all()
    def post(self, request, *args, **kwargs): # remove this
        return self.create(request, *args, **kwargs)


class ReservationAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'pnr'
    serializer_class = ReservationSerializer

    def get_queryset(self):
        qs = Reservation.objects.filter(is_ticketed=False)

        dk = self.request.GET.get("dk")
        booking_pcc = self.request.GET.get("booking_pcc")

        if dk is not None:
            qs = qs.filter(Q(interface_id = dk)).distinct()
            
        if booking_pcc is not None:
            qs = qs.filter(Q(booking_pcc = booking_pcc)).distinct()

        return qs
    def post(self, request, *args, **kwargs): # remove this
        return self.create(request, *args, **kwargs)

class SegmentAPIView(generics.ListAPIView):
    
    lookup_field = 'id'
    serializer_class = SegmentSchedChangeSerializer

    def get_queryset(self):
        qs = SegmentSched.objects.all()

        pnr = self.request.GET.get("pnr")

        if pnr is not None:      
            qs = qs.filter(Q(pnr = pnr)).distinct()   

        return qs

class SendEmailAPIView(APIView):
    serializer_class = SendEmailSerializer
    
    def get(self, request, format=None):

        pnr = request.query_params.get('pnr', None)
        email = request.query_params.get('email', None)
        if pnr is not None and email is not None:
            obj = Mail().sendMail(email,pnr)
            print(obj)
            resul = 'Done'
        else:
            resul = 'Failed'
        return Response(resul)

class TravelAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = TravelSerializer

    def get_queryset(self):
        qs = Travel.objects.all() 
        return qs

    def post(self, request, *args, **kwargs): # remove this
        return self.create(request, *args, **kwargs)