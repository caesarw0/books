import os
import sys
import django
from django.core.management import call_command

def setup_django():
    # Set the Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")

    # Setup Django
    django.setup()

def run_migrations():
    print("Running makemigrations...")
    call_command('makemigrations')
    print("Running migrate...")
    call_command('migrate')

def load_initial_data():
    print("Loading initial data...")
    call_command('loaddata', 'initial_data.json')

def run_server():
    print("Starting the server...")
    call_command('runserver', '0.0.0.0:8000')

if __name__ == "__main__":
    try:
        setup_django()
        run_migrations()
        load_initial_data()
        run_server()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting...")
        sys.exit(1)
