import os
import json
from django import template
from django.db.models import Q
from datetime import datetime, timedelta, date, timezone
from django.conf import settings
from django.contrib.auth.models import User
register = template.Library()
from urllib.parse import urlencode
from collections import OrderedDict

# settings value
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")