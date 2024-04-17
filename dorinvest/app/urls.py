from django.urls import path
from .views import *

urlpatterns = [
    path('api/expositions/<int:pk>/partners', get_partners, name='get_partners'),
    path('api/expositions/<int:pk>/dogs', get_dogs, name='get_dogs'),
    path('api/expositions/<int:pk>/cats', get_cats, name='get_cats'),
    path('api/expositions/old/images', get_old_expositions_image, name='get_old_expositions_image'),
    path('api/expositions/old', get_old_expositions, name='get_old_expositions'),
    path('api/expositions/<int:pk>', get_exposition, name='get_exposition'),
    path('api/pet/<int:pk>', get_pet, name='get_pet'),
    path('api/start', get_start, name='get_start'),
    path('api/questions', get_questions, name='get_questions'),
    path('api/form/call', save_callform, name='save_callform'),
    path('api/form/feedback', save_feedbackform, name='save_feedbackform'),
    path('api/form/pickuppet', save_pickuppetform, name='save_pickuppetform'),
]
