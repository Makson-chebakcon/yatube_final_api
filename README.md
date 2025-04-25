
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
