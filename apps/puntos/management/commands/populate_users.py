from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = [
            {
                'username': "yurley@mail.com",
                'first_name': "Yurley",
                'last_name': "Sanchez",
                'password': "admin",
            },
            {
                'username': "mac@mail.com",
                'first_name': "Mac",
                'last_name': "Herrera",
                'password': "admin",
            },
        ]

        for user in users:
            if not User.objects.filter(email=user['username']).exists():
                print(">>> User with username: '{}' created".format(user['username']))
                user_object = User(username=user['username'], email=user['username'], first_name=user['first_name'],
                                   last_name=user['last_name'])
                user_object.set_password(user['password'])
                user_object.save()

        if not User.objects.filter(email='admin@mail.com').exists():
            user_object = User(username='admin', email='admin@mail.com', first_name='admin', last_name="Ziru's Pizza")
            user_object.set_password('admin')
            user_object.is_superuser = True
            user_object.is_staff = True

            user_object.save()

            print(">>> User with username: '{}' created".format('admin'))
