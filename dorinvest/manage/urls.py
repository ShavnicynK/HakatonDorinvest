from django.urls import path
from .views import *


urlpatterns = [
    path('manage', manage_page, name='manage'),
    path('manage/settings', settings_page, name='settings'),
    path('manage/expositions', expositions_page, name='expositions'),
    path('manage/exposition_edit/<int:pk>', exposition_edit_page, name='exposition_edit'),
    path('manage/exposition_view/<int:pk>', exposition_view_page, name='exposition_view'),
    path('manage/exposition_close/<int:pk>', exposition_close_page, name='exposition_close'),
    path('manage/exposition/<int:pk>/image/delete/<int:ipk>', exposition_image_drop, name='exposition_image_drop'),
    path('manage/partners', partners_page, name='partners'),
    path('manage/partners/delete/<int:pk>', partner_drop, name='partner_delete'),
    path('manage/questions', questions_page, name='questions'),
    path('manage/questions/delete/<int:pk>', question_drop, name='question_delete'),
    path('manage/pets', pets_page, name='pets'),
    path('manage/pets/delete/<int:pk>', pet_drop, name='pet_delete'),
    path('manage/pets/edit/<int:pk>', pet_edit_page, name='pet_edit_page'),
    path('manage/pets/edit/<int:pk>/image/delete/<int:ipk>', pet_image_drop, name='pet_image_drop'),
    path('manage/calldone/<int:pk>', call_done, name='call_done'),
    path('manage/pickuppetdone/<int:pk>', pickuppet_done, name='pickuppet_done'),
    path('manage/feedbackdone/<int:pk>', feedback_done, name='feedback_done'),
]
