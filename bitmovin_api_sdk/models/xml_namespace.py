# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class XmlNamespace(object):
    @poscheck_model
    def __init__(self,
                 prefix=None,
                 uri=None):
        # type: (string_types, string_types) -> None

        self._prefix = None
        self._uri = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if uri is not None:
            self.uri = uri

    @property
    def openapi_types(self):
        types = {
            'prefix': 'string_types',
            'uri': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'prefix': 'prefix',
            'uri': 'uri'
        }
        return attributes

    @property
    def prefix(self):
        # type: () -> string_types
        """Gets the prefix of this XmlNamespace.

        Name of the XML Namespace reference (required)

        :return: The prefix of this XmlNamespace.
        :rtype: string_types
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        # type: (string_types) -> None
        """Sets the prefix of this XmlNamespace.

        Name of the XML Namespace reference (required)

        :param prefix: The prefix of this XmlNamespace.
        :type: string_types
        """

        if prefix is not None:
            if not isinstance(prefix, string_types):
                raise TypeError("Invalid type for `prefix`, type has to be `string_types`")

        self._prefix = prefix

    @property
    def uri(self):
        # type: () -> string_types
        """Gets the uri of this XmlNamespace.

        Source of the XML Namespace reference (required)

        :return: The uri of this XmlNamespace.
        :rtype: string_types
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        # type: (string_types) -> None
        """Sets the uri of this XmlNamespace.

        Source of the XML Namespace reference (required)

        :param uri: The uri of this XmlNamespace.
        :type: string_types
        """

        if uri is not None:
            if not isinstance(uri, string_types):
                raise TypeError("Invalid type for `uri`, type has to be `string_types`")

        self._uri = uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, XmlNamespace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
