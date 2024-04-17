import random
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


@api_view(['GET'])
def get_start(request):
    settings = BaseSettings.objects.get(id=1)

    settings_dict = {}

    settings_dict['full_description'] = settings.full_description
    settings_dict['form_email'] = settings.form_email
    settings_dict['contact_email'] = settings.contact_email
    settings_dict['contact_phone'] = settings.contact_phone
    settings_dict['contact_address'] = settings.contact_address
    settings_dict['contact_telegram'] = settings.contact_telegram
    settings_dict['contact_vkontakte'] = settings.contact_vkontakte
    settings_dict['contact_odnoklassniki'] = settings.contact_odnoklassniki
    settings_dict['statistic_pets'] = settings.statistic_pets
    settings_dict['statistic_volunteers'] = settings.statistic_volunteers
    settings_dict['statistic_pets_home'] = settings.statistic_pets_home
    settings_dict['how_get_text'] = settings.how_get_text
    settings_dict['contract_file'] = request._current_scheme_host + f'/{settings.contract_file}'
    settings_dict['meta_title'] = settings.meta_title
    settings_dict['meta_description'] = settings.meta_description
    settings_dict['meta_keywords'] = settings.meta_keywords

    if Exposition.objects.filter(status='active').exists():
        exposition = Exposition.objects.get(status='active')
    elif Exposition.objects.filter(status='completed').exists():
        exposition = Exposition.objects.get(status='completed')
    else:
        exposition = None

    if exposition:
        settings_dict['exposition_id'] = exposition.id
        settings_dict['status'] = exposition.status
        settings_dict['place'] = exposition.place
        settings_dict['date_start'] = exposition.date_start
        settings_dict['date_finish'] = exposition.date_finish

        if exposition.status == 'completed':
            settings_dict['exposition_description'] = exposition.description
            images = ImageExposition.objects.filter(exposition=exposition)
            images_list = []
            for image in images:
                images_list.append(request._current_scheme_host + f'/{image.image}')
            settings_dict['exposition_images'] = images_list

    return Response({"state": "ok", "data": settings_dict})


# партнеры
@api_view(['GET'])
def get_partners(request, pk):

    if ExpositionPartner.objects.filter(exposition_id=pk).exists():
        result = []
        partners = ExpositionPartner.objects.filter(exposition_id=pk)
        for partner in partners:
            partner_item_dict = {}
            partner_item = Partner.objects.get(id=partner.partner_id)
            partner_item_dict['name'] = partner_item.name
            partner_item_dict['link'] = partner_item.link
            partner_item_dict['image'] = request._current_scheme_host + f'/{partner_item.image}'

            result.append(partner_item_dict)

        return Response({"state": "ok", "result": result})

    else:
        return Response({"state": "error", "message": "no data"})


@api_view(['GET'])
def get_questions(request):

    if Question.objects.filter().exists():
        result = []
        questions = Question.objects.filter()
        for question in questions:
            question_item_dict = {}
            question_item_dict['question'] = question.question
            question_item_dict['answer'] = question.answer

            result.append(question_item_dict)

        return Response({"state": "ok", "result": result})

    else:
        return Response({"state": "error", "message": "no data"})


@api_view(['GET'])
def get_dogs(request, pk):

    if ExpositionPet.objects.filter(exposition_id=pk).exists():
        result = []
        pets = ExpositionPet.objects.filter(exposition_id=pk)
        for pet in pets:
            dog_item_dict = {}
            pet_item = Pet.objects.get(id=pet.pet_id)
            if pet_item.type == 'dog':
                dog_item_dict['id'] = pet_item.id
                dog_item_dict['name'] = pet_item.name
                dog_item_dict['gender'] = pet_item.gender
                dog_item_dict['age'] = pet_item.age
                dog_item_dict['image'] = request._current_scheme_host + f'/{pet_item.images.all().first().image}'

                result.append(dog_item_dict)

        return Response({"state": "ok", "result": result})

    else:
        return Response({"state": "error", "message": "no data"})


