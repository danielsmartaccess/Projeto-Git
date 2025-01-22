from django.apps import AppConfig


class ApprinvestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apprinvest'

    def ready(self):
        try:
            from . import scheduler
            scheduler.start()
        except Exception as e:
            print(f"Error starting scheduler: {e}")
            # Continue without scheduler for now
            pass
