from django.apps import AppConfig
from django.contrib.auth import get_user_model

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        User = get_user_model()

        # create admin only if not exists
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@test.com",
                password="Hitesh@2013"
            )