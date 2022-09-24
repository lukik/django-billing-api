# -*- coding: utf-8 -*-

"""
This file specifies project version.

Consider using SemVer:
https://semver.org/
"""

# TODO: Change version on release
__version__ = '0.0.0'

from .taskapp.celery import app as celery_app

__all__ = ['celery_app']
