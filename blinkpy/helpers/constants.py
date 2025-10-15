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
# Updated to match Blink Android app version 47.0 (released August 2025)
# Previous version was 27.0 with build ANDROID_28373244
# New version uses build identifier ANDROID_30000192
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
