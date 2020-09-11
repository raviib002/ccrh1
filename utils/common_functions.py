import datetime
import urllib.parse
import random
import requests
import binascii
import json
import re
from django.contrib.auth.models import User, Group
from django.utils.html import strip_tags, format_html
from django.db.models.functions import Lower
from django.db.models import Q
from django.shortcuts import render

#Start Common Functions Here