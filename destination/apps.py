from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DestinationConfig(AppConfig):
    name = 'destination'
    verbose_name = _('Destination')
