import os
import django
import random
from faker import Faker

# Настройте настройки Django для скрипта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homework20.settings')
django.setup()

# Импорт модели после инициализации Django
from HW20.models import Article

def add_random_articles(num_articles=10):
    fake = Faker()  # Создаем экземпляр класса Faker

    for _ in range(num_articles):
        # Генерация фейковых данных для каждой статьи
        title = fake.sentence()
        content = fake.text()

        # Создание новой записи в базе данных
        Article.objects.create(title=title, content=content)

# Укажите, сколько статей вы хотите создать
add_random_articles(10)  # Это создаст 10 статей
