#  Core Wrapper Library
#    contains wrapper functions used for
#    integrating with other libraries

# Shortcuts
from django.shortcuts import render

# Apps
from django.apps import AppConfig

# Core
from django.core.management import execute_from_command_line

# Conf
from django.conf import settings
from django.conf.urls.static import static

# Database
from django.db import models

# Http
from django.http import JsonResponse

# Urls
from django.urls import path, re_path, include
