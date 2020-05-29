# django-readonly-model

[![Build Status](https://travis-ci.org/dorosch/django-readonly-model.svg?branch=master)](https://travis-ci.org/dorosch/django-readonly-model)
[![codecov](https://codecov.io/gh/dorosch/django-project-start/branch/master/graph/badge.svg)](https://codecov.io/gh/dorosch/django-project-start)
[![PyPI version](https://badge.fury.io/py/django-readonly-model.svg)](https://badge.fury.io/py/django-readonly-model)
[![Downloads](https://pepy.tech/badge/django-readonly-model)](https://pepy.tech/project/django-readonly-model)

The easiest way to create read-only models


## Installation

Install using `pip`:

    pip install django-readonly-model


Add `'readonly_model'` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = [
        ...
        'readonly_model',
    ]

## Example

Declare a model to read:

```python
from django.db import models

class Directory(models.Model):
    class Meta:
        read_only_model = True
```

We can read data from the model but we cannot write:

```python
>>> from app.models import Directory
>>> Directory.objects.count()
0
>>> Directory.objects.create(name='kg')
...
readonly_model.exceptions.ReadOnlyModel: Model 'app.models.Directory' is read-only
```

You cannot write but you can load data from fixtures:

```bash
$ python3 manage.py loaddata fixtures/directory.json
```

```python
>>> from app.models import Directory
>>> Directory.objects.count()
3
```


## When is it needed?

- When you want to protect the model from accidental recording.

- When you have some data that cannot be changed programmatically (for example, various directories).

- When you need to use a read-only model from a database that you cannot write to it.
