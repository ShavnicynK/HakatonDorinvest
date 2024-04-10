# HakatonDorinvest

## REST API

### Mетоды

#### GET /api/expositions
Возвращает все выставки

Запрос:
```html
https://vistavki.dorinvest.ru/api/expositions
```

Ответ:
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "alias": "vistavka-na-lukomore",
            "date_start": "2024-04-19",
            "date_finish": "2024-04-20",
            "place": "Лукоморье, Дуб З",
            "status": "active"
        },
        {
            "id": 2,
            "alias": "vistavka-na-kudikinoy-gore",
            "date_start": "2024-03-19",
            "date_finish": "2024-03-20",
            "place": "Кудыкина гора, Помидорная 7",
            "status": "disable"
        }
    ]
}
```

#### GET /api/expositions/{id exposition}
Возвращает конретную выставку

Запрос:
```html
https://vistavki.dorinvest.ru/api/expositions/1
```

Ответ:
```json
{
    "id": 1,
    "alias": "vistavka-na-lukomore",
    "date_start": "2024-04-19",
    "date_finish": "2024-04-20",
    "place": "Лукоморье, Дуб З",
    "status": "active",
    "meta_title": "Метазаголовк страницы в окне браузера",
    "meta_description": "Метаописание страницы для поисковых систем"
}
```

#### GET /api/expositions/{id exposition}/partners
Возвращает всех партнеров выставки

Запрос:
```html
https://vistavki.dorinvest.ru/api/expositions/1/partners
```

Ответ:
```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Партнер 1",
            "image": "https://vistavki.dorinvest.ru/static/images/partners/image1.jpg",
            "link": "https://partner1.ru"
        },
        {
            "name": "Партнер 2",
            "image": "https://vistavki.dorinvest.ru/static/images/partners/image2.jpg",
            "link": "https://partner2.ru"
        },
        {
            "name": "Партнер 3",
            "image": "https://vistavki.dorinvest.ru/static/images/partners/image3.jpg",
            "link": "https://partner3.ru"
        },
        {
            "name": "Партнер 4",
            "image": "https://vistavki.dorinvest.ru/static/images/partners/image4.jpg",
            "link": "https://partner4.ru"
        },
        {
            "name": "Партнер 5",
            "image": "https://vistavki.dorinvest.ru/static/images/partners/image5.jpg",
            "link": "https://partner5.ru"
        }
    ]
}
```

#### GET /api/expositions/{id exposition}/cats
Возвращает всех кошек для выставки

Запрос:
```html
https://vistavki.dorinvest.ru/api/expositions/1/cats
```

Ответ:
```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,  
            "name": "Мурка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        },
        {
            "id": 2,
            "name": "Мурка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        },
        {
            "id": 3,
            "name": "Мурка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        },
        {
            "id": 4,
            "name": "Мурка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        },
        {
            "id": 5,
            "name": "Мурка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        }
    ]
}
```

#### GET /api/expositions/{id exposition}/dogs
Возвращает всех собак для выставки

Запрос:
```html
https://vistavki.dorinvest.ru/api/expositions/1/gogs
```

Ответ:
```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,  
            "name": "Жучка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        },
        {
            "id": 2,
            "name": "Жучка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        },
        {
            "id": 3,
            "name": "Жучка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        },
        {
            "id": 4,
            "name": "Жучка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        },
        {
            "id": 5,
            "name": "Жучка",
            "gender": "girl",
            "age": "1 год 3 месяца",
            "image": "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
        }
    ]
}
```

#### GET /api/expositions/{id exposition}/pets/{id pet}
Возвращает всех собак для выставки

Запрос:
```html
https://vistavki.dorinvest.ru/api/expositions/1/pets/5
```

Ответ:
```json
{
    "id": 5,
    "name": "Жучка",
    "gender": "girl",
    "age": "1 год 3 месяца",
    "description": "Пушистая зараза",
    "images": [
        "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg",
        "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg",
        "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg",
        "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg",
        "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg",
        "https://vistavki.dorinvest.ru/static/images/pets/image1.jpg"
    ]    
}
```

#### GET /api/questions
Возвращает все вопросы и ответы

Запрос:
```html
https://vistavki.dorinvest.ru/api/questions
```

Ответ:
```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "question": "Вопрос 1",
            "answer": "Ответ на вопрос 1"
        },
        {
            "question": "Вопрос 2",
            "answer": "Ответ на вопрос 2"
        },
        {
            "question": "Вопрос 3",
            "answer": "Ответ на вопрос 3"
        },
        {
            "question": "Вопрос 4",
            "answer": "Ответ на вопрос 4"
        }
    ]
}
```