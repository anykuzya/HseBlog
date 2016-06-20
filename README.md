# HseBlog

Для запуска необходимо установить django v >= 1.8, python3


Создание базы данных:

`python manage.py makemigrations common_blog`
`python manage.py migrate`
Запустить сервер:

`python manage.py runserver`


После этого в браузере по адресу 127.0.0.1:8000 видим наш сайт.


  При переходе по ссылке "Войти" можно увидеть окно входа и ссылку на регистрацию.
  
  
  Зарегистированный пользователь может писать статьи, первые абзацы которых будут отображаться на главной странице или по ссылке /articles.
  
  
  Также залогиненному пользователю досупно написание комментариев и оценка существующих статей по двухбальной шкале: "+" или "-" (оценка осуществляется без перезагрузки страницы с использованием ajax).
  
  
  Проект реализован средствами django-framework'a. Оформление - простейшая каскадная таблица стилей.
  
  
