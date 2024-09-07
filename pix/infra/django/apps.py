from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class PixConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pix'

    # def ready(self):
    #     #autodiscover_modules('pix')
    #     import pix.infra.database.models
