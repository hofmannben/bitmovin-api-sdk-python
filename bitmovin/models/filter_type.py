# coding: utf-8
from enum import Enum


class FilterType(Enum):
    """
    allowed enum values
    """
    CROP = "CROP"
    WATERMARK = "WATERMARK"
    ENHANCED_WATERMARK = "ENHANCED_WATERMARK"
    ROTATE = "ROTATE"
    DEINTERLACE = "DEINTERLACE"
    AUDIO_MIX = "AUDIO_MIX"
    DENOISE_HQDN3D = "DENOISE_HQDN3D"
    TEXT = "TEXT"
    UNSHARP = "UNSHARP"
    SCALE = "SCALE"
    INTERLACE = "INTERLACE"
    AUDIO_VOLUME = "AUDIO_VOLUME"
    EBU_R128_SINGLE_PASS = "EBU_R128_SINGLE_PASS"
