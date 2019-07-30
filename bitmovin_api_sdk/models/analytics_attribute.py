# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AnalyticsAttribute(Enum):
    IMPRESSION_ID = "IMPRESSION_ID"
    ACTIVE_PLAYER_STARTUPTIME = "ACTIVE_PLAYER_STARTUPTIME"
    AD = "AD"
    ANALYTICS_VERSION = "ANALYTICS_VERSION"
    ASN = "ASN"
    AUDIO_BITRATE = "AUDIO_BITRATE"
    AUDIO_CODEC = "AUDIO_CODEC"
    AUTOPLAY = "AUTOPLAY"
    BROWSER = "BROWSER"
    BROWSER_VERSION_MAJOR = "BROWSER_VERSION_MAJOR"
    BROWSER_IS_BOT = "BROWSER_IS_BOT"
    BUFFERED = "BUFFERED"
    CDN_PROVIDER = "CDN_PROVIDER"
    CITY = "CITY"
    CLIENT_TIME = "CLIENT_TIME"
    COUNTRY = "COUNTRY"
    CUSTOM_DATA_1 = "CUSTOM_DATA_1"
    CUSTOM_DATA_2 = "CUSTOM_DATA_2"
    CUSTOM_DATA_3 = "CUSTOM_DATA_3"
    CUSTOM_DATA_4 = "CUSTOM_DATA_4"
    CUSTOM_DATA_5 = "CUSTOM_DATA_5"
    CUSTOM_USER_ID = "CUSTOM_USER_ID"
    DAY = "DAY"
    DEVICE_CLASS = "DEVICE_CLASS"
    DEVICE_TYPE = "DEVICE_TYPE"
    DOMAIN = "DOMAIN"
    DRM_LOAD_TIME = "DRM_LOAD_TIME"
    DRM_TYPE = "DRM_TYPE"
    DROPPED_FRAMES = "DROPPED_FRAMES"
    DURATION = "DURATION"
    ERROR_CODE = "ERROR_CODE"
    ERROR_MESSAGE = "ERROR_MESSAGE"
    ERROR_RATE = "ERROR_RATE"
    EXPERIMENT_NAME = "EXPERIMENT_NAME"
    HOUR = "HOUR"
    INITIAL_TIME_TO_TARGET_LATENCY = "INITIAL_TIME_TO_TARGET_LATENCY"
    IP_ADDRESS = "IP_ADDRESS"
    IS_CASTING = "IS_CASTING"
    IS_LIVE = "IS_LIVE"
    IS_LOW_LATENCY = "IS_LOW_LATENCY"
    IS_MUTED = "IS_MUTED"
    ISP = "ISP"
    LANGUAGE = "LANGUAGE"
    LATENCY = "LATENCY"
    LICENSE_KEY = "LICENSE_KEY"
    M3U8_URL = "M3U8_URL"
    MINUTE = "MINUTE"
    MONTH = "MONTH"
    MPD_URL = "MPD_URL"
    OPERATINGSYSTEM = "OPERATINGSYSTEM"
    OPERATINGSYSTEM_VERSION_MAJOR = "OPERATINGSYSTEM_VERSION_MAJOR"
    PAGE_LOAD_TIME = "PAGE_LOAD_TIME"
    PAGE_LOAD_TYPE = "PAGE_LOAD_TYPE"
    PATH = "PATH"
    PAUSED = "PAUSED"
    PLATFORM = "PLATFORM"
    PLAYED = "PLAYED"
    PLAYER = "PLAYER"
    PLAYER_KEY = "PLAYER_KEY"
    PLAYER_STARTUPTIME = "PLAYER_STARTUPTIME"
    PLAYER_TECH = "PLAYER_TECH"
    PLAYER_VERSION = "PLAYER_VERSION"
    PROG_URL = "PROG_URL"
    REGION = "REGION"
    SCALE_FACTOR = "SCALE_FACTOR"
    SCREEN_HEIGHT = "SCREEN_HEIGHT"
    SCREEN_WIDTH = "SCREEN_WIDTH"
    SEEKED = "SEEKED"
    SEQUENCE_NUMBER = "SEQUENCE_NUMBER"
    SIZE = "SIZE"
    STARTUPTIME = "STARTUPTIME"
    STREAM_FORMAT = "STREAM_FORMAT"
    SUPPORTED_VIDEO_CODECS = "SUPPORTED_VIDEO_CODECS"
    TARGET_LATENCY = "TARGET_LATENCY"
    TARGET_LATENCY_DELTA = "TARGET_LATENCY_DELTA"
    TIME = "TIME"
    TIME_TO_TARGET_LATENCY = "TIME_TO_TARGET_LATENCY"
    USER_ID = "USER_ID"
    VIDEO_BITRATE = "VIDEO_BITRATE"
    VIDEO_CODEC = "VIDEO_CODEC"
    VIDEO_DURATION = "VIDEO_DURATION"
    VIDEO_ID = "VIDEO_ID"
    VIDEO_PLAYBACK_HEIGHT = "VIDEO_PLAYBACK_HEIGHT"
    VIDEO_PLAYBACK_WIDTH = "VIDEO_PLAYBACK_WIDTH"
    VIDEO_STARTUPTIME = "VIDEO_STARTUPTIME"
    VIDEO_TITLE = "VIDEO_TITLE"
    VIDEO_WINDOW_HEIGHT = "VIDEO_WINDOW_HEIGHT"
    VIDEO_WINDOW_WIDTH = "VIDEO_WINDOW_WIDTH"
    VIDEOTIME_END = "VIDEOTIME_END"
    VIDEOTIME_START = "VIDEOTIME_START"
