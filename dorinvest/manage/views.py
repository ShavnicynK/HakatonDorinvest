from datetime import date
from django.db.models import Q
from django.shortcuts import render, redirect
from app.models import *
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required
def manage_page(request):
    try:
        calls = CallForm.objects.filter(status='new')
    except IntegrityError:
        calls = None

    try:
        feedback = FeedBackForm.objects.filter(status='new')
    except IntegrityError:
        feedback = None

    try:
        pickuppet = PickUpPetForm.objects.filter(status='new')
    except IntegrityError:
        pickuppet = None
    else:
        for row in pickuppet:
            row.petname = Pet.objects.get(id=row.pet).name

    return render(request, "manage/manage_page.html", {'pickuppet': pickuppet,
                                                       'feedback': feedback,
                                                       'calls': calls})


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
        meta_title = request.POST['meta_title']
        meta_description = request.POST['meta_description']
        meta_keywords = request.POST['meta_keywords']

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

        return redirect('/manage/pets')

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
def exposition_edit_page(request, pk):
    if request.method == "POST":
        place = request.POST['place']
        date_start = request.POST['date_start']
        date_finish = request.POST['date_finish']
        top_image = request.POST['top_image']

        try:
            if pk > 0:
                Exposition.objects.filter(id=pk).update(place=place,
                                                        date_start=date_start,
                                                        date_finish=date_finish,
                                                        top_image=top_image)
                exposition = Exposition.objects.get(id=pk)
            else:
                Exposition.objects.filter(status='completed').update(status='past')
                exposition = Exposition.objects.create(place=place,
                                                       date_start=date_start,
                                                       date_finish=date_finish,
                                                       top_image=top_image)

        except IntegrityError:
            pass
        else:
            if pk > 0:
                ExpositionPartner.objects.filter(exposition=exposition).delete()

            for partner in request.POST.getlist('partners'):
                partner_obj = Partner.objects.get(id=partner)
                try:
                    ExpositionPartner.objects.create(exposition=exposition, partner=partner_obj)
                except IntegrityError:
                    pass

            if pk > 0:
                ExpositionPet.objects.filter(exposition=exposition).delete()

            for pet in request.POST.getlist('pets'):
                pet_obj = Pet.objects.get(id=pet)
                try:
                    ExpositionPet.objects.create(exposition=exposition, pet=pet_obj)
                except IntegrityError:
                    pass

            return redirect('/manage/expositions')

    data = dict()
    pets = Pet.objects.all()
    for row in pets:
        if row.images.first():
            row.image = row.images.first().image
        else:
            row.image = ''

    data['partners'] = Partner.objects.all()
    data['pets'] = pets

    if pk > 0:
        data['exposition'] = Exposition.objects.get(id=pk)
    else:
        exposition_date =  {}
        exposition_date['date_start'] = date.today()
        exposition_date['date_finish'] = date.today()
        data['exposition'] = exposition_date

    return render(request, 'manage/exposition_edit.html', {'data': data})


@login_required
@csrf_exempt
def expositions_page(request):
    data = Exposition.objects.all().order_by('-id')

    if Exposition.objects.filter(status='active').exists():
        active = 1
    else:
        active = 0

    for row in data:
        row.cats = 0
        row.dogs = 0

        for pet in row.pets.all():
            if pet.type == 'cat':
                row.cats += 1
            else:
                row.dogs += 1

    return render(request, 'manage/expositions.html', {'data': data, 'active': active})


@login_required
@csrf_exempt
def exposition_close_page(request, pk):
    if request.method == "POST":
        description = request.POST['description']

        try:
            Exposition.objects.filter(id=pk).update(description=description, status='completed')
            exposition = Exposition.objects.get(id=pk)
        except IntegrityError:
            pass
        else:
            for image in request.FILES.getlist('images'):
                try:
                    ImageExposition.objects.create(exposition=exposition, image=image)
                except IntegrityError:
                    pass

        return redirect('/manage/expositions')

    else:
        return render(request, 'manage/exposition_close.html', {})


@login_required
@csrf_exempt
def exposition_view_page(request, pk):
    if request.method == "POST":
        description = request.POST['description']

        try:
            Exposition.objects.filter(id=pk).update(description=description, status='past')
            exposition = Exposition.objects.get(id=pk)
        except IntegrityError:
            pass
        else:
            for image in request.FILES.getlist('images'):
                try:
                    ImageExposition.objects.create(exposition=exposition, image=image)
                except IntegrityError:
                    pass

    exposition = Exposition.objects.get(id=pk)

    images = ImageExposition.objects.filter(exposition=exposition)

    return render(request, 'manage/exposition_view.html', {'data': exposition, 'images': images})


@login_required
@csrf_exempt
def exposition_image_drop(request, pk, ipk):
    if ipk > 0:
        try:
            ImageExposition.objects.filter(id=ipk).delete()
        except IntegrityError:
            pass

    return redirect(f'/manage/exposition_view/{pk}')


@login_required
@csrf_exempt
def pet_edit_page(request, pk):
    if request.method == "POST":
        pk = request.POST['pk']
        name = request.POST['name']
        gender = request.POST['gender']
        age = request.POST['age']
        description = request.POST['description']
        ptype = request.POST['type']

        try:
            Pet.objects.filter(id=pk).update(name=name, gender=gender, age=age, description=description, type=ptype)
            pet = Pet.objects.get(id=pk)
        except IntegrityError:
            pass
        else:
            for image in request.FILES.getlist('images'):
                try:
                    ImagePet.objects.create(pet=pet, image=image)
                except IntegrityError:
                    pass

    pet = Pet.objects.get(id=pk)

    images = ImagePet.objects.filter(pet=pk)

    return render(request, 'manage/pet_edit.html', {'data': pet, 'images': images})


@login_required
@csrf_exempt
def pet_image_drop(request, pk, ipk):
    if ipk > 0:
        try:
            ImagePet.objects.filter(id=ipk).delete()
        except IntegrityError:
            pass

    return redirect(f'/manage/pets/edit/{pk}')


@login_required
@csrf_exempt
def call_done(request, pk):
    if pk > 0:
        try:
            CallForm.objects.filter(id=pk).update(status='done')
        except IntegrityError:
            pass

    return redirect('/manage')


@login_required
@csrf_exempt
def feedback_done(request, pk):
    if pk > 0:
        try:
            FeedBackForm.objects.filter(id=pk).update(status='done')
        except IntegrityError:
            pass

    return redirect('/manage')


@login_required
@csrf_exempt
def pickuppet_done(request, pk):
    if pk > 0:
        try:
            PickUpPetForm.objects.filter(id=pk).update(status='done')
        except IntegrityError:
            pass

    return redirect('/manage')

