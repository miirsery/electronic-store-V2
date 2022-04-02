"""
WSGI config for electronic_store_V2_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from dj_static import Cling, MediaCling
from django.core.wsgi import get_wsgi_application

# тут нужно скачать dj-static      (НЕ ЗАБЫТЬ ПОТОМ УБРАТЬ(ЗАБУДУ))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electronic_store_V2_backend.settings")

application = Cling(MediaCling(get_wsgi_application()))
