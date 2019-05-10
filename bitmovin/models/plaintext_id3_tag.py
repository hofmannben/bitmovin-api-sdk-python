# coding: utf-8

from bitmovin.models.id3_tag import Id3Tag
from bitmovin.models.id3_tag_position_mode import Id3TagPositionMode
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class PlaintextId3Tag(Id3Tag):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(PlaintextId3Tag, self).openapi_types
        types.update({
            'text': 'str',
            'frame_id': 'str'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(PlaintextId3Tag, self).attribute_map
        attributes.update({
            'text': 'text',
            'frame_id': 'frameId'
        })
        return attributes

    def __init__(self, text=None, frame_id=None, *args, **kwargs):
        super(PlaintextId3Tag, self).__init__(*args, **kwargs)

        self._text = None
        self._frame_id = None
        self.discriminator = None

        self.text = text
        self.frame_id = frame_id

    @property
    def text(self):
        """Gets the text of this PlaintextId3Tag.

        Plain Text Data

        :return: The text of this PlaintextId3Tag.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PlaintextId3Tag.

        Plain Text Data

        :param text: The text of this PlaintextId3Tag.
        :type: str
        """

        if text is not None:
            if not isinstance(text, str):
                raise TypeError("Invalid type for `text`, type has to be `str`")

            self._text = text


    @property
    def frame_id(self):
        """Gets the frame_id of this PlaintextId3Tag.

        4 character long Frame ID

        :return: The frame_id of this PlaintextId3Tag.
        :rtype: str
        """
        return self._frame_id

    @frame_id.setter
    def frame_id(self, frame_id):
        """Sets the frame_id of this PlaintextId3Tag.

        4 character long Frame ID

        :param frame_id: The frame_id of this PlaintextId3Tag.
        :type: str
        """

        if frame_id is not None:
            if not isinstance(frame_id, str):
                raise TypeError("Invalid type for `frame_id`, type has to be `str`")

            self._frame_id = frame_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(PlaintextId3Tag, self).to_dict()

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
            if issubclass(PlaintextId3Tag, dict):
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
        if not isinstance(other, PlaintextId3Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
