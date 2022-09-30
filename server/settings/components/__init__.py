# -*- coding: utf-8 -*-

# For some reason PurePath is throwing errors. Used Path instead
from pathlib import Path
from decouple import AutoConfig


# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing:
# BASE_DIR = dirname(dirname(dirname(dirname(__file__))))
BASE_DIR = Path(__file__).parent.parent.parent.parent

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
# config = AutoConfig(search_path=BASE_DIR.joinpath('config'))
