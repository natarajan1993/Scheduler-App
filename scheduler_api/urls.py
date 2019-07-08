from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as api_view

router = DefaultRouter()
router.register('person', api_view.PersonViewset, base_name = 'person')
router.register('event', api_view.EventViewset, base_name = 'event')

urlpatterns = [
    path('',include(router.urls)),
]
