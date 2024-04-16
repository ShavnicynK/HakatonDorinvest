from django.urls import path
from .views import *


urlpatterns = [
    path('manage', manage_page, name='manage'),
    path('manage/settings', settings_page, name='settings'),
    path('manage/expositions', exposition_add_page, name='expositions'),
    path('manage/partners', partners_page, name='partners'),
    path('manage/partners/delete/<int:pk>', partner_drop, name='partner_delete'),
    path('manage/questions', questions_page, name='questions'),
    path('manage/questions/delete/<int:pk>', question_drop, name='question_delete'),
    path('manage/pets', pets_page, name='pets'),
    path('manage/pets/delete/<int:pk>', pet_drop, name='pet_delete'),
]
