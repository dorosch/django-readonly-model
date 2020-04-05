from django.utils.translation import gettext_lazy as _

from readonly_model import settings
from readonly_model import exceptions


class ReadOnlyModelRouter:
    """Database router for checking read-only models."""

    def db_for_write(self, model, **hints):
        """
        Database selection method for models.

        Django supports the installation of several databases, and each time
        you work with the database, you need to choose which database will
        work. When choosing a database for writing, this method is called.
        """

        field = settings.READONLY_MODEL.get('META_ATTR')

        if hasattr(model._meta, field):
            # Get value of META_ATTR in Meta class from model
            read_only_model = getattr(model._meta, field)

            # Get path to the model
            model_path = f'{model.__module__}.{model.__name__}'

            assert isinstance(read_only_model, bool), \
                _(f"Field '{model_path}.Meta.{field}' must be bool type")

            if read_only_model:
                raise exceptions.ReadOnlyModel(
                    _(f"Model '{model_path}' is read-only")
                )
