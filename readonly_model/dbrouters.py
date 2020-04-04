class ReadOnlyModelRouter:
    """Database router for checking read-only models."""

    read_only_model_field = 'read_only_model'

    def db_for_write(self, model, **hints):
        """
        Database selection method for models.

        Django supports the installation of several databases, and each time
        you work with the database, you need to choose which database will
        work. When choosing a database for writing, this method is called.
        """

        if hasattr(model._meta, self.read_only_model_field):
            read_only_model = getattr(model._meta, self.read_only_model_field)
            model_path = f'{model.__module__}.{model.__name__}'

            assert isinstance(read_only_model, bool), \
                f'Field \'{model_path}.Meta.read_only_model\' must be bool type'

            if read_only_model:
                raise Exception(f'Model \'{model_path}\' is read-only')
