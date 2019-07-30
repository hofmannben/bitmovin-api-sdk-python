# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input_stream import InputStream
import pprint
import six


class ConcatenationInputStream(InputStream):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 concatenation=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[ConcatenationInputConfiguration]) -> None
        super(ConcatenationInputStream, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._concatenation = list()
        self.discriminator = None

        if concatenation is not None:
            self.concatenation = concatenation

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ConcatenationInputStream, self), 'openapi_types'):
            types = getattr(super(ConcatenationInputStream, self), 'openapi_types')

        types.update({
            'concatenation': 'list[ConcatenationInputConfiguration]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ConcatenationInputStream, self), 'attribute_map'):
            attributes = getattr(super(ConcatenationInputStream, self), 'attribute_map')

        attributes.update({
            'concatenation': 'concatenation'
        })
        return attributes

    @property
    def concatenation(self):
        # type: () -> list[ConcatenationInputConfiguration]
        """Gets the concatenation of this ConcatenationInputStream.

        Concatenation configuration for the output of this stream

        :return: The concatenation of this ConcatenationInputStream.
        :rtype: list[ConcatenationInputConfiguration]
        """
        return self._concatenation

    @concatenation.setter
    def concatenation(self, concatenation):
        # type: (list) -> None
        """Sets the concatenation of this ConcatenationInputStream.

        Concatenation configuration for the output of this stream

        :param concatenation: The concatenation of this ConcatenationInputStream.
        :type: list[ConcatenationInputConfiguration]
        """

        if concatenation is not None:
            if not isinstance(concatenation, list):
                raise TypeError("Invalid type for `concatenation`, type has to be `list[ConcatenationInputConfiguration]`")

        self._concatenation = concatenation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ConcatenationInputStream, self), "to_dict"):
            result = super(ConcatenationInputStream, self).to_dict()
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConcatenationInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
