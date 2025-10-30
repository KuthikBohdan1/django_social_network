### 🆕 Створення проєкту Django з шаблону

#### 1\. Клонування репозиторію

Для початку, склонуйте репозиторій із шаблоном собі на комп'ютер:

```bash
git clone https://github.com/volodymyrlogika/django_template.git
```

#### 2\. Створення нового проєкту

Перейдіть до каталогу, де ви хочете створити новий проєкт. Потім скористайтеся командою `django-admin startproject`, вказавши шлях до склонованого шаблону:

```bash
django-admin startproject --template=/шлях/до/шаблону назва_проєкту .
```

### ⚙️ Підготовка та запуск

#### 1\. Віртуальне середовище

Створіть та активуйте віртуальне середовище для ізоляції залежностей проєкту.

  * **Створення:**
    ```bash
    python -m venv .venv
    ```
  * **Активація:**
      * **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
      * **Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```

#### 2\. Встановлення залежностей

Встановіть усі необхідні бібліотеки з файлу `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### 3\. Міграції бази даних

Застосуйте міграції для створення необхідних таблиць у базі даних:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 4\. Створення суперкористувача

Створіть адміністратора для доступу до панелі управління Django:

```bash
python manage.py createsuperuser
```

#### 5\. Запуск сервера

Запустіть локальний сервер розробки, щоб перевірити роботу проєкту:

```bash
python manage.py runserver
```







{
    "message": [
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-29T21:25:54.790155+02:00",
            "message": "message 1",
            "file": null
        },
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-29T21:56:20.272447+02:00",
            "message": "message 2",
            "file": null
        },
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-30T14:29:27.243248+02:00",
            "message": "adssads",
            "file": null
        },
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-30T14:29:36.609726+02:00",
            "message": "asdasdasda",
            "file": null
        },
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-30T14:29:42.929441+02:00",
            "message": "asdasdsa",
            "file": null
        },
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-30T15:01:13.849849+02:00",
            "message": "asdasd",
            "file": null
        },
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-30T15:05:20.273577+02:00",
            "message": "sfdfsd",
            "file": null
        },
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-30T16:05:18.767609+02:00",
            "message": "returnjnjknj",
            "file": null
        },
        {
            "user_email": "admin@gmail.com",
            "date": "2025-10-30T17:52:48.496852+02:00",
            "message": "куегкт 2",
            "file": null
        }
    ]
}