from django.contrib.auth.models import User


users = User.objects.all()
print(users)