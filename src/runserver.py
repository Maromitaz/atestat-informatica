from waitress import serve

from atestat.wsgi import application
# documentation: https://docs.pylonsproject.org/projects/waitress/en/stable/api.html

if __name__ == '__main__':
    serve(application, port='8080')