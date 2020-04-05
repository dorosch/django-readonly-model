import pytest

from readonly_model import exceptions

from .models import ReadOnlyModel


class TestReadOnlyModel:
    @pytest.mark.django_db
    def test_save_model_instance(self):
        with pytest.raises(exceptions.ReadOnlyModel):
            ReadOnlyModel().save()

    @pytest.mark.django_db
    def test_create_from_manager_model_instance(self):
        with pytest.raises(exceptions.ReadOnlyModel):
            ReadOnlyModel.objects.create()

    @pytest.mark.django_db
    def test_delete_model_instance(self):
        with pytest.raises(exceptions.ReadOnlyModel):
            ReadOnlyModel().delete()

    @pytest.mark.django_db
    def test_delete_from_manager_model_instance(self):
        with pytest.raises(exceptions.ReadOnlyModel):
            ReadOnlyModel.objects.all().delete()
