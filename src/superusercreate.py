from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'pass')
print("Cont de utilizator cu privilegii creat cu succes.")