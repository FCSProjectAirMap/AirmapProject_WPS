import os

from .base import PROJECT_ROOT_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")


# Media files
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "images")
MEDIA_URL = "/media/"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'airmap': {
            'source_filenames': (
              'css/application.css',
            ),
            'output_filename': 'css/airmap.css',
        }
    },
}
