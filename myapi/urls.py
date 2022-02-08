from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from.views import Tracklist, trackDetail
router = routers.DefaultRouter()
router.register(r'track',Tracklist)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path('detail/<id>/', trackDetail),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]