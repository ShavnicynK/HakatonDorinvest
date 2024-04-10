from .models import *
from .serializers import *
from rest_framework import viewsets


# партнеры
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


# вопросы и ответы
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# мерч мероприятия
class MerchViewSet(viewsets.ModelViewSet):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer


# животные
class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


# фотографии животных
class ImagePetViewSet(viewsets.ModelViewSet):
    queryset = ImagePet.objects.all()
    serializer_class = ImagePetSerializer


# фотографии выставки
class ImageExpositionViewSet(viewsets.ModelViewSet):
    queryset = ImageExposition.objects.all()
    serializer_class = ImageExpositionSerializer


# выставки
class ExpositionViewSet(viewsets.ModelViewSet):
    queryset = Exposition.objects.all()
    serializer_class = ExpositionSerializer


