import pytest
from django import conf
from django.db import models

from readonly_model import settings


class TestReadOnlyAppSetting:
    def test_read_only_model_attr_in_meta_class(self):
        assert 'read_only_model' in models.options.DEFAULT_NAMES

    def test_database_routers_contain_read_only_router(self):
        assert settings.READONLY_MODEL.get('DATABASE_ROUTER') in \
            conf.settings.DATABASE_ROUTERS
