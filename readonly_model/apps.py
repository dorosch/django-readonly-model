from django import apps
from django import conf
from django.db import models

from readonly_model import settings


class ReadOnlyModelAppConfig(apps.AppConfig):
    """Application settings class for support read-only models."""

    name = settings.READONLY_MODEL.get('NAME')
    verbose_name = 'Django read-only model'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Django doesn't support adding third-party fields to model class Meta.
        # Therefore, the only way to add custom fields is to add them to
        # the list of supported fields 'DEFAULT_NAMES' for the Meta class.
        models.options.DEFAULT_NAMES += (
            settings.READONLY_MODEL.get('META_ATTR'),
        )

        # To save the user from the need to add a database routing class in
        # the application settings, we do this in runtime.
        conf.settings.DATABASE_ROUTERS.append(
            settings.READONLY_MODEL.get('DATABASE_ROUTER')
        )
