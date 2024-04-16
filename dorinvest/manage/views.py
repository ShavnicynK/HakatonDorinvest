from django.shortcuts import render
from app.models import BaseSettings, Partner, Question, Pet, ImagePet, Exposition, ExpositionPartner, ExpositionPet
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required
def manage_page(request):

    return render(request, "manage/manage_page.html", {})


@login_required
@csrf_exempt
def settings_page(request):
    if request.method == "POST":
        setting_id = request.POST['setting_id']
        full_description = request.POST['full_description']
        form_email = request.POST['form_email']
        contact_email = request.POST['contact_email']
        contact_phone = request.POST['contact_phone']
        contact_address = request.POST['contact_address']
        contact_telegram = request.POST['contact_telegram']
        contact_vkontakte = request.POST['contact_vkontakte']
        contact_odnoklassniki = request.POST['contact_odnoklassniki']
        statistic_pets = request.POST['statistic_pets']
        statistic_volunteers = request.POST['statistic_volunteers']
        statistic_pets_home = request.POST['statistic_pets_home']
        how_get_text = request.POST['how_get_text']
        contract_file = request.FILES['contract_file']
        meta_title = request.FILES['meta_title']
        meta_description = request.FILES['meta_description']
        meta_keywords = request.FILES['meta_keywords']

        try:
            BaseSettings.objects.update_or_create(id=setting_id, defaults={
                'full_description': full_description,
                'form_email': form_email,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'contact_address': contact_address,
                'contact_telegram': contact_telegram,
                'contact_vkontakte': contact_vkontakte,
                'contact_odnoklassniki': contact_odnoklassniki,
                'statistic_pets': statistic_pets,
                'statistic_volunteers': statistic_volunteers,
                'statistic_pets_home': statistic_pets_home,
                'how_get_text': how_get_text,
                'contract_file': contract_file,
                'meta_title': meta_title,
                'meta_description': meta_description,
                'meta_keywords': meta_keywords
            })
        except IntegrityError:
            pass

    if BaseSettings.objects.filter(id=1).exists():
        settings = BaseSettings.objects.get(id=1)
        data = {
            'setting_id': settings.id,
            'full_description': settings.full_description,
            'form_email': settings.form_email,
            'contact_email': settings.contact_email,
            'contact_phone': settings.contact_phone,
            'contact_address': settings.contact_address,
            'contact_telegram': settings.contact_telegram,
            'contact_vkontakte': settings.contact_vkontakte,
            'contact_odnoklassniki': settings.contact_odnoklassniki,
            'statistic_pets': settings.statistic_pets,
            'statistic_volunteers': settings.statistic_volunteers,
            'statistic_pets_home': settings.statistic_pets_home,
            'how_get_text': settings.how_get_text,
            'contract_file': request._current_scheme_host + f'/{settings.contract_file}',
            'meta_title': settings.meta_title,
            'meta_description': settings.meta_description,
            'meta_keywords': settings.meta_keywords
        }
    else:
        data = {
            'setting_id': '1',
            'full_description': '',
            'form_email': '',
            'contact_email': '',
            'contact_phone': '',
            'contact_address': '',
            'contact_telegram': '',
            'contact_vkontakte': '',
            'contact_odnoklassniki': '',
            'statistic_pets': 0,
            'statistic_volunteers': 0,
            'statistic_pets_home': 0,
            'how_get_text': '',
            'contract_file': '',
            'meta_title': '',
            'meta_description': '',
            'meta_keywords': ''
        }

    return render(request, 'manage/settings.html', {'data': data})


@login_required
@csrf_exempt
def partners_page(request):
    if request.method == "POST":
        name = request.POST['name']
        link = request.POST['link']
        image = request.FILES['image']

        try:
            Partner.objects.create(name=name, link=link, image=image)
        except IntegrityError:
            pass

    data = Partner.objects.all()

    return render(request, 'manage/partners.html', {'data': data})


@login_required
@csrf_exempt
def partner_drop(request, pk):
    if pk > 0:
        try:
            Partner.objects.filter(id=pk).delete()
        except IntegrityError:
            pass

    data = Partner.objects.all()

    return render(request, 'manage/partners.html', {'data': data})


@login_required
@csrf_exempt
def questions_page(request):
    if request.method == "POST":
        question = request.POST['question']
        answer = request.POST['answer']

        try:
            Question.objects.create(question=question, answer=answer)
        except IntegrityError:
            pass

    data = Question.objects.all()

    return render(request, 'manage/questions.html', {'data': data})


@login_required
@csrf_exempt
def question_drop(request, pk):
    if pk > 0:
        try:
            Question.objects.filter(id=pk).delete()
        except IntegrityError:
            pass

    data = Question.objects.all()

    return render(request, 'manage/questions.html', {'data': data})


@login_required
@csrf_exempt
def pets_page(request):
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        age = request.POST['age']
        description = request.POST['description']
        ptype = request.POST['type']

        try:
            pet = Pet.objects.create(name=name, gender=gender, age=age, description=description, type=ptype)
        except IntegrityError:
            pass
        else:
            for image in request.FILES.getlist('images'):
                try:
                    ImagePet.objects.create(pet=pet, image=image)
                except IntegrityError:
                    pass

    data = Pet.objects.all()
    for row in data:
        if row.images.first():
            row.image = row.images.first().image
        else:
            row.image = ''

    return render(request, 'manage/pets.html', {'data': data})


@login_required
@csrf_exempt
def pet_drop(request, pk):
    if pk > 0:
        try:
            Pet.objects.filter(id=pk).delete()
        except IntegrityError:
            pass

    data = Pet.objects.all()
    for row in data:
        if row.images.first():
            row.image = row.images.first().image
        else:
            row.image = ''

    return render(request, 'manage/pets.html', {'data': data})


@login_required
@csrf_exempt
def exposition_add_page(request):
    if request.method == "POST":
        place = request.POST['place']
        date_start = request.POST['date_start']
        date_finish = request.POST['date_finish']

        try:
            exposition = Exposition.objects.create(place=place, date_start=date_start, date_finish=date_finish, top_image='')
        except IntegrityError:
            pass
        else:
            for partner in request.POST.getlist('partners'):
                partner_obj = Partner.objects.get(id=partner)
                try:
                    ExpositionPartner.objects.create(exposition=exposition, partner=partner_obj)
                except IntegrityError:
                    pass

            for pet in request.POST.getlist('pets'):
                pet_obj = Pet.objects.get(id=pet)
                try:
                    ExpositionPet.objects.create(exposition=exposition, pet=pet_obj)
                except IntegrityError:
                    pass

    data = dict()
    pets = Pet.objects.all()
    for row in pets:
        if row.images.first():
            row.image = row.images.first().image
        else:
            row.image = ''

    data['partners'] = Partner.objects.all()
    data['pets'] = pets

    return render(request, 'manage/exposition_add.html', {'data': data})