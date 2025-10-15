"""Generates constants for use in blinkpy."""

import importlib.metadata

__version__ = importlib.metadata.version("blinkpy")

"""
URLS
"""
BLINK_URL = "immedia-semi.com"
DEFAULT_URL = f"rest-prod.{BLINK_URL}"
BASE_URL = f"https://{DEFAULT_URL}"
LOGIN_ENDPOINT = f"{BASE_URL}/api/v5/account/login"

"""
Dictionaries
"""
ONLINE = {"online": True, "offline": False}

"""
OTHER
"""
# Updated to match Blink Android app version 47.0 (August 2025)
# The version code follows the pattern ANDROID_<version_code>
# Version 47.0 uses versionCode 192, which likely corresponds to a build number
# in the 30000000+ range based on historical patterns
APP_BUILD = "ANDROID_30000192"
DEFAULT_USER_AGENT = "47.0ANDROID_30000192"
DEVICE_ID = "Blinkpy"
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
DEFAULT_MOTION_INTERVAL = 1
DEFAULT_REFRESH = 30
MIN_THROTTLE_TIME = 2
SIZE_NOTIFICATION_KEY = 152
SIZE_UID = 16
TIMEOUT = 10
TIMEOUT_MEDIA = 90
