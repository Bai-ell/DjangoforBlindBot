from django.core.management import call_command

def import_data():
    try:
        print("Импорт данных из data.json...")
        call_command('loaddata', 'data.json')
        print("Данные успешно импортированы!")
    except Exception as e:
        print(f"Ошибка импорта данных: {e}")
