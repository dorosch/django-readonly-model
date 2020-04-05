import pytest

from readonly_model import exceptions
from tests.models import ReadOnlyModel


class TestReadOnlyModel:
    def test_save_model_instance(self):
        with pytest.raises(exceptions.ReadOnlyModel):
            ReadOnlyModel().save()

    def test_create_from_manager_model_instance(self):
        with pytest.raises(exceptions.ReadOnlyModel):
            ReadOnlyModel.objects.create()

    def test_delete_model_instance(self):
        with pytest.raises(exceptions.ReadOnlyModel):
            ReadOnlyModel().delete()

    def test_delete_from_manager_model_instance(self):
        with pytest.raises(exceptions.ReadOnlyModel):
            ReadOnlyModel.objects.all().delete()
