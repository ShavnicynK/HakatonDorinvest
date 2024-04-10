from django.db import models


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
disabled = 'disabled'
ACTIVITIES = [
    (active, 'active'),
    (disabled, 'disabled'),
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


# мерч мероприятия
class Merch(models.Model):
    label = models.CharField(max_length=300, blank=False)
    image = models.ImageField(upload_to='static/images/merch')


# животные
class Pet(models.Model):
    name = models.CharField(max_length=300, blank=False)
    gender = models.CharField(max_length=10, choices=GENDERS, default=boy)
    age = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    type = models.CharField(max_length=10, choices=TYPES_PET, default=cat)


# фотографии животных
class ImagePet(models.Model):
    image = models.ImageField(upload_to='static/images/pets')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


# выставки
class Exposition(models.Model):
    alias = models.CharField(max_length=300, blank=False)
    date_start = models.DateField()
    date_finish = models.DateField()
    place = models.CharField(max_length=500, blank=False)
    status = models.CharField(max_length=10, choices=ACTIVITIES, default=active)
    meta_title = models.CharField(max_length=300, blank=False)
    meta_description = models.CharField(max_length=500, blank=False)
    pets = models.ManyToManyField(Pet, through='ExpositionPet', related_name='exposition_pet')
    partners = models.ManyToManyField(Partner, through='ExpositionPartner', related_name='exposition_partner')


# фотографии выставки
class ImageExposition(models.Model):
    image = models.ImageField(upload_to='static/images/expositions')
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



