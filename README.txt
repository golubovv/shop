Для начала работы необходимо установить следующие пакеты

Django 3.2          //// команда pip install Django==3.2
python-dotenv       //// команда pip install python-dotenv
psycopg2            //// команда pip install psycopg2
Pillow              //// команда pip install Pillow

+ установленный на системе postgresql

В директории shop/shopet создать файл .env, в этом файле указать приватные переменные
ниже находится пример заполненого файла:

---------------------- Файл .env -----------------------------
SECRET_KEY = %cie*mik8m%*_z=#r-%$)9ji#=$ztfft06jk@j4f74i50*z)cf         //// Секретный ключ ......
DEBUG = True                                                            //// Режим отладки Да/Нет

ENGINE = django.db.backends.postgresql
DATABASE = MyNameDataBase       //// Название базы данных
USER = NameUser                 //// Имя пользователя для авторизации в БД
PASSWORD = UserPassword         //// Пароль для пользователя в БД
DB_HOST = localhost             //// .... Хост по умолчанию localhost
DB_PORT = 8000                  //// .... Порт по умолчанию 8000, но если не пойдет что-то, то можно удалить
----------------------  Конец файл .env -----------------------------