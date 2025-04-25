### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DedDirectora2277/api_final_yatube.git
```


Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в директорию приложения:
```
cd yatube_api
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Описание:
Данный проект представляет собой ресурс, на котором пользователи могут
создавать посты, комменитировать чужие посты, а также подписываться друг на друга.

### Пирмеры запросов:

Запрос: GET на адрес http://127.0.0.1:8000/api/v1/posts/

Ответ:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Запрос: POST на адрес http://127.0.0.1:8000/api/v1/posts/
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Ответ:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

Подробнее описано в документации http://127.0.0.1:8000/redoc/
