from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url
from django.contrib import admin

from gds.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url( r'^schedchange/$', SchedChangeAPIView.as_view(), name='sched_chance' ),
    url( r'^passengers/$', PassengerAPIView.as_view(), name='list-passenger' ),
    url( r'^reservations/$', ReservationAPIView.as_view(), name='list-reservation' ),
    url( r'^detailschedchange/$', SegmentAPIView.as_view(), name='details' ),
    url(r'^sendemail/$', SendEmailAPIView.as_view(), name='email'),
]


