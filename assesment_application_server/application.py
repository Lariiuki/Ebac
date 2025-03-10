from app import application

if __name__ == "__main__":
    application.run()

# gunicorn --bind 0.0.0.0:8000 wsgi:application