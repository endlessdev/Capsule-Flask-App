# -*- coding: utf-8 -*-

# -----------------------------
#  COMMON CONFIG
# -----------------------------

# ENVIRONMENT (development, production)
ENVIRONMENT = 'development'

# DEFAULT URL
DEFAULT_URL = 'http://0.0.0.0:5000'

# LOGGER FORMATTING
LOGGER_FORMAT = '[%(levelname)s][%(filename)s:%(lineno)s] %(message)s'


# -----------------------------
#  APP CONFIG
# -----------------------------

# APP DEFAULT PORT (default : 3000)
APP_DEFAULT_PORT = 5000

# APP SECRET KEY
APP_SECRET_KEY = 'f61b6dd1d53854823db8027fd0d4cb63ac7ff5475ffa3588727c53b237cfe3df'

# TOKEN
TOKEN_SCHEME = "bearer"
TOKEN_EXPIRE_TIME = 60 * 60 * 24 * 30 * 6


# -----------------------------
#  API CONFIG
# -----------------------------

# API VERSION
API_VERSION = 1

# API ACCEPT HEADER
API_ACCEPT_HEADER = 'application/json'


# -----------------------------
#  MOBILE APPLICATION CONFIG
# -----------------------------

# APPLICATION VERSION
APP_VERSION = '1.0.0'


# -----------------------------
#  GOOGLE API CONFIG
# -----------------------------

# API KEY
GOOGLE_API_KEY = 'AIzaSyCPkL05w4RW09027iQVTkeF2GvHLIlifvk'


# -----------------------------
#  DATABASE CONFIG
# -----------------------------

# DATABASE URL & SETTING
DATABASE = '%(engine)s://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s' % {
    'engine': 'mysql',
    'host': 'yeom.me',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'capsule'
}
