#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line

def create_superuser():
    from django.contrib.auth.models import User  # Импортируем модель после настройки Django
    username = "admin5"
    email = "admin5@example.com"
    password = "5"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Суперпользователь создан")
    else:
        print("Суперпользователь уже существует")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        import django
        django.setup()  # Инициализация Django
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Теперь, когда Django настроен, создадим суперпользователя
    create_superuser()

    # Запуск административных команд Django
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
