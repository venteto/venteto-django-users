# venteto-django-users
Generic reusable custom user app for Django projects.

## Rebuild
Assumes `twine` is installed and an API token is stored in a `.pypirc` file.

```bash
python -m build && twine upload dist/*
```

## Installation
```bash
pip install venteto-django-users
```

## Usage
In project settings add `venteto_django_users` to `INSTALLED_APPS` and set `AUTH_USER_MODEL = 'zz_users.User'`
