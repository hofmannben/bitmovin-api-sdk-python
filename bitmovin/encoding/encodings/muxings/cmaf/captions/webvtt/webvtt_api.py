# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.web_vtt_embed import WebVttEmbed
from bitmovin.encoding.encodings.muxings.cmaf.captions.webvtt.customdata.customdata_api import CustomdataApi


class WebvttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(WebvttApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, muxing_id, web_vtt_embed, **kwargs):
        """CMAF Embed WebVtt Captions"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/captions/webvtt',
            web_vtt_embed,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=WebVttEmbed,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, captions_id, **kwargs):
        """Get CMAF Embed WebVtt Captions Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/captions/webvtt/{captions_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'captions_id': captions_id},
            type=WebVttEmbed,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, **kwargs):
        """List CMAF Embed WebVtt Captions"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/cmaf/{muxing_id}/captions/webvtt',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            pagination_response=True,
            type=WebVttEmbed,
            **kwargs
        )
