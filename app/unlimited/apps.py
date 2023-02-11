from django.apps import AppConfig


class UnlimitedConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "unlimited"
    
    def ready(self):
            import unlimited.signals