import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'gunicorn',
    'djsupervisor',
    'django_extensions',
    'sekizai',
    'djangobower',
    'ckeditor',
    'lineage',
    'endless_pagination',
    'website',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai'
)

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static configuration
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

# wysiwyg settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'CMS, Full',
        'toolbar_CMS': [
            {
                'name': 'basicstyles',
                'groups': ['basicstyles', 'cleanup'],
                'items': ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat']
            },
            {
                'name': 'paragraph',
                'groups': ['list', 'indent', 'blocks'],
                'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote']
            },
            {
                'name': 'links',
                'items': ['Link', 'Unlink']
            },
            {
                'name': 'insert',
                'items': ['Image', 'HorizontalRule', 'Table', 'Iframe', ]
            },
            {
                'name': 'colors',
                'items': ['TextColor', 'BGColor']
            }
        ],
        'height': 400,
        'width': 1500,
        'skin': 'moono',
        'uiColor': '#eeeeee'
    },
}


# Bower components
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'static')
BOWER_INSTALLED_APPS = (
    'zurb/bower-foundation#5.5.0',
    'slick.js',
)

# pagination
ENDLESS_PAGINATION_PER_PAGE = 3

# load local_settings
try:
    from local_settings import *
except ImportError:
    pass
