 docker build .                
 docker-compose up -d --build 
 docker-compose exec web python manage.py migrate
 docker-compose exec web python manage.py createsuperuser

Получение питомцев из командной строки всех/с фото/ без фото
python manage.py getpets [--has-photos | --no-has-photos]
ссылка на сайт с демо данными
http://swerka.ru/
