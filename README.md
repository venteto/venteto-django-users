# venteto-django-users
Generic reusable custom user app for Django projects.

The main app files are most copied verbatim from [upstream](https://github.com/django/django/tree/main/django/contrib/auth), tweaked to replace the stock `first_name` and `last_name` conventions from upstream with slightly more international options, inspired lightly by the [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django/blob/master/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/users/models.py#L27) project.

## Rebuild
Assumes `twine` is installed and an API token is stored in a `.pypirc` file.

```bash
python -m build && twine upload dist/*
gac && gp hub main
git tag v0.0.x && gp hub --tags
```

## Installation
```bash
pip install venteto-django-users
```

## Usage
In project settings add `venteto_django_users` to `INSTALLED_APPS` and set `AUTH_USER_MODEL = 'zz_users.User'`
