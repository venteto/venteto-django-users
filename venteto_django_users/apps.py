from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "venteto_django_users"
    label = "zzv_users"
    verbose_name = "zzv: Auth Users (Custom via PyPI)"
