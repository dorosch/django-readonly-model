from django.db import models


class BaseTestModel(models.Model):
    pass


class ReadOnlyModel(BaseTestModel):
    class Meta:
        read_only_model = True
