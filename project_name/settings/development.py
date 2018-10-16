"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django {{ django_version }}.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

from .base import (ALLOWED_HOSTS, AUTH_PASSWORD_VALIDATORS,  # noqa: F401
                   BASE_DIR, DATABASE_FILE_NAME, DATABASES, DJANGO_APPS,
                   LANGUAGE_CODE, MEDIA_ROOT, MEDIA_URL, MIDDLEWARE,
                   ROOT_URLCONF, SECRET_KEY, STATIC_DIR, STATIC_ROOT,
                   STATIC_URL, STATICFILES_DIRS, TEMPLATES, TEMPLATES_DIR,
                   TIME_ZONE, USE_I18N, USE_L10N, USE_TZ, WSGI_APPLICATION,)

DEBUG = True

THIRD_PARTY_APPS = [
]

LOCAL_APPS = [
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
