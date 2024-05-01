from django.db import models
from django_resized import ResizedImageField


girl = 'girl'
boy = 'boy'
GENDERS = [
    (girl, 'girl'),
    (boy, 'boy'),
]

cat = 'cat'
dog = 'dog'
TYPES_PET = [
    (cat, 'cat'),
    (dog, 'dog'),
]

active = 'active'
past = 'past'
ACTIVITIES = [
    (active, 'active'),
    (past, 'past'),
]

new = 'new'
done = 'done'
STATUSES = [
    (new, 'new'),
    (done, 'done'),
]


# партнеры
class Partner(models.Model):
    name = models.CharField(max_length=300, blank=False)
    image = models.ImageField(upload_to='static/images/partners')
    link = models.CharField(max_length=500, blank=True)


# вопросы и ответы
class Question(models.Model):
    question = models.CharField(max_length=2000, blank=False)
    answer = models.CharField(max_length=2000, blank=False)


# животные
class Pet(models.Model):
    name = models.CharField(max_length=300, blank=False)
    gender = models.CharField(max_length=10, choices=GENDERS, default=boy)
    age = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    type = models.CharField(max_length=10, choices=TYPES_PET, default=cat)


# фотографии животных
class ImagePet(models.Model):
    image = ResizedImageField(size=[900, None], quality=100, upload_to='static/images/pets')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='images')


# выставки
class Exposition(models.Model):
    date_start = models.DateField()
    date_finish = models.DateField()
    top_image = models.CharField(max_length=300, blank=False, default='')
    place = models.CharField(max_length=500, blank=False, default='')
    status = models.CharField(max_length=10, choices=ACTIVITIES, default=active)
    pets = models.ManyToManyField(Pet, through='ExpositionPet', related_name='exposition_pet')
    partners = models.ManyToManyField(Partner, through='ExpositionPartner', related_name='exposition_partner')
    description = models.CharField(max_length=3000, blank=True)


# фотографии выставки
class ImageExposition(models.Model):
    image = ResizedImageField(size=[900, None], quality=100, upload_to='static/images/expositions')
    exposition = models.ForeignKey(Exposition, on_delete=models.CASCADE)


class ExpositionPet(models.Model):
    exposition = models.ForeignKey(Exposition, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class ExpositionPartner(models.Model):
    exposition = models.ForeignKey(Exposition, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)


class ImageExpositionImage(models.Model):
    exposition = models.ForeignKey(Exposition, on_delete=models.CASCADE)
    image = models.ForeignKey(ImageExposition, on_delete=models.CASCADE)


class BaseSettings(models.Model):
    full_description = models.CharField(max_length=3000, blank=True)
    form_email = models.CharField(max_length=500, blank=True)
    contact_email = models.CharField(max_length=500, blank=True)
    contact_phone = models.CharField(max_length=500, blank=True)
    contact_address = models.CharField(max_length=500, blank=True)
    contact_telegram = models.CharField(max_length=500, blank=True)
    contact_vkontakte = models.CharField(max_length=500, blank=True)
    contact_odnoklassniki = models.CharField(max_length=500, blank=True)
    statistic_pets = models.IntegerField(default=0)
    statistic_volunteers = models.IntegerField(default=0)
    statistic_pets_home = models.IntegerField(default=0)
    how_get_text = models.CharField(max_length=3000, blank=True)
    contract_file = models.FileField(upload_to='static/files', blank=True)
    meta_title = models.CharField(max_length=300, blank=False, default='')
    meta_description = models.CharField(max_length=500, blank=False, default='')
    meta_keywords = models.CharField(max_length=500, blank=False, default='')


class CallForm(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUSES, default=new)


class FeedBackForm(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length=1500)
    status = models.CharField(max_length=10, choices=STATUSES, default=new)


class PickUpPetForm(models.Model):
    pet = models.IntegerField(default=0)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUSES, default=new)

