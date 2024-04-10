from .models import *
from rest_framework import serializers


# партнеры
class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ()


# вопросы и ответы
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ()


# мерч мероприятия
class MerchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Merch
        fields = ()


# животные
class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ()


# фотографии животных
class ImagePetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagePet
        fields = ()


# фотографии выставки
class ImageExpositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageExposition
        fields = ()


# выставки
class ExpositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exposition
        fields = ()

