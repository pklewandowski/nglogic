from django.apps import AppConfig

from app.nglogic.model.nglogic_api_data_model import nglogic_api_data


class NglogicApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.nglogic"

    def ready(self):
        nglogic_api_data.initialize()
