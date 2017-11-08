from ms_site.settings.base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ms_website',
        'USER': 'root',
        'PASSWORD': os.environ.get('MYSQL_PASS', 'fallback'),
    }
}



try:
    from ms_site.settings.local import *
except:
    pass
