"""
Django settings for appmain project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1f_wrj0#9x#o!ig0lpl(=4hy=!xmyr3q*&bui$5h-tgr6kb^7o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'train',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'appmain.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'appmain.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'


CSRF_TRUSTED_ORIGINS = [
    'https://calories.colanerxyz.xyz',
    ' https://calories.colanerxyz.xyz/register/',
    ' https://calories.colanerxyz.xyz/person_info/',
    ' https://calories.colanerxyz.xyz/login/',
    ' https://calories.colanerxyz.xyz/logout/',
    ' https://calories.colanerxyz.xyz/calories_and_bjy/',
    ' https://calories.colanerxyz.xyz/profile/',
    ' https://calories.colanerxyz.xyz/report/',
    ' https://calories.colanerxyz.xyz/breakfast/',
    ' https://calories.colanerxyz.xyz/lunch/',
    ' https://calories.colanerxyz.xyz/dinner/',
    ' https://calories.colanerxyz.xyz/snack/',
    ' https://calories.colanerxyz.xyz/activities/',
    ' https://calories.colanerxyz.xyz/eatingbase/',
    ' https://calories.colanerxyz.xyz/add_breakfast/',
    ' https://calories.colanerxyz.xyz/add_lunch/',
    ' https://calories.colanerxyz.xyz/add_dinner/',
    ' https://calories.colanerxyz.xyz/add_snack/',
    ' https://calories.colanerxyz.xyz/add_activity_view/',
    ' https://calories.colanerxyz.xyz/remove_from_list/<int:product_id>/',
    ' https://calories.colanerxyz.xyz/remove_from_list2/<int:product_id>/',
    ' https://calories.colanerxyz.xyz/delete_activity/<int:id>/',
    ' https://calories.colanerxyz.xyz/edit_person_info/',
    ' https://calories.colanerxyz.xyz/creategroup/',
    ' https://calories.colanerxyz.xyz/groupdetail/<int:group_id>/',
    ' https://calories.colanerxyz.xyz/adduser/<int:group_id>/',
    ' https://calories.colanerxyz.xyz/removeuser/<int:group_id>/',
    ' https://calories.colanerxyz.xyz/userinfo/<int:user_id>/',
    ' https://calories.colanerxyz.xyz/step1/',
    ' https://calories.colanerxyz.xyz/step2/',
    ' https://calories.colanerxyz.xyz/step3/',
    ' https://calories.colanerxyz.xyz/step4/',
    ' https://calories.colanerxyz.xyz/step5/',
    ' https://calories.colanerxyz.xyz/display_chart/',

    # Другие доверенные источники (если есть)
]


PWA_APP_NAME = 'Калькулятор калорий'
PWA_APP_DESCRIPTION = "My app description"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait-primary'
PWA_APP_START_URL = 'https://calories.colanerxyz.xyz'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/icons/1616.png',
        'sizes': '160x160'
    },
    {
        "src": "/static/icons/9696.png",
        "sizes": "96x96",
        "type": "image/png"
    },
    {
        "src": "/static/icons/152.png",
        "sizes": "152x152",
        "type": "image/png"
    },

    {
        "src": "/static/icons/192.png",
        "sizes": "192x192",
        "type": "image/png"
    },
    {
        "src": "/static/icons/384.png",
        "sizes": "384x384",
        "type": "image/png"
    },

    {
        "src": "/static/icons/512512.png",
        "sizes": "512x512",
        "type": "image/png"
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/icons/1616.png',
        'sizes': '160x160'
    },
    {
        "src": "/static/icons/512512.png",
        "sizes": "512x512",
        "type": "image/png"
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/icons/6411.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
PWA_APP_SHORTCUTS = [
    {
        'name': 'Shortcut',
        'url': '/target',
        'description': 'Shortcut to a page in my application'
    }
]
PWA_APP_SCREENSHOTS = [
    {
      'src': '/static/icons/7513.png',
      'sizes': '750x1334',
      "type": "image/png",
        "form_factor": "wide",
        "label": "Wonder Widgets"

    },
    {
        'src': '/static/icons/1072.png',
        'sizes': '1080x1920',
        "type": "image/png",
        "label": "Wonder Widgets"

    }
]


PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'serviceworker.js')