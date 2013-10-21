from os.path import dirname
BASEDIR = dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Luis Jarufe', 'luisjarufe@gmail.com'),
)
MANAGERS = ADMINS

from .database import DATABASES

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Lima'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = '%s/public/media/' % BASEDIR
MEDIA_URL = '/media/'
STATIC_ROOT = '%s/public/static/' % BASEDIR
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'i=n5763%pamg2owy%reo)2w5n5aqgb!qimsum($w9009-wq@%('

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'intifil.urls'

WSGI_APPLICATION = 'intifil.wsgi.application'

TEMPLATE_DIRS = (
    "%s/../common/templates" % BASEDIR,
    "%s/../enterprise/templates" % BASEDIR,
    "%s/../items/templates" % BASEDIR,
    "%s/../global_presence/templates" % BASEDIR,
    "%s/../sitemap/templates" % BASEDIR,    
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # local apps
    'enterprise',
    'items',
    'common',
    'global_presence',
    'teams',
    'sitemap',
    # third part apps
    'modeltranslation',
    'south',
    'easy_thumbnails',
    'compressor',
    'tinymce',
    'embed_video',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# model translation
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('it', gettext('Italian')),
    ('zh', gettext('Chinese')),
    ('ja', gettext('Japanese')),
)

# easy_thumbnails
THUMBNAIL_ALIASES = {
    '': {
        # Home
        'huge_small': {'size': (223, 223), 'crop': True, 'upload': True,
                        'upscale': True},
        'huge_wide': {'size': (466, 223), 'crop': True, 'upload': True,
                       'upscale': True},
        'huge_tall': {'size': (223, 466), 'crop': True, 'upload': True,
                       'upscale': True},
        'huge_big': {'size': (466, 466), 'crop': True, 'upload': True,
                      'upscale': True},
        'large_small': {'size': (194, 194), 'crop': True, 'upload': True,
                        'upscale': True},
        'large_wide': {'size': (408, 194), 'crop': True, 'upload': True,
                       'upscale': True},
        'large_tall': {'size': (194, 408), 'crop': True, 'upload': True,
                       'upscale': True},
        'large_big': {'size': (408, 408), 'crop': True, 'upload': True,
                      'upscale': True},
        'medium_small': {'size': (161, 161), 'crop': True, 'upload': True,
                        'upscale': True},
        'medium_wide': {'size': (342, 161), 'crop': True, 'upload': True,
                       'upscale': True},
        'medium_tall': {'size': (161, 342), 'crop': True, 'upload': True,
                       'upscale': True},
        'medium_big': {'size': (342, 342), 'crop': True, 'upload': True,
                      'upscale': True},
        'short_small': {'size': (206, 206), 'crop': True, 'upload': True,
                        'upscale': True},
        'short_wide': {'size': (432, 206), 'crop': True, 'upload': True,
                       'upscale': True},
        'short_tall': {'size': (206, 432), 'crop': True, 'upload': True,
                       'upscale': True},
        'short_big': {'size': (432, 432), 'crop': True, 'upload': True,
                      'upscale': True},
        'tiny_small': {'size': (253, 253), 'crop': True, 'upload': True,
                        'upscale': True},
        'tiny_wide': {'size': (526, 253), 'crop': True, 'upload': True,
                       'upscale': True},
        'tiny_tall': {'size': (253, 526), 'crop': True, 'upload': True,
                       'upscale': True},
        'tiny_big': {'size': (526, 526), 'crop': True, 'upload': True,
                      'upscale': True},
        # Galeria - miniaturas
        'mini_huge': {'size': (123, 90), 'crop': True, 'upload': True,
                       'upscale': True},
        # 109, 79
        'mini_large': {'size': (104, 76), 'crop': True, 'upload': True,
                       'upscale': True},
        # 105, 76
        'mini_medium': {'size': (99, 73), 'crop': True, 'upload': True,
                        'upscale': True},
        # 73, 54
        'mini_short': {'size': (70, 52), 'crop': True, 'upload': True,
                       'upscale': True},
        # 57, 43
        'mini_tiny': {'size': (55, 42), 'crop': True, 'upload': True,
                      'upscale': True},
        # Galeria - slider
        'slider_huge': {'size': (868, 759), 'crop': True, 'upload': True,
                         'upscale': True},        
        'slider_large': {'size': (770, 647), 'crop': True, 'upload': True,
                         'upscale': True},
        'slider_medium': {'size': (752, 631), 'crop': True, 'upload': True,
                          'upscale': True},
        'slider_short': {'size': (680, 508), 'crop': True, 'upload': True,
                         'upscale': True},
        'slider_tiny': {'size': (548, 409), 'crop': True, 'upload': True,
                        'upscale': True},
    },
    # GLOBAL PRESENCE
    'global_presence.Item.flag_image': {
        # sizes increased to have good quality image of the infifil flag
        'gp_item_flag_image_huge': {
            'size': (140, 100), 'crop': True, 'upload': True,
            'upscale': True, 'quality': 100},        
        # 78, 56
        'gp_item_flag_image_large': {
            'size': (120, 85), 'crop': True, 'upload': True,
            'upscale': True, 'quality': 100},
        # 68, 49
        'gp_item_flag_image_medium': {
            'size': (104, 75), 'crop': True, 'upload': True,
            'upscale': True, 'quality': 100},
        # 62, 44
        'gp_item_flag_image_short': {
            'size': (100, 70), 'crop': True, 'upload': True,
            'upscale': True, 'quality': 100},
        # 48, 35
        'gp_item_flag_image_tiny': {
            'size': (90, 65), 'crop': True, 'upload': True,
            'upscale': True, 'quality': 100},
    },
    'global_presence.Country.flag_image': {
        'gp_country_flag_image_huge': {
            'size': (90, 64), 'crop': True, 'upload': True, 'upscale': True,
            'quality': 100
        },
        # 82, 59        
        'gp_country_flag_image_large': {
            'size': (78, 56), 'crop': True, 'upload': True, 'upscale': True,
            'quality': 100
        },
        # 68, 49
        'gp_country_flag_image_medium': {
            'size': (65, 46), 'crop': True, 'upload': True, 'upscale': True,
            'quality': 100
        },
        # 62, 44
        'gp_country_flag_image_short': {
            'size': (57, 41), 'crop': True, 'upload': True, 'upscale': True,
            'quality': 100
        },
        # 48, 35
        'gp_country_flag_image_tiny': {
            'size': (44, 32), 'crop': True, 'upload': True, 'upscale': True,
            'quality': 100
        },
    },
    'global_presence.Team.image': {
        'gp_team_image_preview': {'size': (150, 150), 'upload': True,
                       'upscale': True, 'quality': 100},
        'gp_team_image_huge': {
            'size': (904, 678), 'crop': True, 'upload': True, 'upscale': True},
        'gp_team_image_large': {
            'size': (803, 602), 'crop': True, 'upload': True, 'upscale': True},
        'gp_team_image_medium': {'size': (733, 549), 'crop': True,
                                 'upload': True,
                       'upscale': True},
        'gp_team_image_short': {'size': (680, 510), 'crop': True,
                                'upload': True,
                       'upscale': True},                       
        'gp_team_image_tiny': {'size': (548, 411), 'crop': True, 'upload': True,
                       'upscale': True},
    },
    # TEAMS
    'teams.Team.photo': {
        'teams_team_photo_huge': {
            'size': (875, 575), 'crop': True, 'upload': True, 'upscale': True},
        'teams_team_photo_large': {
            'size': (800, 526), 'crop': True, 'upload': True, 'upscale': True},
        'teams_team_photo_medium': {'size': (770, 490), 'crop': True,
                                    'upload': True, 'upscale': True},
        'teams_team_photo_short': {'size': (680, 510), 'crop': True,
                                   'upload': True, 'upscale': True},
        'teams_team_photo_tiny': {'size': (548, 411), 'crop': True,
                                  'upload': True, 'upscale': True},
    },
    'teams.TeamMember.photo': {
        'teams_teammember_photo_0_huge': {
            'size': (200, 280), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_0_large': {
            'size': (200, 280), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_0_medium': {
            'size': (189, 264), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_1_huge': {
            'size': (200, 360), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_1_large': {
            'size': (200, 360), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_1_medium': {
            'size': (189, 340), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_2_huge': {
            'size': (200, 280), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_2_large': {
            'size': (200, 280), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_2_medium': {
            'size': (189, 264), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_3_huge': {
            'size': (360, 200), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_3_large': {
            'size': (360, 200), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_3_medium': {
            'size': (340, 189), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_4_huge': {
            'size': (200, 360), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_4_large': {
            'size': (200, 360), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_4_medium': {
            'size': (189, 340), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_5_huge': {
            'size': (466, 200), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_5_large': {
            'size': (466, 200), 'crop': True, 'upload': True, 'upscale': True},
        'teams_teammember_photo_5_medium': {
            'size': (440, 189), 'crop': True, 'upload': True, 'upscale': True},
    }
}

