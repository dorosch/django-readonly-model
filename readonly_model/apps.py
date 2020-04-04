from django.db import models
from django.conf import settings
from django.apps import AppConfig


class ReadOnlyModelAppConfig(AppConfig):
    """Application settings class for support read-only models."""

    name = 'readonly_model'
    verbose_name = "Django read-only model"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Django doesn't support adding third-party fields to model class Meta.
        # Therefore, the only way to add custom fields is to add them to
        # the list of supported fields 'DEFAULT_NAMES' for the Meta class.
        models.options.DEFAULT_NAMES += ('read_only_model',)

        # To save the user from the need to add a database routing class in
        # the application settings, we do this in runtime.
        settings.DATABASE_ROUTERS.append(
            'readonly_model.dbrouters.ReadOnlyModelRouter'
        )