@api_view(['GET'])
def get_cats(request, pk):

    if ExpositionPet.objects.filter(exposition_id=pk).exists():
        result = []
        pets = ExpositionPet.objects.filter(exposition_id=pk)
        for pet in pets:
            dog_item_dict = {}
            pet_item = Pet.objects.get(id=pet.pet_id)
            print(pet_item.type)
            if pet_item.type == 'cat':
                print(pet_item)
                dog_item_dict['id'] = pet_item.id
                dog_item_dict['name'] = pet_item.name
                dog_item_dict['gender'] = pet_item.gender
                dog_item_dict['age'] = pet_item.age
                dog_item_dict['image'] = request._current_scheme_host + f'/{pet_item.images.all().first().image}'

                result.append(dog_item_dict)

        return Response({"state": "ok", "result": result})

    else:
        return Response({"state": "error", "message": "no data"})


@api_view(['GET'])
def get_pet(request, pk):

    if Pet.objects.filter(id=pk).exists():
        result = {}
        pet = Pet.objects.get(id=pk)
        result['id'] = pet.id
        result['name'] = pet.name
        result['gender'] = pet.gender
        result['age'] = pet.age
        result['description'] = pet.description
        pet_image = []
        for image in pet.images.all():
            pet_image.append(request._current_scheme_host + f'/{image.image}')

        result['images'] = pet_image

        return Response({"state": "ok", "result": result})

    else:
        return Response({"state": "error", "message": "no data"})


@api_view(['GET'])
def get_old_expositions_image(request):
    if Exposition.objects.filter(status='active').exists():
        exposition = Exposition.objects.get(status='active')
    elif Exposition.objects.filter(status='completed').exists():
        exposition = Exposition.objects.get(status='completed')
    else:
        exposition = None
    if exposition:
        images = ImageExposition.objects.exclude(exposition_id=exposition.id)

        random_images = random.choices(images, k=10)

        expositions_image = []
        for image in random_images:
            expositions_image.append(request._current_scheme_host + f'/{image.image}')

        return Response({"state": "ok", "result": expositions_image})

    else:
        return Response({"state": "error", "message": "no data"})


@api_view(['GET'])
def get_old_expositions(request):
    expositions = Exposition.objects.filter(status='past')
    expositions_list = []
    for exposition in expositions:
        exposition_dict = {}
        exposition_dict['id'] = exposition.id
        exposition_dict['date_start'] = exposition.date_start
        exposition_dict['date_finish'] = exposition.date_finish
        exposition_dict['place'] = exposition.place
        images = ImageExposition.objects.filter(exposition_id=exposition.id)

        random_images = random.choices(images, k=3)

        expositions_image = []
        for image in random_images:
            expositions_image.append(request._current_scheme_host + f'/{image.image}')

        exposition_dict['images'] = expositions_image

        expositions_list.append(exposition_dict)

    return Response({"state": "ok", "result": expositions_list})


@api_view(['GET'])
def get_exposition(request, pk):

    if Exposition.objects.filter(id=pk).exists():
        exposition = Exposition.objects.get(id=pk)
        exposition_dict = {}
        exposition_dict['id'] = exposition.id
        exposition_dict['date_start'] = exposition.date_start
        exposition_dict['date_finish'] = exposition.date_finish
        exposition_dict['place'] = exposition.place
        exposition_dict['description'] = exposition.description
        images = ImageExposition.objects.filter(exposition_id=exposition.id)

        expositions_image = []
        for image in images:
            expositions_image.append(request._current_scheme_host + f'/{image.image}')

        exposition_dict['images'] = expositions_image

        return Response({"state": "ok", "result": exposition_dict})


@api_view(['POST'])
def save_callform(request):

    name = request.data.get('name')
    phone = request.data.get('phone')

    try:
        CallForm.objects.create(name=name, phone=phone)
    except IntegrityError:
        return Response({"state": "error", "message": "error add"})
    else:
        return Response({"state": "ok", "message": "processed successfully"})


@api_view(['POST'])
def save_feedbackform(request):

    name = request.data.get('name')
    phone = request.data.get('phone')
    email = request.data.get('email')
    message = request.data.get('message')

    try:
        CallForm.objects.create(name=name, phone=phone, email=email, message=message)
    except IntegrityError:
        return Response({"state": "error", "message": "error add"})
    else:
        return Response({"state": "ok", "message": "processed successfully"})


@api_view(['POST'])
def save_pickuppetform(request):

    name = request.data.get('name')
    phone = request.data.get('phone')
    pet = request.data.get('email')

    try:
        CallForm.objects.create(name=name, phone=phone, pet=pet)
    except IntegrityError:
        return Response({"state": "error", "message": "error add"})
    else:
        return Response({"state": "ok", "message": "processed successfully"})