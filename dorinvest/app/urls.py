from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'api/expositions/<int:pk>/partners', PartnerViewSet)
urlpatterns = router.urls

