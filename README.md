# django-readonly-model

The easiest way to create read-only models


## Installation

Install using `pip`...

    pip install django-readonly-model


## Example

Add `'django_readonly_model'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = [
        ...
        'readonly_model',
    ]

And just use:

```python
from django.db import models

class YourModel(models.Model):
    """Some fields..."""

    class Meta:
        read_only_model = True
```
