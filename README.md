# HakatonDorinvest

## REST API


#### GET /api/start
Запрос основных данных лендинга

Запрос:
```html
https://vistavki.srv9.ru/api/start
```

Ответ:
```json
{
    "state": "ok",
    "data": {
        "full_description": "Выставки-пристройства организовывают для того, чтобы помочь найти дом животным из разных приютов и частных передержек. На мероприятии волонтеры рассказывают потенциальным хозяевам про зверей и помогают пристроить их в добрые руки.",
        "form_email": "gbudorinvest@dom.mos.ru",
        "contact_email": "gbudorinvest@dom.mos.ru",
        "contact_phone": "8(499)251-71-43",
        "contact_address": "Государственное бюджетное учреждение города Москвы «Доринвест»\r\n125047, г.Москва, 2-я Тверская-Ямская улица, д.2\r\n",
        "contact_telegram": "https://t.me",
        "contact_vkontakte": "https://vk.com",
        "contact_odnoklassniki": "https://ok.ru",
        "statistic_pets": 65,
        "statistic_volunteers": 20,
        "statistic_pets_home": 25,
        "how_get_text": "Потенциальные хозяева должны заключить договор об ответственном содержании животного. Договор нужен, чтобы новый владелец полностью принял ответственность, а также чтобы защитить питомца на случай, если что-то пойдет не так. ",
        "contract_file": "https://vistavki.srv9.ru/static/files/1.docx",
        "meta_title": "Выставка пристройство бездомных животных",
        "meta_description": "Выставка пристройство бездомных животных",
        "meta_keywords": "Выставка, пристройство, бездомных, животных",
        "exposition_id": 3,
        "status": "active",
        "place": "Лекторий",
        "date_start": "2024-04-18",
        "date_finish": "2024-04-20"
    }
}
```

#### GET /api/expositions/old/images
Получить 15 рандомных фото с прошедших выставок

Запрос:
```html
https://vistavki.srv9.ru/api/expositions/old/images
```

Ответ:
```json
{
    "state": "ok",
    "result": [
        "https://vistavki.srv9.ru/static/images/expositions/R0001975.JPG",
        "https://vistavki.srv9.ru/static/images/expositions/DSC_2228.jpg",
        "https://vistavki.srv9.ru/static/images/expositions/R0002015.JPG",
        "https://vistavki.srv9.ru/static/images/expositions/DSC_2228.jpg",
        "https://vistavki.srv9.ru/static/images/expositions/DSC_2235.jpg",
        "https://vistavki.srv9.ru/static/images/expositions/R0002040.JPG",
        "https://vistavki.srv9.ru/static/images/expositions/DSC_2228.jpg",
        "https://vistavki.srv9.ru/static/images/expositions/R0002018.JPG",
        "https://vistavki.srv9.ru/static/images/expositions/R0001927.JPG",
        "https://vistavki.srv9.ru/static/images/expositions/R0002018.JPG"
    ]
}
```

#### GET /api/expositions/{id выставки}/partners
Возвращает всех партнеров выставки

Запрос:
```html
https://vistavki.srv9.ru/api/expositions/1/partners
```

Ответ:
```json
{
    "state": "ok",
    "result": [
        {
            "name": "Департамент жилищного-комунального хозяйства",
            "link": "https://dorinvest.ru/",
            "image": "https://vistavki.srv9.ru/static/images/partners/depzhil.png"
        },
        {
            "name": "Комплекс городского хозяйства Москвы",
            "link": "https://dorinvest.ru/",
            "image": "https://vistavki.srv9.ru/static/images/partners/depzhil_xGg8f50.png"
        }
    ]
}
```

#### GET /api/expositions/{id выставки}/cats
Возвращает всех кошек для выставки

Запрос:
```html
https://vistavki.srv9.ru/api/expositions/2/cats
```

Ответ:
```json
{
    "state": "ok",
    "result": [
        {
            "id": 5,
            "name": "Айра",
            "gender": "girl",
            "age": "2 года",
            "image": "https://vistavki.srv9.ru/static/images/pets/DSC_1062.jpg"
        }
    ]
}
```

#### GET /api/expositions/{id выставки}/dogs
Возвращает всех собак для выставки

Запрос:
```html
https://vistavki.srv9.ru/api/expositions/1/dogs
```

Ответ:
```json
{
    "state": "ok",
    "result": [
        {
            "id": 1,
            "name": "Айка",
            "gender": "girl",
            "age": "4 года",
            "image": "https://vistavki.srv9.ru/static/images/pets/R0007200.jpg"
        },
        {
            "id": 3,
            "name": "Арахис",
            "gender": "boy",
            "age": "2 года",
            "image": "https://vistavki.srv9.ru/static/images/pets/R0005680.JPG"
        }
    ]
}
```

