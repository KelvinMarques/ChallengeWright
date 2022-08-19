from django.urls import include, path
from rest_framework import routers

from challengeWright_api.views import NoteLenovoViewSet
from .views import ScraperBot

router = routers.DefaultRouter()
router.register(r'lenovo', NoteLenovoViewSet)


urlpatterns = [
   path('', include(router.urls)),
   
]