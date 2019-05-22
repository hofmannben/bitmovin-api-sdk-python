# coding: utf-8

from bitmovin.models.bitmovin_resource import BitmovinResource
from bitmovin.models.convert_scc_caption_web_vtt_settings import ConvertSccCaptionWebVttSettings
from bitmovin.models.input_path import InputPath
from bitmovin.models.stream_caption_output_format import StreamCaptionOutputFormat
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class ConvertSccCaption(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ConvertSccCaption, self).openapi_types
        types.update({
            'input': 'InputPath',
            'outputs': 'list[EncodingOutput]',
            'file_name': 'str',
            'output_format': 'StreamCaptionOutputFormat',
            'web_vtt_settings': 'ConvertSccCaptionWebVttSettings'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ConvertSccCaption, self).attribute_map
        attributes.update({
            'input': 'input',
            'outputs': 'outputs',
            'file_name': 'fileName',
            'output_format': 'outputFormat',
            'web_vtt_settings': 'webVttSettings'
        })
        return attributes

    def __init__(self, input=None, outputs=None, file_name=None, output_format=None, web_vtt_settings=None, *args, **kwargs):
        super(ConvertSccCaption, self).__init__(*args, **kwargs)

        self._input = None
        self._outputs = None
        self._file_name = None
        self._output_format = None
        self._web_vtt_settings = None
        self.discriminator = None

        self.input = input
        self.outputs = outputs
        self.file_name = file_name
        self.output_format = output_format
        if web_vtt_settings is not None:
            self.web_vtt_settings = web_vtt_settings

    @property
    def input(self):
        """Gets the input of this ConvertSccCaption.

        The input location to get the scc file from

        :return: The input of this ConvertSccCaption.
        :rtype: InputPath
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ConvertSccCaption.

        The input location to get the scc file from

        :param input: The input of this ConvertSccCaption.
        :type: InputPath
        """

        if input is not None:
            if not isinstance(input, InputPath):
                raise TypeError("Invalid type for `input`, type has to be `InputPath`")

            self._input = input


    @property
    def outputs(self):
        """Gets the outputs of this ConvertSccCaption.


        :return: The outputs of this ConvertSccCaption.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ConvertSccCaption.


        :param outputs: The outputs of this ConvertSccCaption.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

            self._outputs = outputs


    @property
    def file_name(self):
        """Gets the file_name of this ConvertSccCaption.

        Name of the captions file

        :return: The file_name of this ConvertSccCaption.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ConvertSccCaption.

        Name of the captions file

        :param file_name: The file_name of this ConvertSccCaption.
        :type: str
        """

        if file_name is not None:
            if not isinstance(file_name, str):
                raise TypeError("Invalid type for `file_name`, type has to be `str`")

            self._file_name = file_name


    @property
    def output_format(self):
        """Gets the output_format of this ConvertSccCaption.


        :return: The output_format of this ConvertSccCaption.
        :rtype: StreamCaptionOutputFormat
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this ConvertSccCaption.


        :param output_format: The output_format of this ConvertSccCaption.
        :type: StreamCaptionOutputFormat
        """

        if output_format is not None:
            if not isinstance(output_format, StreamCaptionOutputFormat):
                raise TypeError("Invalid type for `output_format`, type has to be `StreamCaptionOutputFormat`")

            self._output_format = output_format


    @property
    def web_vtt_settings(self):
        """Gets the web_vtt_settings of this ConvertSccCaption.

        Optional settings when converting SCC to WebVTT

        :return: The web_vtt_settings of this ConvertSccCaption.
        :rtype: ConvertSccCaptionWebVttSettings
        """
        return self._web_vtt_settings

    @web_vtt_settings.setter
    def web_vtt_settings(self, web_vtt_settings):
        """Sets the web_vtt_settings of this ConvertSccCaption.

        Optional settings when converting SCC to WebVTT

        :param web_vtt_settings: The web_vtt_settings of this ConvertSccCaption.
        :type: ConvertSccCaptionWebVttSettings
        """

        if web_vtt_settings is not None:
            if not isinstance(web_vtt_settings, ConvertSccCaptionWebVttSettings):
                raise TypeError("Invalid type for `web_vtt_settings`, type has to be `ConvertSccCaptionWebVttSettings`")

            self._web_vtt_settings = web_vtt_settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ConvertSccCaption, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(ConvertSccCaption, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConvertSccCaption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