#### GET /api/pet/{id питомца}
Возвращает информацию о конкретном питомце

Запрос:
```html
https://vistavki.srv9.ru/api/pet/1
```

Ответ:
```json
{
    "state": "ok",
    "result": {
        "id": 1,
        "name": "Айка",
        "gender": "girl",
        "age": "4 года",
        "description": "Описание собаки",
        "images": [
            "https://vistavki.srv9.ru/static/images/pets/R0007200.jpg",
            "https://vistavki.srv9.ru/static/images/pets/R0007201.jpg",
            "https://vistavki.srv9.ru/static/images/pets/R0007218.jpg",
            "https://vistavki.srv9.ru/static/images/pets/R0007221.jpg",
            "https://vistavki.srv9.ru/static/images/pets/R0007226.jpg",
            "https://vistavki.srv9.ru/static/images/pets/R0007190.jpg",
            "https://vistavki.srv9.ru/static/images/pets/R0007191.jpg",
            "https://vistavki.srv9.ru/static/images/pets/R0007194.jpg",
            "https://vistavki.srv9.ru/static/images/pets/R0007197.jpg"
        ]
    }
}
```

#### GET /api/expositions/old
Возвращает все прошедшие выставки и 3 фотки к каждой

Запрос:
```html
https://vistavki.srv9.ru/api/expositions/old
```

Ответ:
```json
{
    "state": "ok",
    "result": [
        {
            "id": 1,
            "date_start": "2024-04-01",
            "date_finish": "2024-04-02",
            "place": "Красная площадь",
            "images": [
                "https://vistavki.srv9.ru/static/images/expositions/DSC_2240.jpg",
                "https://vistavki.srv9.ru/static/images/expositions/DSC_2368.jpg",
                "https://vistavki.srv9.ru/static/images/expositions/DSC_2331.jpg"
            ]
        },
        {
            "id": 2,
            "date_start": "2024-04-03",
            "date_finish": "2024-04-04",
            "place": "вднх",
            "images": [
                "https://vistavki.srv9.ru/static/images/expositions/R0002018.JPG",
                "https://vistavki.srv9.ru/static/images/expositions/R0001927.JPG",
                "https://vistavki.srv9.ru/static/images/expositions/R0002007.JPG"
            ]
        }
    ]
}
```

#### GET /api/expositions/{id выставки}
Возвращает все прошедшие выставки и 3 фотки к каждой

Запрос:
```html
https://vistavki.srv9.ru/api/expositions/2
```

Ответ:
```json

{
    "state": "ok",
    "result": {
        "id": 2,
        "date_start": "2024-04-03",
        "date_finish": "2024-04-04",
        "place": "вднх",
        "description": "выставка прошла успешно",
        "images": [
            "https://vistavki.srv9.ru/static/images/expositions/R0002000.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0002007.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0002011.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0002015.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0002018.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0002040.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0002052.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0001972.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0001975.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0001978.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0001989.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0001921.JPG",
            "https://vistavki.srv9.ru/static/images/expositions/R0001927.JPG"
        ]
    }
}
```

#### GET /api/questions
Возвращает все вопросы и ответы

Запрос:
```html
https://vistavki.srv9.ru/api/questions
```

Ответ:
```json
{
    "state": "ok",
    "result": [
        {
            "question": "Первый вопрос",
            "answer": "Ответ на первый вопрос"
        },
        {
            "question": "Первый вопрос",
            "answer": "Ответ на первый вопрос"
        }
    ]
}
```

#### POST /api/form/call
Добавляет запрос заказ звонка

Запрос:
```html
https://vistavki.srv9.ru/api/form/call
```

Тело запроса:
```json
{
    "name": "name",
    "phone": "phone"
}
```

Ответ:
```json
{
    "state": "ok",
    "message": "processed successfully"
}
```

#### POST /api/form/feedback
Добавляет запрос из формы обратной связи

Запрос:
```html
https://vistavki.srv9.ru/api/form/feedback
```

Тело запроса:
```json
{
    "name": "name",
    "phone": "phone", 
    "email": "email",
    "message": "message"
}
```

Ответ:
```json
{
    "state": "ok",
    "message": "processed successfully"
}
```

#### POST /api/form/pickuppet
Добавляет запрос о желании забрать питомца

Запрос:
```html
https://vistavki.srv9.ru/api/form/pickuppet
```

Тело запроса:
```json
{
    "name": "name",
    "phone": "phone",
    "pet": "pet"
}
```

Ответ:
```json
{
    "state": "ok",
    "message": "processed successfully"
}
```