VIDEO_SIZES = {
    'huge': {'width': 868, 'height': 759},
    'large': {'width': 770, 'height': 647},
    'medium': {'width': 752, 'height': 631},
    'short': {'width': 680, 'height': 508},
    'tiny': {'width': 548, 'height': 409},
}

# admin-tools
ADMIN_TOOLS_MENU = 'intifil.menu.CustomMenu'

# django-tinymce configuration
TINYMCE_DEFAULT_CONFIG = {
    'custom_undo_redo_levels': 10,
    # General options
    #'mode': "textareas",
    'theme': "advanced",
    'plugins': ""
        "autolink,lists,spellchecker,pagebreak,style,layer,table,save,advhr,"
        "advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,"
        "preview,media,searchreplace,print,contextmenu,paste,directionality,"
        "fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    # Theme options
    'theme_advanced_buttons1': ""
        "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,"
        "justifycenter,justifyright,justifyfull,|,styleselect,formatselect,"
        "fontselect,fontsizeselect",
    'theme_advanced_buttons2': ""
        "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,"
        "numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,"
        "image,cleanup,help,code,|,insertdate,inserttime,preview,|,"
        "forecolor,backcolor",
    'theme_advanced_buttons3': ""
        "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,"
        "emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
    'theme_advanced_buttons4': ""
        "insertlayer,moveforward,movebackward,absolute,|,styleprops,"
        "spellchecker,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,"
        "nonbreaking,template,blockquote,pagebreak,|,insertfile,insertimage",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
    # Skin options
    'skin': "o2k7",
    'skin_variant': "silver",
    # Language
    'language': 'en',
}
TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = True
