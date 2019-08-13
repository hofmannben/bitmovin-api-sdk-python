# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class PresetConfiguration(Enum):
    LIVE_HIGH_QUALITY = "LIVE_HIGH_QUALITY"
    LIVE_LOW_LATENCY = "LIVE_LOW_LATENCY"
    VOD_HIGH_QUALITY = "VOD_HIGH_QUALITY"
    VOD_HIGH_SPEED = "VOD_HIGH_SPEED"
    VOD_SPEED = "VOD_SPEED"
    VOD_STANDARD = "VOD_STANDARD"
    VOD_EXTRAHIGH_SPEED = "VOD_EXTRAHIGH_SPEED"
    VOD_VERYHIGH_SPEED = "VOD_VERYHIGH_SPEED"
    VOD_SUPERHIGH_SPEED = "VOD_SUPERHIGH_SPEED"
    VOD_ULTRAHIGH_SPEED = "VOD_ULTRAHIGH_SPEED"