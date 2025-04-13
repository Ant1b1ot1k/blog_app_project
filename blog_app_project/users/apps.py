from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # import signals here to bring it all together
    def ready(self):
        # This method is called when the application is fully loaded.
        # Importing 'users.signals' here registers all signal handlers defined in that module (in this case signals.py file)
        import users.signals
